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
# Listing All Keys for a User
# https://docs.wasabi.com/docs/api-keys
# -----------------------------------------------

#############################################################################
# Listing All Keys for a User
# -----------------------------------------
# List for all key for a user what is associated with the access key
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
#     "api-keys": [
#         {
#             "id": "abc123",
#             "jwt": "APIKEY",
#             "active": true,
#             "user_id": "591481bf1940f20c341b9386a9a192f4",
#             "created_at": "2017-05-31T20:56:04.002433Z",
#             "updated_at": "2017-05-31T20:56:04.002433Z"
#         },
#         {
#             "id": "abc124",
#             "jwt": "APIKEY",
#             "active": true,
#             "user_id": "591481bf1940f20c341b9386a9a192f4",
#             "created_at": "2017-05-31T20:56:04.002433Z",
#             "updated_at": "2017-05-31T20:56:04.002433Z"
#         },
#         {
#             "id": "abc125",
#             "jwt": "APIKEY",
#             "active": false,
#             "user_id": "591481bf1940f20c341b9386a9a192f4",
#             "created_at": "2017-05-31T20:56:04.002433Z",
#             "updated_at": "2017-05-31T20:56:04.002433Z"
#         }
#     ]
# }
# FAIL
# {} # NULL (dictionary)
#
#############################################################################
def curio_list_keys():

    #GET /api/data/api-keys
    api_method = "GET"
    api_url = "/api/data/api-keys"

    response = {}

    logger.debug(f" Input parameter : NONE")

    response = curio_get_data(url=api_url)

    logger.debug(f"get_data({api_url}) called")

    return response


# for the execution of this script only
def main():
    
    logger.debug(f"Calling curio_list_keys() ...")

    response = curio_list_keys()

    logger.debug(f"curio_list_keys() completed.")  

    ## return value 
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");  

if __name__ == "__main__":
    main()
