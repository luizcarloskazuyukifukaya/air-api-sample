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
# Listing All Extractor Profiles
# https://docs.wasabi.com/docs/duplicates-api
# -----------------------------------------------

#############################################################################
# Listing All Extractor Profiles
# -----------------------------------------
# Listing All Extractor Profiles
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
# 	"profiles": [
# 		{
# 			"id": "default",
# 			"name": "default",
# 			"description": "default profile"
# 		},
# 		{
# 			"id": "5f34150bbcf4bbc4903a5546470bf4b3",
# 			"name": "JRG Extractor Profile",
# 			"description": "This profile will be for compliance analyzation"
# 		},
# 		{
# 			"id": "5f3fb8f46d91b2bdbb2249fd8b817ebb",
# 			"name": "New Extractor Profile",
# 			"description": "Profile for test container"
# 		}
# 	]
# }
# FAIL
# {} # NULL (dictionary)
#
#############################################################################
def curio_list_extractors():

    # GET /api/data/h2/extractor-profiles
    api_method = "GET"
    api_url = "/api/data/h2/extractor-profiles"

    response = {}

    logger.debug(f" Input parameter : NONE")

    response = curio_get_data(url=api_url)

    logger.debug(f"get_data({api_url}) called")

    return response


#############################################################################
# Listing All Enabled Extractors for a Profile
# -----------------------------------------
# Listing All Enabled Extractors for a Profile
# =========================================
# *******************
#  Parameters
# *******************
# Input parameter
# id: Profile id
# *******************
#  Return value
# This call returns a list of all currently enabled extractors within the requested extractor profile as well as the individual extractor id(s).
# *******************
# SUCCESS
# TODO
# FAIL
# {} # NULL (dictionary)
#
#############################################################################
def curio_list_extractors_for_profile(id):

    # GET /api/data/h2/extractor-profiles/{id}
    api_method = "GET"
    api_url = "/api/data/h2/extractor-profiles/{}".format(id)

    response = {}

    logger.debug(f" Input parameter : {id}")

    response = curio_get_data(url=api_url)

    logger.debug(f"get_data({api_url}) called")

    return response


# for the execution of this script only
def list_extractors():

    logger.debug(f"Calling curio_list_extractors ...")

    response = curio_list_extractors()

    logger.debug(f"curio_list_extractors completed.")  

    ## return value
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");  


def list_extractors_for_profile():
    # Retrieve the profile id (first one) from response of list_extractors()
    id = ""
    r = curio_list_extractors()
    if len(r):
        # id = r["profiles"][0]["id"] # [0] is always "default"
        id = r["profiles"][1]["id"]  # other than the "default", if exists

        logger.debug(f"Calling curio_list_extractors_for_profile ...")

        response = curio_list_extractors_for_profile(id)

        logger.debug(f"curio_list_extractors_for_profile completed.")

        ## return value
        logger.debug(f"{response}")
        logger.debug(f"{type(response)}")

def main():
    list_extractors()
    list_extractors_for_profile()

if __name__ == "__main__":
    main()
