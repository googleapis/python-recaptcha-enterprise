# Google Cloud reCAPTCHA Enterprise


<a href="https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-recaptcha-enterprise&page=editor&open_in_editor=samples/demosite_application/README.md">
<img alt="Open in Cloud Shell" src ="http://gstatic.com/cloudssh/images/open-btn.png"></a>

or 

[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run/?git_repo=https://github.com/googleapis/python-recaptcha-enterprise.git&revision=demosite-app&dir=samples/demosite_application)

Google [Cloud reCAPTCHA Enterprise](https://cloud.google.com/recaptcha-enterprise) helps protect your website from fraudulent activity, spam, and abuse without creating friction.

This application demonstrates the technical costs of integrating reCAPTCHA Enterprise using the Python Client Libraries.

## Prerequisites

### Google Cloud Project

Set up a Google Cloud project with billing enabled.

### Enable the API

You must [enable the Google reCAPTCHA Enterprise API](https://console.cloud.google.com/flows/enableapi?apiid=recaptchaenterprise.googleapis.com) for your project in order to use this application.

### Service account

A service account with private key credentials is required to create signed bearer tokens.
Create a [service account](https://console.cloud.google.com/iam-admin/serviceaccounts/create) and download the credentials file as JSON.

### Create Score key and Checkbox key

Create a Score key, and a Checkbox key via [Cloud Console.](https://console.cloud.google.com/security/recaptcha)

### Set Environment Variables

You must set your project ID and service account credentials in order to run the tests.

```
$ export GOOGLE_CLOUD_PROJECT="<google-project-id-here>"
$ export GOOGLE_APPLICATION_CREDENTIALS="<path-to-service-account-credentials-file>"
$ export SITE_KEY="<score-key-id-here>"
$ export CHECKBOX_SITE_KEY="<checkbox-key-id-here>"
```

### Grant Permissions

You must ensure that the [user account or service account](https://cloud.google.com/iam/docs/service-accounts#differences_between_a_service_account_and_a_user_account) you used to authorize your gcloud session has the proper permissions to edit reCAPTCHA Enterprise resources for your project. In the Cloud Console under IAM, add the following roles to the project whose service account you're using to test:

* reCAPTCHA Enterprise Agent
* reCAPTCHA Enterprise Admin

More information can be found in the [Google reCAPTCHA Enterprise Docs](https://cloud.google.com/recaptcha-enterprise/docs/access-control#rbac_iam).


## Build and Run

The following instructions will help you prepare your development environment.


1. Clone the python-recaptcha-enterprise repository.
```
git clone https://github.com/googleapis/python-recaptcha-enterprise.git
```

2. Navigate to the sample code directory.

```
cd python-recaptcha-enterprise/samples/demosite_application
```

3. Install all the requirements as mentioned in the requirements.txt file.


4. Run the **main.py** file.
