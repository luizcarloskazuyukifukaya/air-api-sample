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
# Summary API in Wasabi AiR
# https://docs.wasabi.com/docs/summary-api
# -----------------------------------------------

#############################################################################
# Getting Platform Data
# -----------------------------------------
# Getting Platform Data
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
#     "harvest_refresh_time": 21600,
#     "offering": {
#         "base_url": "",
#         "saas": False,
#         "saas_details": {"max_items": 2500, "plans": None},
#         "facial_recognition_enabled": True,
#         "experimental_extractors_enabled": False,
#         "license": {
#             "expiration": "2138-11-21T01:48:30.783897677Z",
#             "base_url": "",
#             "enforce_base_url_check": False,
#             "license_generated_at": "0001-01-01T00:00:00Z",
#             "license_generation_host": "",
#             "remote_usage_enabled": False,
#             "license_checks_enabled": False,
#         },
#         "loadnstore": {
#             "enabled": False,
#             "limit_bytes": 0,
#             "ignore_patterns": [
#                 ".ds_store",
#                 "thumbs.db",
#                 "__macosx",
#                 "desktop.ini",
#                 ".spotlight-v100",
#                 "._*",
#                 "~*.docx",
#                 "~*.pptx",
#                 "~*.xlsx",
#                 ".smbdelete*",
#                 "*.tmp",
#                 "*.plist",
#                 "*.IND",
#                 "*.mhl",
#                 "*.BNP",
#                 "*.aframe",
#                 "*.ale",
#                 "*.hprj",
#                 "*.INP",
#                 "*.INT",
#                 "*.BDM",
#                 "*.BIM",
#                 "*.bk",
#                 "*.conf",
#                 "*.in_progress",
#                 "*.lnk",
#                 "*.sav",
#                 "*.sh",
#                 "*.root",
#                 "*.aep",
#             ],
#         },
#         "aws_custom_labels": {"enabled": False, "project_import_enabled": False},
#     },
#     "password_length_minimum": 8,
#     "password_length_maximum": 72,
#     "google_maps_key": "",
#     "rollbar_write_key_frontend": "",
#     "segment_write_key": "",
# }
# FAIL
# {} # NULL (dictionary)
#
#############################################################################
def curio_get_platform_data():

    # GET /api/data/summary/platform
    api_method = "GET"
    api_url = "/api/data/summary/platform"

    response = {}

    logger.debug(f" Input parameter : NONE")

    response = curio_get_data(url=api_url)

    logger.debug(f"get_data({api_url}) called")

    return response

    # for the execution of this script only
def get_platform_data():
    logger.debug(f"Calling curio_get_platform_data ...")

    response = curio_get_platform_data()

    logger.debug(f"curio_get_platform_data completed.")  

    ## return value
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");  


#############################################################################
# Getting a Summary of Your Data
# -----------------------------------------
# Getting a Summary of Your Data
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
#     "total_files": 5690,
#     "deleted_files": 0,
#     "total_pages": 0,
#     "total_size": 708572608,
#     "video_runtime_seconds": 45.828,
#     "last_harvest": "2019-09-04T04:20:04.724949556Z",
# }
# FAIL
# {} # NULL (dictionary)
#
#############################################################################
def curio_get_your_data():

    # GET /api/data/summary/data
    api_method = "GET"
    api_url = "/api/data/summary/data"

    response = {}

    logger.debug(f" Input parameter : NONE")

    response = curio_get_data(url=api_url)

    logger.debug(f"get_data({api_url}) called")

    return response

    # for the execution of this script only


def get_your_data():
    logger.debug(f"Calling curio_get_your_data ...")

    response = curio_get_your_data()

    logger.debug(f"curio_get_your_data completed.")

    ## return value
    logger.debug(f"{response}")
    logger.debug(f"{type(response)}")


#############################################################################
# Item Summary
# -----------------------------------------
# Item Summary
# =========================================
# *******************
#  Parameters
# *******************
# Input parameter
# item_id: Id of the item to get summary
# *******************
#  Return value
# *******************
# SUCCESS
# {
#     "summary": {
#         "title": "CustomerHarassment/カスハラ3+.mp4",
#         "technical": {
#             "audio": {
#                 "channels": 2,
#                 "codec": "AAC",
#                 "duration_time": "00: 00: 43: 12",
#                 "bit_rate": 128000,
#                 "format": "AAC",
#                 "true_peak_dbfs": -10.1,
#             },
#             "video": {
#                 "resolution": "960 x 540",
#                 "aspect_ratio": "16: 9",
#                 "frame_rate": 29.97,
#                 "duration_time": "00: 00: 43.377",
#                 "chroma_subsampling": "4: 2: 0",
#                 "bit_rate": 4723563,
#                 "container": "Base Media / Version 2",
#             },
#             "size": "26.4 MB",
#             "file_type": "mp4",
#         },
#         "tags": [
#             {"appearances": 0.2727272727272727, "name": "glasses"},
#             {"appearances": 0.045454545454545456, "name": "people"},
#         ],
#     }
# }
# FAIL
# {} # NULL (dictionary)
#
#############################################################################
def curio_get_item_summary(item_id):

    # GET /api/data/v3/summary/items/{id}
    api_method = "GET"
    api_url = "/api/data/v3/summary/items/{}".format(item_id)

    response = {}

    logger.debug(f" Input parameter : {item_id}")

    response = curio_get_data(url=api_url)

    logger.debug(f"get_data({api_url}) called")

    return response

    # for the execution of this script only


def get_item_summary(id):
    logger.debug(f"Calling curio_get_item_summary ...")

    response = curio_get_item_summary(id)

    logger.debug(f"curio_get_item_summary completed.")

    ## return value
    logger.debug(f"{response}")
    logger.debug(f"{type(response)}")


def main():
    # Switch profile here otherwise "default" is used
    profile = "kfukaya"
    logger.debug(f"Setting profile to {profile} ...")
    curio_set_profile(profile)

    get_platform_data()

    # get summary of Your Data (user: set by the profile)
    get_your_data()

    # switch profile
    profile = "hhashimoto"
    logger.debug(f"Setting profile to {profile} ...")
    curio_set_profile(profile)
    get_your_data()

    # item
    item_id = "ba2b16d645730d415480b466132fe766"  # UI: From "Tech Data"
    get_item_summary(item_id)

if __name__ == "__main__":
    main()
