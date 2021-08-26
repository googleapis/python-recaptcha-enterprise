import time
import typing

import google
import pytest
from flask import url_for
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import create_assessment
import site_key
from app import create_app

# TODO(developer): Replace these variables before running the sample.
PROJECT = google.auth.default()[1]
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
    recaptcha_site_key = site_key.create_site_key(project_id=PROJECT, domain_name=DOMAIN_NAME)
    yield recaptcha_site_key
    site_key.delete_site_key(project_id=PROJECT, recaptcha_site_key=recaptcha_site_key)


@pytest.mark.usefixtures('live_server')
class TestLiveServer(object):

    def test_create_assessment(self, capsys: typing.Any, recaptcha_site_key, browser) -> None:
        token, action = self.get_token(recaptcha_site_key, browser)
        self.assess_token(recaptcha_site_key, token=token, action=action)
        out, _ = capsys.readouterr()
        assert f"The reCAPTCHA score for this token is: " in out
        score = out.rsplit(":", maxsplit=1)[1].strip()
        self.set_score(browser, score)

    def get_token(self, recaptcha_site_key, browser):
        browser.get(url_for('assess', site_key=recaptcha_site_key, _external=True))
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
        create_assessment.create_assessment(project_id=PROJECT, recaptcha_site_key=recaptcha_site_key,
                                            token=token,
                                            recaptcha_action=action)

    def set_score(self, browser, score: str) -> None:
        browser.find_element_by_css_selector("#assessment").send_keys(score)
