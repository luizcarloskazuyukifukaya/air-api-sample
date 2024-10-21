# ======================================
# Python Wasabi Air SDK
# Python SDK for Wasabi Air API Access
# No guaranty from Wasabi Inc.
# ======================================

# Define function to parse configuration file (curio.conf)
# INPUT: config file
# OUTPUT: dictionary {'endpoint_url':'<URL>', 'api_key_value':'<API_KEY_VALUE>', 'profile':'<PROFILE_NAME>'}
# -------------------------------------------------------------------------------------------------------------
# Example config file
# [default]
# endpoint_url = https://us.metafarm.dev
# api_key_value = xxxxxxxxxxxxxxxxxxxxxxxx
# [wasabi]
# endpoint_url = https://us.metafarm.dev
# api_key_value = xxxxxxxxxxxxxxxxxxxxxxxx
# EOF
# -------------------------------------------------------------------------------------------------------------

import sys
import logging

# GLOBAL Variables
# TODO
global GBL_CURIO_LOG_LEVEL

GBL_CURIO_LOG_LEVEL = 10
# Global Profile defined here
DEFAULT_CURIO_PROFILE = "default"
DEFAULT_CURIO_CONF_SUB_PATH = "/.wasabi/"

# Create logger object
logging.basicConfig()   # This is important
logger = logging.getLogger(__name__)

# Set logging level (default is WARNING)
# DEBUG    - 10
# INFO     - 20
# WARNING  - 30
# ERROR    - 40
# CRITICAL - 50

# logger samples
# logger.info("This is a info log.")
# logger.warning("This is a warning log.")

# Set logging level
logger.setLevel(GBL_CURIO_LOG_LEVEL)
level = logger.level

logger.debug(f"Current Logging Level is {level}")

from os.path import expanduser
home = expanduser("~")

# return value when the input is not valid
INVALID_KEY = 'no_key'
INVALID_VALUE = ''

def parse_conf(profile):
    DEFAULT_CONF_PATH = '/.wasabi/curio.conf' #DEFAULT Configure relative path
    target_profile = ''
 
    curio_api_inf = {'api_key':'', 'endpoint':''}

    if len(profile) == 0:
        profile = 'default'
    
    logger.info(f"Target profile is {profile}")

    # profile is set either default or specific value    
    target_profile = '[' + profile + ']';
    
    # open configuration file
    conf_file_path = home + DEFAULT_CONF_PATH;
    file = open(conf_file_path, 'r')
    lines = file.readlines()
    
    target_profile_found = False
    target_counts = 0 # when both key found, the configuration file read to end
    for line in lines:
        l = line.strip()
        if len(l) == 0:
            continue

        # line is not spaced only
        k , v = extract_key(l)
            
        if k == INVALID_KEY:
            continue

        if k == target_profile:
            target_profile_found = True
            continue

        if target_profile_found == False:
            continue
        
        # only when the target profile is found
        if k == 'api_key_value':
            curio_api_inf['api_key'] = v
            target_counts = target_counts + 1

        if k == 'endpoint_url':
            curio_api_inf['endpoint'] = v
            target_counts = target_counts + 1
        
        if target_counts == 2:
            break                
    # read line and identify the start of profile information   
    # return Wasabi AiR API configuration information as dictionary
    return curio_api_inf


def extract_key(l):
    # space only line
    l = l.strip()
    if len(l) == 0:
        return INVALID_KEY, INVALID_VALUE;
    
    # l should have content, but skip comments (line starting with #)
    if l[0] == '#':
        return INVALID_KEY, INVALID_VALUE;
    
    # l should have content, but skip comments (line starting with #)
    if l[0] == '[':
        return l, None;

    # find start of comment and remove the remaining characters
    l = l.split('#', 1)[0];
    
    # split the line by ':'
    keys = l.split('=')
    
    if len(keys) == 2:
        return f"{keys[0].strip()}",f"{keys[1].strip()}";
    else:
        logger.error("The configuration file syntax is not correct. Please check the format of the file.");
        return INVALID_KEY, INVALID_VALUE;

def main():
    logger.debug(f"Logging Level        :: {GBL_CURIO_LOG_LEVEL}")
    logger.info(f"Logging Level         :: {GBL_CURIO_LOG_LEVEL}")
    logger.warning(f"Logging Level      :: {GBL_CURIO_LOG_LEVEL}")
    logger.error(f"Logging Level        :: {GBL_CURIO_LOG_LEVEL}")
    logger.critical(f"Logging Level     :: {GBL_CURIO_LOG_LEVEL}")

    if len(sys.argv) == 1:
        profile = 'default'
        api_conf = parse_conf(profile)
    else:
        logger.debug(f"Parameter is provided: {sys.argv[1]}")
        profile = sys.argv[1]
        api_conf = parse_conf(profile)
    logger.debug(api_conf)
    return api_conf

# for the execution of this script only
# If parameter is specified, the first one will be considered as target profile
# while remaining is dismissed
# Example: python3 curio_config.py wasabi
# For this case, "wasabi" is used to specify the target profile
if __name__ == "__main__":
    main()
