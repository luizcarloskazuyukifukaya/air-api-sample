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
# Retrieving Duplicate Stats
# https://docs.wasabi.com/docs/duplicates-api
# https://docs.wasabi.com/docs/duplicates-api
# -----------------------------------------------

#############################################################################
# Listing Duplicated Hashes
# -----------------------------------------
# The Duplicates API is a way to access information about items that have identical checksums and file sizes. Such items are considered to be duplicate copies of the same file.
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
#     "duplicates": [
#         {
#             "hash": "1bf6808152b518ec38b18780f96526ef",
#             "items": [
#                 "0ddc337d7f399b406073f5f8e5324fc4",
#                 "3566d2ff4aea65d30eda983c2c749274",
#                 "444ccc35017f1e39188d735d7ec126a0",
#                 "4a86bb348ba1050511777d40a2471d3e",
#                 "69af63e7f10ad1b8fa5e9a05f149bbea",
#                 "7d63cf40504e9f2501250f731fea03b0",
#                 "84deb4ebb35d5c78cd69b9dce4eaf4b5",
#                 "cbbf806d29b43fdbeb9f2516e4813525",
#                 "faa93144670268595c8acc823e861de7"
#             ],
#             "count": 9,
#             "file_size": 614912,
#             "footprint_size": 39803040,
#             "items_next_page": ""
#         },
#         {
#             "hash": "fd083c80752b24b6085eb773ed1b9609",
#             "items": [
#                 "4223082baa8abcb70c1fcd600b0f7b83",
#                 "82d37a0a16911b49a001e5686ad58a07",
#                 "92306656ab6c366b113af0cc6ca0abad",
#                 "92fb0a09883700b8c2116eaccf2b80e8",
#                 "9c8b1b15613e22f3474291f3ea2d8ca6",
#                 "be265a032be6d5b759e1ead68df875b9",
#                 "c27582011f2966350c7a64c834d88637",
#                 "dcb2c7f92cecac5b2a89fdd046a9bac8",
#                 "fe63caef8d1089b930a76dfc21dd5634"
#             ],
#             "count": 9,
#             "file_size": 3598,
#             "footprint_size": 28784,
#             "items_next_page": ""
#         },
#         {
#             "hash": "c37470f71fb1bc9c7242c5282274cdd8",
#             "items": [
#                 "017dc9a61a040855f819f48b85d3119b",
#                 "651f0dc8cd2d2fe9d2b8462dfa03d04b",
#                 "82aaa25ff23826e21629d9f391b83d18",
#                 "84e5ae7f3fcd7caa4259d1480f057a73"
#             ],
#             "count": 4,
#             "file_size": 54047,
#             "footprint_size": 162141,
#             "items_next_page": ""
#         },
#         {
#             "hash": "6461a4d3c389f561207065dfd8d4c01b",
#             "items": [
#                 "0fc10bd128c62699c80d3af21d5356ba",
#                 "eb41c0739e90a24d7d855933c5d3c231"
#             ],
#             "count": 2,
#             "file_size": 367922,
#             "footprint_size": 367922,
#             "items_next_page": ""
#         }
#     ],
#     "next_page": ""
# }
# FAIL
# {} # NULL (dictionary)
#
#############################################################################
def curio_list_duplicated_hashes():

    #GET /api/data/v3/duplicates
    api_method = "GET"
    api_url = "/api/data/v3/duplicates"
    response = {}

    logger.debug(f" Input parameter : NONE")

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
def main():
    
    logger.debug(f"Calling curio_list_duplicated_hashes() ...")

    response = curio_list_duplicated_hashes()

    logger.debug(f"curio_list_duplicated_hashes() completed.")  

    ## return value 
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");  

if __name__ == "__main__":
    main()
