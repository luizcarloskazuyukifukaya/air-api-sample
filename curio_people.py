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
# People API in Wasabi AiR
# https://docs.wasabi.com/docs/people-api
# -----------------------------------------------

#############################################################################
# Listing People
# -----------------------------------------
# Listing People
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
#     "next_page_token": "",
#     "people": [
#         {
#             "person_id": "39d2a59c-2a79-4dec-8e01-3c862d846820",
#             "name": "unknown",
#             "is_known": false,
#             "face_img_path": "d8402f6d8949e19010db80aebd45be2c/face/9a325483-4ae5-45c1-b2ec-bbb327a1f1fd.jpg",
#             "face_img_width": 292,
#             "face_img_height": 379,
#             "face_img_small_path": "",
#             "face_img_small_width": 0,
#             "face_img_small_height": 0,
#             "num_faces": 1,
#             "created_at": "2018-12-19T15:22:10.788526Z",
#             "updated_at": "2018-12-19T15:22:10.788526Z",
#         },
#         ...,
#     ],
# }
# FAIL
# {} # NULL (dictionary)
#
#############################################################################
def curio_list_people():

    # GET /api/data/v3/people
    api_method = "GET"
    api_url = "/api/data/v3/people"

    response = {}

    logger.debug(f" Input parameter : NONE")

    response = curio_get_data(url=api_url)

    logger.debug(f"get_data({api_url}) called")

    return response


# for the execution of this script only
def list_people():

    logger.debug(f"Calling curio_list_people ...")

    response = curio_list_people()

    logger.debug(f"curio_list_people completed.")  

    ## return value
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");  


#############################################################################
# Getting Total People and Faces Counts
# -----------------------------------------
# Getting Total People and Faces Counts
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
# 	"num_known": 1,
# 	"num_unknown": 18
# }
# FAIL
# {} # NULL (dictionary)
#
#############################################################################
def curio_get_people_stats():

    # GET /api/data/v3/people/stats
    api_method = "GET"
    api_url = "/api/data/v3/people/stats"

    response = {}

    logger.debug(f" Input parameter : NONE")

    response = curio_get_data(url=api_url)

    logger.debug(f"get_data({api_url}) called")

    return response


# for the execution of this script only
def get_people_stats():

    logger.debug(f"Calling curio_get_people_stats ...")

    response = curio_get_people_stats()

    logger.debug(f"curio_get_people_stats completed.")

    ## return value
    logger.debug(f"{response}")
    logger.debug(f"{type(response)}")


def main():
    list_people()
    get_people_stats()


if __name__ == "__main__":
    main()
