# ======================================
# Python Sample for Wasabi AiR
# No guaranty from Wasabi Inc.
# ======================================

from curio_tools import curio_rest_request, curio_set_profile
from curio_tools import (
    curio_get_data,
    curio_post_data,
    curio_put_data,
    curio_patch_data,
    curio_delete_data,
)

import requests
import json

import logging

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
logger.setLevel(10)
level = logger.level
logger.debug(f"Current Logging Level is {level}")

## Wasabi AiR specific URL
# -----------------------------------------------
# Create the API Key for Wasabi AiR API access
# https://docs.wasabi.com/docs/api-keys
# -----------------------------------------------

#############################################################################
# Create the API Key for Wasabi AiR API access
# -----------------------------------------
# Create the API Key for Wasabi AiR API access
# IMPORTANT: 500 is returned if the key name already exist.
# =========================================
# *******************
#  Parameters
# *******************
# Input parameter
# name : Name of the key to be created
# *******************
#  Return value
# *******************
# SUCCESS
# {
# TODO
#   "results": []
# }
# FAIL
# {} # NULL (dictionary)
#
# =========================================
# Example:
# TODO
#############################################################################
def curio_create_key(name):

    # POST /api/data/search
    api_method = "POST"
    api_url = "/api/data/api-keys"

    response = {}

    query = {
        "name": "",  # string    (MANDATORY: search query)
    }

    if len(name) == 0:
        name = "New API Key"    
    query["name"] = name

    logger.debug(f" Input parameter : {name}")

    response = curio_post_data(url=api_url, body=query)

    logger.debug(f"post_data({api_url}) called")

    return response


# for the execution of this script only
def main():
    # Switch profile here otherwise "default" is used
    # curio_set_profile("hhashimoto")
    # curio_set_profile("tokyo")
    # curio_set_profile("wasabi")

    logger.debug(f"Calling curio_create_key() ...")

    response = curio_create_key("Backup API Key (NEW)")

    logger.debug(f"curio_create_key() completed.")  

    ## return value
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");  

if __name__ == "__main__":
    main()
