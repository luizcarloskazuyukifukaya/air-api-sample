# ======================================
# Python Sample for Wasabi AiR
# No guaranty from Wasabi Inc.
# ======================================

from curio_tools import curio_rest_request
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
        name = "kfukaya"    
    query["name"] = name

    logger.debug(f" Input parameter : {name}")

    response = curio_post_data(url=api_url, body=query)

    logger.debug(f"post_data({api_url}) called")

    return response


# # Example usage
# @rest_request(method='GET')
# def curio_get_data(url):
#     pass

# @rest_request(method='POST')
# def curio_post_data(url, body):
#     pass

# # Using the decorated functions
# get_result = get_data(url='/api/data/user-keys')
# if curio_get_result:
#     print("GET Result:", get_result)

# post_result = post_data(url='/api/data/search', body={'key': 'value'})
# if curio_post_result:
#     print("POST Result:", post_result)


# for the execution of this script only
def main():

    logger.debug(f"Calling curio_create_key() ...")

    response = curio_create_key("My New Key 2")

    logger.debug(f"curio_create_key() completed.")  

    ## return value
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");  

if __name__ == "__main__":
    main()
