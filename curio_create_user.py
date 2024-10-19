# ======================================
# Python Sample for Wasabi AiR
# No guaranty from Wasabi Inc.
# ======================================

from curio_tools import rest_request
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
# Creating a User
# -----------------------------------------
# Creating a User with the email address specified.
# Other profile information is optional.
# If not specified, the password is set to be the user's email address value.
# User role is default to "default-user", which is the normal user.
# =========================================
# *******************
#  Parameters
# *******************
# Input parameter
# New User Information
# dict
# {
#   "email": "",    # string    (MANDATORY: User email address)
#   "first_name": "",    # string    (OPTIONAL: User First name) [""]
#   "last_name": "",    # string    (OPTIONAL: User Last name) [""]
#   "password": "",    # string    (OPTIONAL: User Password) [user's email]
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
# newUserInfo =
    # {
    # "email": "kfukaya@wasabi.com",    # string    (MANDATORY: User email address)
    # "first_name": "Kazuyuki",    # string    (OPTIONAL: User First name) [""]
    # "last_name": "FUKAYA",    # string    (OPTIONAL: User Last name) [""]
    # "password": "",    # string    (OPTIONAL: User Password) [user's email]
    # "role_id": "",    # string    (OPTIONAL: "default-user" | "root" )
    # }
# result = curio_create_user(newUserInfo)
#
#############################################################################
def curio_create_user(info):

    # POST /api/data/users
    api_method = "POST"
    api_url = "/api/data/users"

    response = {}

    userInfo = {
        "email": "",    # string    (MANDATORY: User email address)
        "first_name": "",    # string    (OPTIONAL: User First name) [""]
        "last_name": "",    # string    (OPTIONAL: User Last name) [""]
        "password": "",    # string    (OPTIONAL: User Password) [user's email]
        "role_id": "default-user",    # string    (OPTIONAL: "default-user" | "root" )
    }
    
    if "email" in info:
        userInfo["email"] = info["email"]
    else:
        # Missing mandatory parameters
        return response
    
    # Other parameters
    keyList = list(info.keys())
    for key in keyList:
        logger.debug(f"{key} is passed as a parameter")
        if key in userInfo:
            # found matching parameter
            userInfo[key] = info[key]
        else:
            logger.info(f"Wrong parameter is given. Ignoring {key} ...")
    
    # Default setting for User password
    # If the password is not specified, we will default to user's email address
    if len(userInfo["password"]) == 0:
        userInfo["password"] = info["email"]
    
    logger.debug(f" Input parameter : {info}")
    logger.debug(f" User Profile : {userInfo}")

    response = curio_post_data(url=api_url, body=userInfo)

    logger.debug(f"post_data({api_url}) called")

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
    "email": "hhashimoto@wasabi.com",    # string    (MANDATORY: User email address)
    "first_name": "Hiroshi",    # string    (OPTIONAL: User First name) [""]
    "last_name": "Hashimoto",    # string    (OPTIONAL: User Last name) [""]
    # "password": "Wasabi123!",    # string    (OPTIONAL: User Password) [user's email]
    # "role_id": "root",    # string    (OPTIONAL: "default-user" | "root" )
    }

    logger.debug(f"Calling curio_create_user() ...")

    response = curio_create_user(param)

    logger.debug(f"curio_create_user() completed.")  

    ## return value
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");  

if __name__ == "__main__":
    main()
