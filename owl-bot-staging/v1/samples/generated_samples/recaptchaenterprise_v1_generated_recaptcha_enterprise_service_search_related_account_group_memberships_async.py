# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for SearchRelatedAccountGroupMemberships
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-recaptcha-enterprise


# [START recaptchaenterprise_v1_generated_RecaptchaEnterpriseService_SearchRelatedAccountGroupMemberships_async]
from google.cloud import recaptchaenterprise_v1


async def sample_search_related_account_group_memberships():
    # Create a client
    client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceAsyncClient()

    # Initialize request argument(s)
    request = recaptchaenterprise_v1.SearchRelatedAccountGroupMembershipsRequest(
        parent="parent_value",
    )

    # Make the request
    page_result = client.search_related_account_group_memberships(request=request)

    # Handle the response
    async for response in page_result:
        print(response)

# [END recaptchaenterprise_v1_generated_RecaptchaEnterpriseService_SearchRelatedAccountGroupMemberships_async]
