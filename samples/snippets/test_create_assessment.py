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
import time
import typing

import pytest
from flask import url_for
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import create_assessment
import google
import site_key
from app import create_app

# TODO(developer): Replace these variables before running the sample.
GOOGLE_CLOUD_PROJECT = google.auth.default()[1]
DOMAIN_NAME = "localhost"


@pytest.fixture(scope="session")
def app():
    return create_app()


@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    yield browser
    browser.close()


@pytest.fixture(scope="module")
def recaptcha_site_key():
    recaptcha_site_key = site_key.create_site_key(project_id=GOOGLE_CLOUD_PROJECT, domain_name=DOMAIN_NAME)
    yield recaptcha_site_key
    site_key.delete_site_key(project_id=GOOGLE_CLOUD_PROJECT, recaptcha_site_key=recaptcha_site_key)


@pytest.mark.usefixtures('live_server')
class TestLiveServer(object):

    def test_create_assessment(self, capsys: typing.Any, recaptcha_site_key, browser) -> None:
        token, action = self.get_token(recaptcha_site_key, browser)
        self.assess_token(recaptcha_site_key, token=token, action=action)
        out, _ = capsys.readouterr()
        assert re.search("The reCAPTCHA score for this token is: ", out)
        score = out.rsplit(":", maxsplit=1)[1].strip()
        self.set_score(browser, score)

    def get_token(self, recaptcha_site_key, browser) -> typing.Tuple:
        browser.get(url_for("assess", site_key=recaptcha_site_key, _external=True))
        time.sleep(5)

        browser.find_element_by_id("username").send_keys("username")
        browser.find_element_by_id("password").send_keys("password")
        browser.find_element_by_id("recaptchabutton").click()

        # Timeout of 5 seconds
        time.sleep(5)

        element = browser.find_element_by_css_selector("#assessment")
        token = element.get_attribute("data-token")
        action = element.get_attribute("data-action")
        return token, action

    def assess_token(self, recaptcha_site_key: str, token: str, action: str) -> None:
        create_assessment.create_assessment(project_id=GOOGLE_CLOUD_PROJECT, recaptcha_site_key=recaptcha_site_key,
                                            token=token,
                                            recaptcha_action=action)

    def set_score(self, browser, score: str) -> None:
        browser.find_element_by_css_selector("#assessment").send_keys(score)
