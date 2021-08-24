import re
import typing

import site_key

# Setting up variables for testing
GCLOUD_PROJECT = "your-gcloud-project-id"
DOMAIN_NAME = "localhost"


def test_recaptcha_site_key(capsys: typing.Any) -> None:
    recaptcha_site_key = site_key.main(GCLOUD_PROJECT, DOMAIN_NAME)

    out, _ = capsys.readouterr()

    assert f"reCAPTCHA Site key created successfully. Site Key:" in out
    assert len(recaptcha_site_key) != 0
    assert f"{recaptcha_site_key}" in out
    assert re.search(f"Successfully obtained the key !.+{recaptcha_site_key}", out)
    assert f"reCAPTCHA Site key successfully updated ! " in out
    assert f"reCAPTCHA Site key deleted successfully !" in out
