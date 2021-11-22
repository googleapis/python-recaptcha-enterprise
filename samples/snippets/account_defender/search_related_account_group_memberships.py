# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START recaptcha_enterprise_search_related_account_group_membership]
from google.cloud import recaptchaenterprise_v1


def search_related_account_group_memberships(project_id: str, hashed_account_id: str) -> None:
    """ List group memberships for the account id.
    Args:
        project_id: Google Cloud Project Id.
        hashed_account_id: HMAC SHA 256- Hashed account id of the user executing the action.
    """
    client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceClient()

    request = recaptchaenterprise_v1.SearchRelatedAccountGroupMembershipsRequest()
    request.parent = f"projects/{project_id}"
    request.hashed_account_id = hashed_account_id

    response = client.search_related_account_group_memberships(request)

    for page in response.pages:
        print(page.related_account_group_memberships.name)
    print("Group membership listing: DONE")

# [END recaptcha_enterprise_search_related_account_group_membership]
