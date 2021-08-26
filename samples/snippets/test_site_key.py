import re
import typing

import google

import site_key

# TODO(developer): Replace these variables before running the sample.
PROJECT = google.auth.default()[1]
DOMAIN_NAME = "localhost"


def test_recaptcha_site_key(capsys: typing.Any) -> None:
    recaptcha_site_key = site_key.main(PROJECT, DOMAIN_NAME)

    out, _ = capsys.readouterr()

    assert f"reCAPTCHA Site key created successfully. Site Key:" in out
    assert len(recaptcha_site_key) != 0
    assert f"{recaptcha_site_key}" in out
    assert re.search(f"Successfully obtained the key !.+{recaptcha_site_key}", out)
    assert f"reCAPTCHA Site key successfully updated ! " in out
    assert f"reCAPTCHA Site key deleted successfully !" in out
