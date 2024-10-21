# ======================================
# Python Sample for Wasabi AiR
# No guaranty from Wasabi Inc.
# ======================================

# *********************************
# TODO
# NOT SUCCESSUFLY EXECUTED THE PASSWORD UPDATE
# FAILED TO UPDATE ITS OWN PASSWORD
# FAILED TO UPDATE WITH ADMIN USER (admin@wasabi.com, Root User neither)

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
# Updating a User Password
# https://docs.wasabi.com/docs/users-and-groups-api
# -----------------------------------------------

#############################################################################
# Updating a User Password
# -----------------------------------------
# Updating a user own password
# [IMPORTANT]
# This API can be used only to change the password for the user who is currently logged in.
# Administrators cannot use this API to change other users’ passwords.
# =========================================
# *******************
#  Parameters
# *******************
# Input parameter
# id: User ID
# password: New user password
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
#   result = curio_update_password(id, password)
#
#############################################################################
def curio_update_password(id, password):

    # PUT /api/data/users/{id}/password
    api_method = "PUT"
    api_url = "/api/data/users/{}/password".format(id)

    response = {}
    if len(password) == 0:
        # Missing mandatory parameters
        return response

    payload = {
        "password": password,  # string    (MANDATORY: search query)
    }
    
    logger.debug(f" Input parameter : {id} , {password}")
    logger.debug(f" URL : {api_url}")
    logger.debug(f" body : {payload}")

    response = curio_put_data(url=api_url, body=payload)

    logger.debug(f"post_data({api_url}) called")

    return response


# for the execution of this script only
def main():
    # User ID
    i = "67126201b10c9abfb41d7c1b8c764d12" #kfukaya@wasabi.com
    # i = "67130cd75864ed1a8832cf61b48b0d38" #hhashimoto@wasabi.com
    # New password
    p = "WasabiJapan"

    logger.debug(f"Calling curio_update_password() ...")

    response = curio_update_password(i, p)

    logger.debug(f"curio_update_password() completed.")  

    ## return value
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");  

if __name__ == "__main__":
    main()
