# Copyright 2021 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START recaptcha_enterprise_account_defender_assessment]
from google.cloud import recaptchaenterprise_v1


def account_defender_assessment(project_id: str, recaptcha_site_key: str, token: str, recaptcha_action: str,
                                hashed_account_id: str) -> None:
    """ This assessment detects account takeovers.
        Input -> Pass in the hashed account id.
        Result -> Tells if the action represents an account takeover.
        You can optionally take actions (to trigger an MFA) based on the result.
    Args:
        project_id: Google Cloud Project ID
        recaptcha_site_key: Site key obtained by registering a domain/app to use recaptcha
                          services.
        token: The token obtained from the client on passing the recaptchaSiteKey.
        recaptcha_action: Action name corresponding to the token.
        hashed_account_id: HMAC SHA 256- Hashed account id of the user executing the action.
    """

    client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceClient()

    # Set the properties of the event to be tracked.
    event = recaptchaenterprise_v1.Event()
    event.site_key = recaptcha_site_key
    event.token = token
    # Set the hashed account id (of the user).
    # Recommended approach: HMAC SHA256 along with salt (or secret key).
    event.hashed_account_id = hashed_account_id

    assessment = recaptchaenterprise_v1.Assessment()
    assessment.event = event

    project_name = f"projects/{project_id}"

    # Build the assessment request.
    request = recaptchaenterprise_v1.CreateAssessmentRequest()
    request.parent = project_name
    request.assessment = assessment

    response = client.create_assessment(request)

    # Check integrity of the response token.
    if not check_token_integrity(response.token_properties, recaptcha_action):
        return
    else:
        # Get the risk score and the reason(s)
        # For more information on interpreting the assessment,
        # see: https://cloud.google.com/recaptcha-enterprise/docs/interpret-assessment
        for reason in response.risk_analysis.reasons:
            print(reason)
        print(
            "The reCAPTCHA score for this token is: "
            + str(response.risk_analysis.score)
        )

        # Get the Account Defender result.
        # Based on the result, can you choose next steps.
        # Few result labels: ACCOUNT_DEFENDER_LABEL_UNSPECIFIED, PROFILE_MATCH,
        # SUSPICIOUS_LOGIN_ACTIVITY, SUSPICIOUS_ACCOUNT_CREATION, RELATED_ACCOUNTS_NUMBER_HIGH.
        # For more info on these types, see: TODO
        print(f"Account Defender Assessment Result: {response.account_defender_assessment.labels}")


def check_token_integrity(token_properties: recaptchaenterprise_v1.TokenProperties, recaptcha_action: str) -> bool:
    # Check if the token is valid.
    if not token_properties.valid:
        print(
            "The CreateAssessment call failed because the token was "
            + "invalid for for the following reasons: "
            + str(token_properties.invalid_reason)
        )
        return False

    # Check if the expected action was executed.
    if token_properties.action != recaptcha_action:
        print(f"The action attribute in your reCAPTCHA tag: {token_properties.action} does"
              + f"not match the action you are expecting to score: {recaptcha_action}"
              )
        return False
    return True

# [END recaptcha_enterprise_account_defender_assessment]
