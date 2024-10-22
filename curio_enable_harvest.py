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
# N/A
# CURIO API DOC (PDF or HTML)
# Disable Live Harvesting
# -----------------------------------------------


#############################################################################
# Disable Live Harvesting
# -----------------------------------------
# Periodically, the Curio AI Platform will check the enabled Containers for changes, and if it detects any, will initiate a re-harvest of those items, ensuring the metadata is kept up-to-date.
# =========================================
# *******************
#  Parameters
# *******************
# Input parameter
# dict
# {
#     "enabled": True, # True to enable, False to disable
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
#   targetStatus = {
#     "enabled": False,
#   }
#   result = curio_enable_harvest(targetStatus)
#
#############################################################################
def curio_enable_harvest(status):
    # status: True: enabled | False: disabled
    # PUT /api/data/features/disabled_live_harvesting
    api_method = "PUT"
    api_url = "/api/data/features/disabled_live_harvesting"

    response = {}
    targetStatus = {
      "enabled": status,
    }

    logger.debug(f" Input parameter : {targetStatus}")

    response = curio_put_data(url=api_url, body=targetStatus)

    logger.debug(f"put_data({api_url}) called")

    return response


# for the execution of this script only
def enable_harvest():
    logger.debug(f"Enabling Live Harvesting...")
    logger.debug(f"curio_enable_harvest({True}) ...")

    response = curio_enable_harvest(True)

    logger.debug(f"curio_harvest_an_item() completed.")

    ## return value
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");  


def disable_harvest():
    logger.debug(f"Disabling Live Harvesting...")
    logger.debug(f"curio_enable_harvest({False}) ...")

    response = curio_enable_harvest(False)

    logger.debug(f"curio_enable_harvest() completed.")

    ## return value
    logger.debug(f"{response}")
    logger.debug(f"{type(response)}")


def main():
    enable_harvest()
    # disable_harvest()

if __name__ == "__main__":
    main()
