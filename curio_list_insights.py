# ======================================
# Python Sample for Wasabi AiR
# No guaranty from Wasabi Inc.
# ======================================

from curio_tools import rest_request
from curio_tools import curio_get_data, curio_post_data, curio_put_data, curio_delete_data

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
# Listing All Insights Groups with associated Words
# https://docs.wasabi.com/docs/insights-api
# -----------------------------------------------

#############################################################################
# Listing All Insights Groups with associated Words
# -----------------------------------------
# The Insights API enables you to create groups of words to search for in audio tracks (speech-to-text) and various other document text. This is useful for compliance issues and flagging specific spoken or written phrases.
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
#     "insight_groups": [
#         {
#             "insight_group_id": "596fd91dd5fec5aae37fe02f9d393df8",
#             "name": "Bad Words",
#             "color": "#FF0000",
#             "num_words": 7,
#             "created_at": "2017-07-19T22:11:41.752231Z",
#             "updated_at": "2017-07-19T22:16:46.122576Z",
#             "words": ["ass", "bad", "boom", "crap", "fudge", "poop", "shoot"],
#             "access_groups": [
#                 "5ec36cca9f163654dc737e6fb8822321",
#                 "5ec36cce7f5637d4815cac98a59173d0",
#             ],
#         },
#         {
#             "insight_group_id": "596fd91dd5fec5aae37fe02f9d393df8",
#             "name": "Band Names",
#             "color": "#006699",
#             "num_words": 4,
#             "created_at": "2017-07-19T22:11:41.752231Z",
#             "updated_at": "2017-07-19T22:16:46.122576Z",
#             "words": ["eagles", "pink floyd", "rolling stones", "zz top"],
#             "access_groups": [],
#         },
#     ]
# }
# FAIL
# {} # NULL (dictionary)
#
#############################################################################
def curio_list_insights():

    # GET /api/data/v3/insights
    api_method = "GET"
    api_url = "/api/data/v3/insights"

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
    
    logger.debug(f"Calling curio_list_insights() ...")

    response = curio_list_insights()

    logger.debug(f"curio_list_insights() completed.")  

    ## return value 
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");  

if __name__ == "__main__":
    main()
