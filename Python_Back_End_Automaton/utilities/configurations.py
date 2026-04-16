
import configparser


def getConfig():
    config = configparser.ConfigParser()    # the method stored in one variable
    config.read('Python_Back_End_Automaton/utilities/properties.ini')   # the variable now has all the knowledge about allt he values present in the properties.ini file.
    return config

