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
# Listing All Locations Kinds
# # https://docs.wasabi.com/docs/location-kinds-api
# -----------------------------------------------

#############################################################################
# Getting a List of Supported Location Kinds
# -----------------------------------------
# Getting a List of Supported Location Kinds
# =========================================
# *******************
#  Parameters
# *******************
# Input parameter
# NONE
# *******************
#  Return value
# *******************
# SUCCESS
# {
#     "location_kinds": [
#         {
#             "id": "wasabi",
#             "name": "Wasabi",
#             "description": "Wasabi",
#             "configuration": [
#                 {
#                     "field": "access_key_id",
#                     "name": "Access Key ID",
#                     "type": "text",
#                     "placeholder": "Access Key ID",
#                     "required": True,
#                     "is_secret": False,
#                 },
#                 {
#                     "field": "secret_key",
#                     "name": "Secret Key",
#                     "type": "text",
#                     "placeholder": "Secret Key",
#                     "required": True,
#                     "is_secret": True,
#                 },
#                 {
#                     "field": "region",
#                     "name": "Region",
#                     "type": "text",
#                     "placeholder": "Wasabi Region",
#                     "required": True,
#                     "is_secret": False,
#                 },
#             ],
#             "editable": True,
#         }
#     ]
# }
# FAIL
# {} # NULL (dictionary)
#
#############################################################################
def curio_list_location_kinds():

    # GET /api/data/v3/location-kinds
    api_method = "GET"
    api_url = "/api/data/v3/location-kinds"

    response = {}

    logger.debug(f" Input parameter : NONE")

    response = curio_get_data(url=api_url)

    logger.debug(f"get_data({api_url}) called")

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

    logger.debug(f"Calling curio_list_location_kinds() ...")

    response = curio_list_location_kinds()

    logger.debug(f"curio_list_location_kinds() completed.")

    ## return value
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");  

if __name__ == "__main__":
    main()
