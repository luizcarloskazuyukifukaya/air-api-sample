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
# Logo Training API in Wasabi AiR
# N/A
# INTERNAL ONLY
# CURIO PDF /api/api/api.wasabi.com/020__API_Reference/Logo_Training_API.html
# -----------------------------------------------

#############################################################################
# Logo Training API
# -----------------------------------------
# Logo training allows you to train LogoGrab’s model to identify specific brand logos.
# Verify user can train logos
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
#    "can_train_logos": true
# }
# FAIL
# {} # NULL (dictionary)
#
# =========================================
# Example:
#   result = curio_check_log_training()
#
#############################################################################
def curio_check_logo_training():

    # OPTIONS /api/data/train/logos
    api_method = "OPTIONS"
    api_url = "/api/data/train/logos"

    response = {}

    logger.debug(f" Input parameter : NONE")

    response = curio_options_data(url=api_url)

    logger.debug(f"curio_options_data({api_url}) called")

    return response

def check_logo():
    response = curio_check_logo_training()
    logger.debug(f"{response}")
    logger.debug(f"{type(response)}")

# NOT SUPPORTED IN WASABI AIR (DEPRECATED FROM CURIO)
#############################################################################
# Logo Training API
# -----------------------------------------
# Get a list of logo training requests
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
# TODO
# {
#    "can_train_logos": true
# }
# FAIL
# {} # NULL (dictionary)
#
# =========================================
# Example:
#   result = curio_list_log_training()
#
#############################################################################
def curio_list_logo_training():

    # GET /api/data/train/logos
    api_method = "GET"
    api_url = "/api/data/train/logos"

    response = {}

    logger.debug(f" Input parameter : NONE")

    response = curio_get_data(url=api_url)

    logger.debug(f"curio_get_data({api_url}) called")

    return response


def list_logo_training():
    response = curio_list_logo_training()
    logger.debug(f"{response}")
    logger.debug(f"{type(response)}")

def main():
    # check logo training possibility
    curio_set_profile("usadmin")
    check_logo()
    # list of logo training requests
    list_logo_training()

if __name__ == "__main__":
    main()
