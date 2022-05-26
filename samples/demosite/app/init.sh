#!/usr/bin/env bash

# Enabling the reCAPTCHA Enterprise API
gcloud services enable recaptchaenterprise.googleapis.com

# gcloud command to get the current GOOGLE Project id.
export GOOGLE_CLOUD_PROJECT=$(gcloud config list --format 'value(core.project)' 2>/dev/null)

# gcloud command to create reCAPTCHA keys.
gcloud alpha recaptcha keys create --display-name=demo-recaptcha-score-key --web --allow-all-domains --integration-type=SCORE 1>/dev/null 2>recaptchascorekeyfile
export SITE_KEY=$(cat recaptchascorekeyfile | sed -n -e 's/.*Created \[\([0-9a-zA-Z_-]\+\)\].*/\1/p')
gcloud alpha recaptcha keys create --display-name=demo-recaptcha-checkbox-key --web --allow-all-domains --integration-type=CHECKBOX 1>/dev/null 2>recaptchacheckboxkeyfile
export CHECKBOX_SITE_KEY=$(cat recaptchacheckboxkeyfile | sed -n -e 's/.*Created \[\([0-9a-zA-Z_-]\+\)\].*/\1/p')

# build and run the local dockerfile in the port 8080.
docker build --build-arg GOOGLE_CLOUD_PROJECT=${GOOGLE_CLOUD_PROJECT} --build-arg SITE_KEY=${SITE_KEY} --build-arg CHECKBOX_SITE_KEY=${CHECKBOX_SITE_KEY} -t test .
docker run -d -p 8080:8080 test:latest
