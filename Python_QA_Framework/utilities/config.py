import configparser
import os
from pathlib import Path
from dotenv import load_dotenv

ENV_PATH = Path(__file__).resolve().parents[1] / ".env"
CONFIG_PATH = Path(__file__).resolve().parents[1] / "config" / "properties.ini"
load_dotenv(ENV_PATH)


def get_credentials(username_key, secret_key, service_name):
    user = os.getenv(username_key)
    secret = os.getenv(secret_key)

    if not user or not secret:
        raise ValueError(
            f"Missing {service_name} credentials. "
            f"Set {username_key} and {secret_key} in your environment."
        )

    return user, secret


def get_github_credentials():
    return get_credentials(
        "GitHub_API_username",
        "GitHub_API_token",
        "GitHub"
    )


def get_mysql_credentials():
    return get_credentials(
        "mysql_username",
        "mysql_password",
        "MySQL"
    )


def get_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)

    if "API" not in config:
        raise ValueError(f"Missing API section in config file: {CONFIG_PATH}")

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
