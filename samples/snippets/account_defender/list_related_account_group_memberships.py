# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START recaptcha_enterprise_list_related_account_group_membership]
from google.cloud import recaptchaenterprise_v1


def list_related_account_group_memberships(project_id: str, related_account_group: str) -> None:
    """ List memberships in a group.
    Args:
        project_id: Google Cloud Project Id.
        related_account_group: Name of the account group.
    """
    client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceClient()

    request = recaptchaenterprise_v1.ListRelatedAccountGroupMembershipsRequest()
    request.parent = f"projects/{project_id}/relatedaccountgroups/{related_account_group}"

    response = client.list_related_account_group_memberships(request)

    for membership in response:
        print(membership.name)
    print("Membership listing: DONE")

# [END recaptcha_enterprise_list_related_account_group_membership]
