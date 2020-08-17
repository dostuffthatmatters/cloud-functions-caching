#!/usr/bin/env bash

gcloud functions deploy build_cms_data --entry-point=build_cms_data --runtime python37 --trigger-http --region=europe-west3
