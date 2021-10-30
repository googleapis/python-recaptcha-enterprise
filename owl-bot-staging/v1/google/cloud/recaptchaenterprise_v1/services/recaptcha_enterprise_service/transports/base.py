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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union
import pkg_resources

import google.auth  # type: ignore
import google.api_core  # type: ignore
from google.api_core import exceptions as core_exceptions  # type: ignore
from google.api_core import gapic_v1    # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account # type: ignore

from google.cloud.recaptchaenterprise_v1.types import recaptchaenterprise
from google.protobuf import empty_pb2  # type: ignore

try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            'google-cloud-recaptcha-enterprise',
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


class RecaptchaEnterpriseServiceTransport(abc.ABC):
    """Abstract transport class for RecaptchaEnterpriseService."""

    AUTH_SCOPES = (
        'https://www.googleapis.com/auth/cloud-platform',
    )

    DEFAULT_HOST: str = 'recaptchaenterprise.googleapis.com'
    def __init__(
            self, *,
            host: str = DEFAULT_HOST,
            credentials: ga_credentials.Credentials = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            **kwargs,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
        """
        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ':' not in host:
            host += ':443'
        self._host = host

        scopes_kwargs = {"scopes": scopes, "default_scopes": self.AUTH_SCOPES}

        # Save the scopes.
        self._scopes = scopes

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs("'credentials_file' and 'credentials' are mutually exclusive")

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                                credentials_file,
                                **scopes_kwargs,
                                quota_project_id=quota_project_id
                            )

        elif credentials is None:
            credentials, _ = google.auth.default(**scopes_kwargs, quota_project_id=quota_project_id)

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if always_use_jwt_access and isinstance(credentials, service_account.Credentials) and hasattr(service_account.Credentials, "with_always_use_jwt_access"):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.create_assessment: gapic_v1.method.wrap_method(
                self.create_assessment,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.annotate_assessment: gapic_v1.method.wrap_method(
                self.annotate_assessment,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.create_key: gapic_v1.method.wrap_method(
                self.create_key,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.list_keys: gapic_v1.method.wrap_method(
                self.list_keys,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_key: gapic_v1.method.wrap_method(
                self.get_key,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.update_key: gapic_v1.method.wrap_method(
                self.update_key,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.delete_key: gapic_v1.method.wrap_method(
                self.delete_key,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.migrate_key: gapic_v1.method.wrap_method(
                self.migrate_key,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_metrics: gapic_v1.method.wrap_method(
                self.get_metrics,
                default_timeout=None,
                client_info=client_info,
            ),
         }

    def close(self):
        """Closes resources associated with the transport.

       .. warning::
            Only call this method if the transport is NOT shared
            with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def create_assessment(self) -> Callable[
            [recaptchaenterprise.CreateAssessmentRequest],
            Union[
                recaptchaenterprise.Assessment,
                Awaitable[recaptchaenterprise.Assessment]
            ]]:
        raise NotImplementedError()

    @property
    def annotate_assessment(self) -> Callable[
            [recaptchaenterprise.AnnotateAssessmentRequest],
            Union[
                recaptchaenterprise.AnnotateAssessmentResponse,
                Awaitable[recaptchaenterprise.AnnotateAssessmentResponse]
            ]]:
        raise NotImplementedError()

    @property
    def create_key(self) -> Callable[
            [recaptchaenterprise.CreateKeyRequest],
            Union[
                recaptchaenterprise.Key,
                Awaitable[recaptchaenterprise.Key]
            ]]:
        raise NotImplementedError()

    @property
    def list_keys(self) -> Callable[
            [recaptchaenterprise.ListKeysRequest],
            Union[
                recaptchaenterprise.ListKeysResponse,
                Awaitable[recaptchaenterprise.ListKeysResponse]
            ]]:
        raise NotImplementedError()

    @property
    def get_key(self) -> Callable[
            [recaptchaenterprise.GetKeyRequest],
            Union[
                recaptchaenterprise.Key,
                Awaitable[recaptchaenterprise.Key]
            ]]:
        raise NotImplementedError()

    @property
    def update_key(self) -> Callable[
            [recaptchaenterprise.UpdateKeyRequest],
            Union[
                recaptchaenterprise.Key,
                Awaitable[recaptchaenterprise.Key]
            ]]:
        raise NotImplementedError()

    @property
    def delete_key(self) -> Callable[
            [recaptchaenterprise.DeleteKeyRequest],
            Union[
                empty_pb2.Empty,
                Awaitable[empty_pb2.Empty]
            ]]:
        raise NotImplementedError()

    @property
    def migrate_key(self) -> Callable[
            [recaptchaenterprise.MigrateKeyRequest],
            Union[
                recaptchaenterprise.Key,
                Awaitable[recaptchaenterprise.Key]
            ]]:
        raise NotImplementedError()

    @property
    def get_metrics(self) -> Callable[
            [recaptchaenterprise.GetMetricsRequest],
            Union[
                recaptchaenterprise.Metrics,
                Awaitable[recaptchaenterprise.Metrics]
            ]]:
        raise NotImplementedError()


__all__ = (
    'RecaptchaEnterpriseServiceTransport',
)
