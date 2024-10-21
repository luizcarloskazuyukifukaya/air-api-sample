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
# Harvest API in Wasabi AiR
# https://docs.wasabi.com/docs/items-api
# -----------------------------------------------


#############################################################################
# Getting All Metadata
# -----------------------------------------
# To get all metadata of an item by its ID, make the following request:
# =========================================
# *******************
#  Parameters
# *******************
# Input parameter
# id: item id
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
#   result = curio_get_all_metadata(item_id)
#
#############################################################################
def curio_get_all_metadata(item_id):

    # GET /api/data/items/{id}
    api_method = "GET"
    api_url = "/api/data/items/{}".format(item_id)

    response = {}

    logger.debug(f" Input parameter : {item_id}")

    response = curio_get_data(url=api_url)

    logger.debug(f"post_data({api_url}) called")

    return response

#############################################################################
# Getting the metadata.json File for an Item
# -----------------------------------------
# Getting the metadata.json File for an Item
# =========================================
# *******************
#  Parameters
# *******************
# Input parameter
# id: item id
# *******************
# Return value
# The response is a JSON document containing the same data as the metadata.json file.
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
#   result = curio_get_metadata_json(item_id)
#
#############################################################################
def curio_get_metadata_json(item_id):

    # GET /files/{item_id}/metadata2.json
    api_method = "GET"
    api_url = "/files/{}/metadata2.json".format(item_id)

    response = {}

    logger.debug(f" Input parameter : {item_id}")

    response = curio_get_data(url=api_url)

    logger.debug(f"post_data({api_url}) called")

    return response

#############################################################################
# Getting audio for an Item
# -----------------------------------------
# Getting audio for an Item
# =========================================
# *******************
#  Parameters
# *******************
# Input parameter
# id: item id
# *******************
# Return value
# The response is a audio timeline
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
#   result = curio_get_audio(item_id)
#
#############################################################################
def curio_get_audio(item_id):

    # GET /api/data/v3/items/{id}/timeline/audio
    api_method = "GET"
    api_url = "/api/data/v3/items/{}/timeline/audio".format(item_id)

    response = {}

    logger.debug(f" Input parameter : {item_id}")

    response = curio_get_data(url=api_url)

    logger.debug(f"post_data({api_url}) called")

    return response

#############################################################################
# Getting logos for an Item
# -----------------------------------------
# Getting logos for an Item
# =========================================
# *******************
#  Parameters
# *******************
# Input parameter
# id: item id
# *******************
# Return value
# The response is a logos
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
#   result = curio_get_logos(item_id)
#
#############################################################################
def curio_get_logos(item_id):

    # GET /api/data/v3/items/{id}/timeline/logos
    api_method = "GET"
    api_url = "/api/data/v3/items/{}/timeline/logos".format(item_id)

    response = {}

    logger.debug(f" Input parameter : {item_id}")

    response = curio_get_data(url=api_url)

    logger.debug(f"post_data({api_url}) called")

    return response


# for the execution of this script only
def get_all_metadata(item_id):

    logger.debug(f"curio_get_all_metadata() ...")

    response = curio_get_all_metadata(item_id)

    logger.debug(f"curio_get_all_metadata() completed.")

    ## return value
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");  

def get_metadata_json(item_id):

    logger.debug(f"curio_get_metadata_json() ...")

    response = curio_get_metadata_json(item_id)

    logger.debug(f"curio_get_metadata_json() completed.")

    ## return value
    logger.debug(f"{response}")
    logger.debug(f"{type(response)}")


def get_audio(item_id):

    logger.debug(f"curio_get_audio() ...")

    response = curio_get_audio(item_id)

    logger.debug(f"curio_get_audio() completed.")

    ## return value
    logger.debug(f"{response}")
    logger.debug(f"{type(response)}")


def get_logos(item_id):

    logger.debug(f"curio_get_logos() ...")

    response = curio_get_logos(item_id)

    logger.debug(f"curio_get_logos() completed.")

    ## return value
    logger.debug(f"{response}")
    logger.debug(f"{type(response)}")


def main():
    #
    # item
    item_id = "ba2b16d645730d415480b466132fe766"  # UI: From "Tech Data"
    # get_all_metadata(item_id)   # per item
    # get_metadata_json(item_id)  # metadata.json file
    # get_audio(item_id)  # audio timeline
    get_logos(item_id)  # logos timeline

if __name__ == "__main__":
    main()
