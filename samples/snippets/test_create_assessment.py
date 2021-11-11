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

import os
import re
import time
import typing

from _pytest.capture import CaptureFixture
from flask import Flask, render_template, url_for
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


# TODO(developer): Replace these variables before running the sample.
from create_site_key import create_site_key
from delete_site_key import delete_site_key
from samples.snippets import annotate_assessment, create_assessment

GOOGLE_CLOUD_PROJECT = os.environ["GOOGLE_CLOUD_PROJECT"]
DOMAIN_NAME = "localhost"
ASSESSMENT_NAME = ""


@pytest.fixture(scope="session")
def app() -> Flask:
    app = Flask(__name__)

    @app.route("/assess/<site_key>", methods=["GET"])
    def assess(site_key: str) -> str:
        return render_template("index.html", site_key=site_key)

    @app.route("/", methods=["GET"])
    def index() -> str:
        return "Helloworld!"

    return app


@pytest.fixture(scope="module")
def browser() -> WebDriver:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    yield browser
    browser.close()


@pytest.fixture(scope="module")
def recaptcha_site_key() -> str:
    recaptcha_site_key = create_site_key(
        project_id=GOOGLE_CLOUD_PROJECT, domain_name=DOMAIN_NAME
    )
    yield recaptcha_site_key
    delete_site_key(
        project_id=GOOGLE_CLOUD_PROJECT, recaptcha_site_key=recaptcha_site_key
    )


@pytest.mark.dependency()
@pytest.mark.usefixtures("live_server")
def test_create_assessment(
    capsys: CaptureFixture, recaptcha_site_key: str, browser: WebDriver
) -> None:
    global ASSESSMENT_NAME
    token, action = get_token(recaptcha_site_key, browser)
    assess_token(recaptcha_site_key, token=token, action=action)
    out, _ = capsys.readouterr()
    score = -1
    for line in out.split("\n"):
        if "The reCAPTCHA score for this token is" in line:
            score = line.rsplit(":", maxsplit=1)[1].strip()
        elif "Assessment name: " in line:
            ASSESSMENT_NAME = line.rsplit(":", maxsplit=1)[1].strip()
    assert score != -1 and ASSESSMENT_NAME != ""
    set_score(browser, score)


@pytest.mark.dependency(depends=['test_create_assessment'])
def test_annotate_assessment(capsys: CaptureFixture) -> None:
    annotate_assessment.annotate_assessment(project_id=GOOGLE_CLOUD_PROJECT, assessment_id=ASSESSMENT_NAME)
    out, _ = capsys.readouterr()
    assert re.search("Annotated response sent successfully ! ", out)


def get_token(recaptcha_site_key: str, browser: WebDriver) -> typing.Tuple:
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


def assess_token(recaptcha_site_key: str, token: str, action: str) -> None:
    create_assessment.create_assessment(
        project_id=GOOGLE_CLOUD_PROJECT,
        recaptcha_site_key=recaptcha_site_key,
        token=token,
        recaptcha_action=action,
    )


def set_score(browser: WebDriver, score: str) -> None:
    browser.find_element_by_css_selector("#assessment").send_keys(score)
