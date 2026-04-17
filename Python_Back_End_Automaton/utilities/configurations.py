
import configparser
import os
from dotenv import load_dotenv

load_dotenv()
def getCredentials():
    user = os.getenv("GitHub_API_username")
    token = os.getenv("GitHub_API_token")
    return user, token


def getConfig():
    config = configparser.ConfigParser()    # the method stored in one variable
    config.read('Python_Back_End_Automaton/utilities/properties.ini')   # the variable now has all the knowledge about allt he values present in the properties.ini file.
    return config

