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
# Getting Distinct Item Types
# https://docs.wasabi.com/docs/items-api
# -----------------------------------------------

#############################################################################
# Getting Distinct Item Types
# -----------------------------------------
# Getting Distinct Item Types
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
#     "types": [
#         "audio",
#         "image/raster",
#         "video"
#     ]
# }
# FAIL
# {} # NULL (dictionary)
#
#############################################################################
def curio_list_item_types():

    # GET /api/data/v3/items/types
    api_method = "GET"
    api_url = "/api/data/v3/items/types"

    response = {}

    logger.debug(f" Input parameter : NONE")

    response = curio_get_data(url=api_url)

    logger.debug(f"get_data({api_url}) called")

    return response


# for the execution of this script only
def main():
    
    logger.debug(f"Calling curio_list_item_types ...")

    response = curio_list_item_types()

    logger.debug(f"curio_list_item_types completed.")  

    ## return value 
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");  

if __name__ == "__main__":
    main()
