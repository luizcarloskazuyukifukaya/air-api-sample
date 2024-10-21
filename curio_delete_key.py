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
# Create the API Key for Wasabi AiR API access
# https://docs.wasabi.com/docs/api-keys
# -----------------------------------------------

#############################################################################
# Permanently delete a key
# -----------------------------------------
# When you are no longer using an API key, it is recommended that you revoke it:
# DELETE /api/data/api-keys/{key-id}
# key-id - (string) The API Key ID (not the JWT itself)
# -----------------------------------------
# Create the API Key for Wasabi AiR API access
# IMPORTANT: Future requests using that key will not work.
# =========================================
# *******************
#  Parameters
# *******************
# Input parameter
# id : Key Id
# *******************
#  Return value
# *******************
# SUCCESS
# {
#   "ok": True
# }
# FAIL
# {} # NULL (dictionary)
#
# =========================================
# Example:
# key_id = "c7e7f6ff2e5c236dcc3a784f524ca5c536a56385bddec19bfeef5cd951d1522b"
# response = curio_delete_key(key_id)
#############################################################################
def curio_delete_key(key_id):

    # DELETE /api/data/api-keys/{key-id}
    api_method = "DELETE"
    api_url = "/api/data/api-keys/{}".format(key_id)

    response = {}

    logger.debug(f" Input parameter : {key_id}")

    response = curio_delete_data(url=api_url)

    logger.debug(f"curio_delete_data({api_url}) called")

    return response


# for the execution of this script only
def main():
    # Switch profile here otherwise "default" is used
    # curio_set_profile("hhashimoto")
    # curio_set_profile("tokyo")
    # curio_set_profile("wasabi")
    # curio_set_profile("kfukaya")

    key_id = "c7e7f6ff2e5c236dcc3a784f524ca5c536a56385bddec19bfeef5cd951d1522b"
    logger.debug(f"Calling curio_delete_key() ...")

    response = curio_delete_key(key_id)

    logger.debug(f"curio_delete_key() completed.")  

    ## return value
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");  

if __name__ == "__main__":
    main()
