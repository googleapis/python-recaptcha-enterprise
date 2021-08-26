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

import re
import typing

import google

import site_key

# TODO(developer): Replace these variables before running the sample.
GOOGLE_CLOUD_PROJECT = google.auth.default()[1]
DOMAIN_NAME = "localhost"


def test_recaptcha_site_key(capsys: typing.Any) -> None:
    recaptcha_site_key = site_key.main(GOOGLE_CLOUD_PROJECT, DOMAIN_NAME)

    out, _ = capsys.readouterr()

    assert f"reCAPTCHA Site key created successfully. Site Key:" in out
    assert len(recaptcha_site_key) != 0
    assert f"{recaptcha_site_key}" in out
    assert re.search(f"Successfully obtained the key !.+{recaptcha_site_key}", out)
    assert f"reCAPTCHA Site key successfully updated ! " in out
    assert f"reCAPTCHA Site key deleted successfully !" in out
