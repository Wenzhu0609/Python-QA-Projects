import configparser
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


def get_credentials():
    user = os.getenv("GitHub_API_username")
    token = os.getenv("GitHub_API_token")

    if not user or not token:
        raise ValueError(
            "Missing GitHub credentials. Set GitHub_API_username and GitHub_API_token in your environment."
        )

    return user, token


def get_config():
    config = configparser.ConfigParser()
    config_path = Path(__file__).resolve().parent / "properties.ini"
    config.read(config_path)

    if "API" not in config:
        raise ValueError(f"Missing API section in config file: {config_path}")

    return config


def get_github_url(path=""):
    base_url = get_config()["API"]["github_endpoint"]
    return f"{base_url}{path}"


def get_rsa_url(path=""):
    base_url = get_config()["API"]["rsa_endpoint"]
    return f"{base_url}{path}"


def get_httpbin_url(path=""):
    base_url = get_config()['API']['httpbin_endpoint']
    return f"{base_url}{path}"


def get_swagger_petstore_url(path=""):
    base_url = get_config()['API']['swagger_petstore_endpoint']
    return f"{base_url}{path}"

