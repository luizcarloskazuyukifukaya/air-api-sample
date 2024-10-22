# ======================================
# Python Sample for Wasabi AiR
# No guaranty from Wasabi Inc.
# ======================================

from curio_tools import (
    curio_set_profile,
    curio_rest_request,
    curio_get_data,
    curio_post_data,
    curio_put_data,
    curio_patch_data,
    curio_delete_data,
    curio_options_data,
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
# Saved Searches API in Wasabi AiR
# https://docs.wasabi.com/docs/saved-searches-api
# -----------------------------------------------

#############################################################################
# Getting Saved Searches
# -----------------------------------------
# Getting Saved Searches
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
#     "saved_searches": [
#         {
#             "saved_search_id": "5966c04e9480ef4d8dff09331af33755",
#             "name": "Celebrities",
#             "params": "query=Brad Pitt",
#             "created_at": "2017-07-13T00:35:26.683471Z",
#         },
#         {
#             "saved_search_id": "5966c06e5179ce3d6f384417722dea1a",
#             "name": "Artwork",
#             "params": "query=Britto",
#             "created_at": "2017-07-13T00:35:58.368016Z",
#         },
#     ]
# }
# FAIL
# {} # NULL (dictionary)
#
#############################################################################
def curio_list_saved_searches():

    # GET /api/data/saved-searches
    api_method = "GET"
    api_url = "/api/data/saved-searches"

    response = {}

    logger.debug(f" Input parameter : NONE")

    response = curio_get_data(url=api_url)

    logger.debug(f"get_data({api_url}) called")

    return response

    # for the execution of this script only
def list_saved_search():
    logger.debug(f"Calling curio_list_saved_searches ...")

    response = curio_list_saved_searches()

    logger.debug(f"curio_list_saved_searches completed.")  

    ## return value
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");  


def main():
    # Switch profile here otherwise "default" is used
    profile = "kfukaya"
    logger.debug(f"Setting profile to {profile} ...")
    curio_set_profile(profile)

    list_saved_search()

if __name__ == "__main__":
    main()
