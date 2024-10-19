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
# Creating a User
# https://docs.wasabi.com/docs/users-and-groups-api
# -----------------------------------------------
#############################################################################
# Partially Updating a User
# -----------------------------------------
# Update user profile
# For password, user can change its own user's password
# =========================================
# *******************
#  Parameters
# *******************
# Input parameter
# New User Information
# *** IMPORTANT ***
# "password" can not be updated - it will be ignored! No Changes.
# dict
# {
#   'id': '67130cd75864ed1a8832cf61b48b0d38', # (MANDATORY: user id)
#   "email": "",    # string    (OPTIONAL: User email address)
#   "first_name": "",    # string    (OPTIONAL: User First name) [""]
#   "last_name": "",    # string    (OPTIONAL: User Last name) [""]
#   "role_id": "",    # string    (OPTIONAL: "default-user" | "root" )
# }
# *******************
#  Return value
# *******************
# SUCCESS
# {
#   'id': '67130cd75864ed1a8832cf61b48b0d38',
#   'email': 'hhashimoto@wasabi.com',
#   'first_name': 'Hiroshi',
#   'last_name': 'Hashimoto',
#   'enabled': True,
#   'created_at': '2024-10-19T01: 35: 19.153604Z',
#   'updated_at': '2024-10-19T01: 35: 19.153604Z',
#   'groups':
#     {'count': 0,
#       'shortlist': None
#     },
#     'avatar': '',
#     'role_id': 'default-user',
#     'company_uid': ''
# }
# FAIL
# {} # NULL (dictionary)
#
# =========================================
# Example:
# updatedUserInfo =
# {
# "id": "67130cd75864ed1a8832cf61b48b0d38" # (MANDATORY: user id)
# "email": "new@email.com",    # string    (OPTIONAL: New User Email Address)
# "first_name": "Kazuyuki",    # string    (OPTIONAL: User First name)
# "last_name": "FUKAYA",    # string    (OPTIONAL: User Last name)
# "role_id": "",    # string    (OPTIONAL: "default-user" | "root" )
# }
# result = curio_update_user(updatedUserInfo)
#
#############################################################################
def curio_update_user(info):
    user_id = 0
    response = {}
    userInfo = {}

    # Check mandatory parameter first
    if "id" in info:
        user_id = info["id"]
    else:
        # Missing mandatory parameters
        return response

    # PATCH /api/data/users/{id}
    api_method = "PATCH"
    api_url = f"/api/data/users/{user_id}"
    
    # Other parameters (just add all that have been provided)
    keyList = list(info.keys())
    keyList.remove('id') # 'id' is should not be included
    for key in keyList:
        logger.debug(f"{key} is passed as a parameter")
        userInfo[key] = info[key]
        
    logger.debug(f" Input parameter : {info}")
    logger.debug(f" User Profile : {userInfo}")

    response = curio_patch_data(url=api_url, body=userInfo)

    logger.debug(f"patch_data({api_url}) called")

    return response


# # Example usage
# @rest_request(method='GET')
# def curio_get_data(url):
#     pass

# @rest_request(method='POST')
# def curio_post_data(url, body):
#     pass

# # Using the decorated functions
# get_result = get_data(url='/api/data/user-keys')
# if curio_get_result:
#     print("GET Result:", get_result)

# post_result = post_data(url='/api/data/search', body={'key': 'value'})
# if curio_post_result:
#     print("POST Result:", post_result)


# for the execution of this script only
def main():
    # create user
    param = {
        "id": "67130cd75864ed1a8832cf61b48b0d38",  # string (MANDATORY: user id)
        "email": "hhashimoto@wasabi.com",  # string (YES YOU CAN CHANGE THE EMAIL)
        "first_name": "Hiroshi",  # string    (OPTIONAL: User First name) [""]
        "last_name": "HASHIMOTO",  # string    (OPTIONAL: User Last name) [""]
        ### IMPORTANT (PASSWORD CAN NOT BE UPDATE)
        # "password": "Wasabi123!",    # string    (OPTIONAL: User Password) [user's email] (NOT POSSIBLE)
        "role_id": "root",  # string    (OPTIONAL: "default-user" | "root" )
    }

    logger.debug(f"Calling curio_update_user() ...")

    response = curio_update_user(param)

    logger.debug(f"curio_update_user() completed.")  

    ## return value
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");  

if __name__ == "__main__":
    main()
