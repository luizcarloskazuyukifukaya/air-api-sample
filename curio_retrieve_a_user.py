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
# Retrieving the User
# https://docs.wasabi.com/docs/users-and-groups-api
# -----------------------------------------------

#############################################################################
# Retrieving the User
# -----------------------------------------
# Retrieving the User specified by the id
# =========================================
# *******************
#  Parameters
# *******************
# Input parameter
# Parameter (id, email)
# *******************
#  Return value
# *******************
# SUCCESS
# {
#     "users": [
#         {
#             "id": "583ba3125b9f5421e1cb5702deb8d45e",
#             "email": "ada@wasabi.com",
#             "first_name": "Ada",
#             "last_name": "Lovelace",
#             "enabled": true,
#             "role_id": "59de4bb09221034b071d83db64950d34",
#             "created_at": "2016-11-28T00:00:00Z",
#             "updated_at": "2016-11-28T14:22:58.44874Z"
#         },
#         {...},
#         {...}
#     ]
# }
# FAIL
# {} # NULL (dictionary)
#
#############################################################################
# By id
# GET /api/data/users/{id}
def curio_retrieve_a_user(id):

    #GET /api/data/users/{id}
    api_method = "GET"
    api_url = "/api/data/users/{}".format(id)

    response = {}

    logger.debug(f" Input parameter : {id}")

    response = curio_get_data(url=api_url)

    logger.debug(f"get_data({api_url}) called")

    return response

# By E-mail address
# GET /api/data/users?email=ada@wasabi.com
def curio_retrieve_a_user_by_email(email):

    #GET /api/data/users?email=ada@wasabi.com
    api_method = "GET"
    api_url = "/api/data/users?email={}".format(email)

    response = {}

    logger.debug(f" Input parameter : {email}")

    response = curio_get_data(url=api_url)

    logger.debug(f"get_data({api_url}) called")

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
def get_user_by_id():
    # for test (kfukaya@wasabi.com / tokyo.metafarm.dev)
    user_id = "67126201b10c9abfb41d7c1b8c764d12"
    # by id
    logger.debug(f"Calling curio_retrieve_a_user(id) ...")

    response = curio_retrieve_a_user(user_id)

    logger.debug(f"curio_retrieve_a_user(id) completed.")  

    ## return value 
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");    

def get_user_by_email():
    # for test (kfukaya@wasabi.com / tokyo.metafarm.dev)
    email = "kfukaya@wasabi.com"
    # by email
    logger.debug(f"Calling curio_retrieve_a_user_by_email(email) ...")

    response = curio_retrieve_a_user_by_email(email)

    logger.debug(f"curio_retrieve_a_user_by_email(email) completed.")  

    ## return value 
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");    

def main():
    get_user_by_id()
    get_user_by_email()

if __name__ == "__main__":
    main()
