# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START recaptcha_enterprise_list_related_account_group]
from google.cloud import recaptchaenterprise_v1


def list_related_account_groups(project_id: str) -> None:
    """ List related account groups in the project.
    Args:
        project_id: Google Cloud Project Id.
    """
    client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceClient()

    request = recaptchaenterprise_v1.ListRelatedAccountGroupsRequest()
    request.parent = f"projects/{project_id}"

    response = client.list_related_account_groups(request)

    for account_group in response:
        print(account_group.name)
    print("Account groups listing: DONE")

# [END recaptcha_enterprise_list_related_account_group]
