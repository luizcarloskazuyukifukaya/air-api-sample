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
# Listing audit records
# https://docs.wasabi.com/docs/audit-api
# -----------------------------------------------

#############################################################################
# Listing audit records
# -----------------------------------------
# The Audit API enables you to view audit records generated by the platform
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
#     "audit_events": [
#         {
#             "id": "59de4bb09221034b071d83db64950d34",
#             "user_id": "59790c0f1ab46239e59188bed540bfc7",
#             "action_key": "login",
#             "target_kind": "authenticate",
#             "target_id": "59790c0f1ab46239e59188bed540bfc7",
#             "time": "2017-10-11T16:49:52.758191Z"
#         },
#         {
#             "id": "59e12813db0201953dfe7214c4750e88",
#             "user_id": "59790c0f1ab46239e59188bed540bfc7",
#             "action_key": "enable",
#             "target_kind": "feature",
#             "target_id": "disabled_live_harvesting",
#             "time": "2017-10-13T20:54:43.14061Z"
#         },
#     ...
#     ],
#     "total": 71,
#     "page": 0
# }
# FAIL
# {} # NULL (dictionary)
#
#############################################################################
def curio_list_audit():

    # GET /api/data/api-keys
    api_method = "GET"
    api_url = "/api/data/audit"

    response = {}

    logger.debug(f" Input parameter : NONE")

    response = curio_get_data(url=api_url)

    logger.debug(f"get_data({api_url}) called")

    return response


#############################################################################
# Retrieving a Specific Audit Event
# -----------------------------------------
# Retrieving a Specific Audit Event by the event id
# =========================================
# *******************
#  Parameters
# *******************
# Input parameter
# id: event id
# *******************
#  Return value
# *******************
# SUCCESS
# {
#     "id": "59e12813db0201953dfe7214c4750e88",
#     "user_id": "59790c0f1ab46239e59188bed540bfc7",
#     "action_key": "enable",
#     "target_kind": "feature",
#     "target_id": "disabled_live_harvesting",
#     "time": "2017-10-13T20:54:43.14061Z",
# }
# FAIL
# {} # NULL (dictionary)
#
#############################################################################
def curio_retrieve_an_audit(id):

    # GET /api/data/audit/{id}
    api_method = "GET"
    api_url = "/api/data/audit/{}".format(id)

    response = {}

    logger.debug(f" Input parameter : {id}")

    response = curio_get_data(url=api_url)

    logger.debug(f"get_data({api_url}) called")

    return response


#############################################################################
# Listing Available Target Kinds and Action Keys
# -----------------------------------------
# Listing Available Target Kinds and Action Keys
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
#     "target_kinds": [
#         {"name": "authenticate", "action_keys": ["login", "update-password"]},
#         {"name": "feature", "action_keys": ["enable"]},
#         {"name": "group", "action_keys": ["create"]},
#     ]
# }
# FAIL
# {} # NULL (dictionary)
#
#############################################################################
def curio_list_filters():

    # GET /api/data/audit/filters
    api_method = "GET"
    api_url = "/api/data/audit/filters"

    response = {}

    logger.debug(f" Input parameter : NONE")

    response = curio_get_data(url=api_url)

    logger.debug(f"get_data({api_url}) called")

    return response


# Usage example
def list_audit():
    logger.debug(f"Calling curio_list_keys() ...")

    response = curio_list_audit()

    logger.debug(f"curio_list_keys() completed.")

    ## return value
    logger.debug(f"{response}")
    logger.debug(f"{type(response)}")

def retrieve_a_audit():

    # retrieve the fist event from the response and request details
    event_id = ""
    r = curio_list_audit()

    if len(r):
        event_id = r["audit_events"][0]["id"]
        logger.debug(f"Calling curio_retrieve_an_audit({event_id}) ...")

        response = curio_retrieve_an_audit(event_id)

        logger.debug(f"curio_retrieve_an_audit() completed.")

        logger.debug(f"{response}")
        logger.debug(f"{type(response)}")


def list_filters():

    # Listing Available Target Kinds and Action Keys
    logger.debug(f"Calling curio_list_filters() ...")

    response = curio_list_filters()

    logger.debug(f"curio_list_filters() completed.")

    ## return value
    logger.debug(f"{response}")
    logger.debug(f"{type(response)}")


# for the execution of this script only
def main():
    list_audit()
    retrieve_a_audit()
    list_filters()

if __name__ == "__main__":
    main()
