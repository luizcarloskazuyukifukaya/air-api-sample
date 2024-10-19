# ======================================
# Python Sample for Wasabi AiR
# No guaranty from Wasabi Inc.
# ======================================


# ************************
# WORKING IN PROGRESS
# ************************


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
# Getting faces - non-deleted faces
# https://docs.wasabi.com/docs/faces-api
# -----------------------------------------------

#############################################################################
# Getting faces - non-deleted faces
# -----------------------------------------
# If not provided, the default size for limit is 5000 responses.
# =========================================
# *******************
#  Parameters
# *******************
# Input parameter
# limit: limit size (MAX: 5000)
# *******************
#  Return value
# *******************
# SUCCESS
# # FAIL
# {} # NULL (dictionary)
#
#############################################################################
def curio_get_non_deleted_faces(limit):

    #GET /api/data/v3/faces?limit=10
    api_method = "GET"
    api_url = "/api/data/v3/faces?limit="
    
    if isinstance(limit, int):
        if limit > 5000:
            limit = 5000
        elif limit < 0:
            limit = 5000
    else:
        limit = 5000
    api_url_with_param = api_url.format(str(limit))
    
    response = {}
    
    logger.debug(f" URL : {api_url_with_param}")
    logger.debug(f" Input parameter : {limit}")

    response = curio_get_data(url=api_url_with_param)

    logger.debug(f"get_data({api_url_with_param}) called")

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
    
    logger.debug(f"Calling  curio_get_non_deleted_faces() ...")

    response =  curio_get_non_deleted_faces(500)

    logger.debug(f" ccurio_get_non_deleted_faces() completed.")  

    ## return value 
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");  

if __name__ == "__main__":
    main()
