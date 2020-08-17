
from google.cloud import storage
import requests
import os
import certifi
import json
from dotenv import load_dotenv

# Set correct SSL certificate
os.environ['SSL_CERT_FILE'] = certifi.where()


def build_cms_data(data):
    print(data)

    if os.getenv("ENVIRONMENT") == "development":
        TMP = "./tmp/"
    else:
        TMP = "/tmp/"

    load_dotenv()

    CMS_URL = os.environ.get("CMS_CACHE_CMS_URL")
    BUCKET_NAME = os.environ.get("CMS_CACHE_BUCKET_NAME")
    REL_PATH = os.environ.get("CMS_CACHE_REL_PATH")
    RESOURCES = os.environ.get("CMS_CACHE_RESOURCES")
    DELIMITER = os.environ.get("CMS_CACHE_DELIMITER")

    assert CMS_URL is not None, "CMS_CACHE_CMS_URL not set"
    assert BUCKET_NAME is not None, "CMS_CACHE_BUCKET_NAME not set"
    assert REL_PATH is not None, "CMS_CACHE_REL_PATH not set"
    assert RESOURCES is not None, "CMS_CACHE_RESOURCES not set"
    assert DELIMITER is not None, "CMS_CACHE_DELIMITER not set"

    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)

    for resource in RESOURCES.split(DELIMITER):
        src = CMS_URL + resource
        dst = resource + ".json"
        tmp_path = TMP + dst
        print(f"Downloading {src} to {tmp_path} ...")

        with open(tmp_path, 'w') as outfile:
            data = requests.get(src).json()
            json.dump(data, outfile)

        bucket.blob(dst).upload_from_filename(tmp_path)
        os.remove(tmp_path)
