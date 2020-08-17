from main import build_cms_data
import os

# Put the service-account.json within the same directory!
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service-account.json"
os.environ["ENVIRONMENT"] = "development"

build_cms_data({})
