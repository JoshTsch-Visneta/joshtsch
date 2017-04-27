from joshtsch import *

def load_config(filename):
    """ Opens and returns the contents of a .YAML configuration file to a python dictionary """

    logger.info("config file specified: %s", filename)
    with open(filename, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
        return cfg