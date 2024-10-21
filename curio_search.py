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
# Search API in Wasabi AiR
# https://docs.wasabi.com/docs/search-api
# -----------------------------------------------


#############################################################################
# Search the metadata in Wasabi AiR
# -----------------------------------------
# Search contents based on the metadata
# =========================================
# *******************
#  Parameters
# *******************
# Input parameter
# NONE
# dict
# {
#   "query": "",                             # string    (MANDATORY: search query)
# }
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
#   searchQuery = {
#       "query": "ship",
#   }
#   result = search_query(**searchQuery)
#
#############################################################################
def curio_search(q):

    # POST /api/data/search
    api_method = "POST"
    api_url = "/api/data/search"

    response = {}

    query = {
        "query": "",  # string    (MANDATORY: search query)
        "page": 0,
        "limit": 25,
        "hit_counts": {},
    }
    
    if "query" in q:
        query["query"] = q["query"]
    else:
        # Missing mandatory parameters
        return response

    logger.debug(f" Input parameter : {query}")

    response = curio_post_data(url=api_url, body=query)

    logger.debug(f"post_data({api_url}) called")

    return response


# for the execution of this script only
def main():
    # search query
    param = {
        "query": "wasabi log",  # string    (MANDATORY: search query)
        "page": 0,
        "limit": 25,
        "hit_counts": {},
    }

    logger.debug(f"Calling curio_search() ...")

    response = curio_search(param)

    logger.debug(f"curio_search() completed.")  

    ## return value
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");  

if __name__ == "__main__":
    main()
