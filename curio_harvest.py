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
# Harvest API in Wasabi AiR
# https://docs.wasabi.com/docs/harvest-api
# -----------------------------------------------


#############################################################################
# Harvesting a Single Item
# -----------------------------------------
# To initiate a harvest of a single item, make the following request:
# =========================================
# *******************
#  Parameters
# *******************
# Input parameter
# dict
# {
#     "location_id": "{location_id}",
#     "item_id": "{item_id}",
#     "extractors": ["{extractor1}", "{extractor2}"],
#     "profile_id": "{profile_id}",
#     "override_extractors": {bool},
#     "new_extractors_only": {bool},
#     "force": {bool},
#     "priority": {priority},
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
#   targetItem = {
#     "location_id": "{location_id}",
#     "item_id": "{item_id}",
#     "extractors": ["{extractor1}", "{extractor2}"],
#     "profile_id": "{profile_id}",
#     "override_extractors": true,
#     "new_extractors_only": false,
#     "force": true,
#     "priority": 1, # 1: highest priority -  10: lowest
#   }
#   result = curio_harvest_an_item(targetItem)
#
#############################################################################
def curio_harvest_an_item(itemInfo):

    # POST /api/control/harvest
    api_method = "POST"
    api_url = "/api/control/harvest"

    response = {}
    mandatoryKeyList = [
      "location_id",
      "item_id",
      "extractors",
      "profile_id"
    ]

    # check if all mandatory key do exist in the given itemInfo
    if not all(item in itemInfo for item in mandatoryKeyList):
        # Missing mandatory parameters
        return response
    # If optional key exist, let us use it as input, if not use the default defined in this method
    if not "override_extractors" in itemInfo:
        itemInfo["override_extractors"] = True

    if not "new_extractors_only" in itemInfo:
        itemInfo["new_extractors_only"] = False

    if not "force" in itemInfo:
        itemInfo["force"] = True

    if not "priority" in itemInfo:
        itemInfo["priority"] = 1

    logger.debug(f" Input parameter : {itemInfo}")

    response = curio_post_data(url=api_url, body=itemInfo)

    logger.debug(f"post_data({api_url}) called")

    return response


#############################################################################
# Harvesting a Single Item
# -----------------------------------------
# To initiate a harvest of a single item, make the following request:
# =========================================
# *******************
#  Parameters
# *******************
# Input parameter
# dict
# {
#     "location_id": "{location_id}",
#     "container_id": "{container_id}",
#     "extractors": ["{extractor1}", "{extractor2}"],
#     "profile_id": "{profile_id}",
#     "override_extractors": {bool},
#     "new_extractors_only": {bool},
#     "force": {bool},
#     "ignore_recently_walked": {bool},
#     "priority": {priority},
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
#   targetItem = {
#      "location_id": "{location_id}",
#      "container_id": "{container_id}",
#      "extractors": ["{extractor1}", "{extractor2}"],
#      "profile_id": "{profile_id}",
#
#     "override_extractors": true,
#     "new_extractors_only": false,
#     "force": true,
#     "ignore_recently_walked": true,
#     "priority": 1, # 1: highest priority -  10: lowest
#   }
#   result = curio_harvest_an_item(targetItem)
#
#############################################################################
def curio_harvest_an_container(containerInfo):

    # POST /api/control/harvest
    api_method = "POST"
    api_url = "/api/control/harvest"

    response = {}
    mandatoryKeyList = ["location_id", "container_id", "extractors", "profile_id"]

    # check if all mandatory key do exist in the given itemInfo
    if not all(item in containerInfo for item in mandatoryKeyList):
        # Missing mandatory parameters
        return response
    # If optional key exist, let us use it as input, if not use the default defined in this method
    if not "override_extractors" in containerInfo:
        containerInfo["override_extractors"] = True

    if not "new_extractors_only" in containerInfo:
        containerInfo["new_extractors_only"] = False

    if not "force" in containerInfo:
        containerInfo["force"] = True

    if not "ignore_recently_walked" in containerInfo:
        containerInfo["ignore_recently_walked"] = True

    if not "priority" in containerInfo:
        containerInfo["priority"] = 1

    logger.debug(f" Input parameter : {containerInfo}")

    response = curio_post_data(url=api_url, body=containerInfo)

    logger.debug(f"post_data({api_url}) called")

    return response


# ALL Wasabi AiR Extrators
ALL_EXTRACTOR_LIST = [
    "archive",
    "audioinfo",
    "audio_previews",
    "audiopeak",
    "black_scenes",
    "caption_files",
    "captionsv2",
    "slates",
    "gm_color_bars",
    "credits",
    "csv",
    "dbf",
    "gm_digital_slates",
    "document_pages",
    "dpx",
    "drm",
    "email",
    "captions",
    "exiv2",
    "fdx",
    "geocoding",
    "gm_audio_classification",
    "gm_faces",
    "hashes",
    "html",
    "json",
    "gmlanguage",
    "gmlogos",
    "m2ts",
    "mediainfo",
    "mime_type",
    "gmocr",
    "officex",
    "pdf",
    "gm_silence",
    "gms2t",
    "gmsports",
    "gm_start_end",
    "stow",
    "gm_texted",
    "gm_textless",
    "thumbnailer",
    "tokens",
    "video_main_frames",
    "video_previews",
    "volumedetect",
    "weather",
    "xml",
]
# for the execution of this script only
def harvest_an_item():
    #
    # harvest an item
    param = {
        "location_id": "67131e559061f7a97671e535af453757",
        "item_id": "ba2b16d645730d415480b466132fe766",  # UI: From "Tech Data"
        "extractors": ALL_EXTRACTOR_LIST,
        "profile_id": "default",  # Use default
        # "override_extractors": true,
        # "new_extractors_only": false,
        # "force": true,
        # "priority": 1, # 1: highest priority -  10: lowest
    }

    logger.debug(f"curio_harvest_an_item() ...")

    response = curio_harvest_an_item(param)

    logger.debug(f"curio_harvest_an_item() completed.")

    ## return value
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");  


def harvest_an_container():
    # harvest an container
    param = {
        "location_id": "67131e559061f7a97671e535af453757", # Connection (id)
        "container_id": "movclips-japanese",  # Bucket name
        "extractors": ALL_EXTRACTOR_LIST,
        "profile_id": "default",  # Use default
        # "override_extractors": true,
        # "new_extractors_only": false,
        # "force": true,
        # "ignore_recently_walked": true,
        # "priority": 1, # 1: highest priority -  10: lowest
    }

    logger.debug(f"curio_harvest_an_container() ...")

    response = curio_harvest_an_container(param)

    logger.debug(f"curio_harvest_an_container() completed.")

    ## return value
    logger.debug(f"{response}")
    logger.debug(f"{type(response)}")


def main():
    harvest_an_item()   # per item
    # harvest_an_container()    # per bucket

if __name__ == "__main__":
    main()
