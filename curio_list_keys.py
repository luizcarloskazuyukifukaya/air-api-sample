# ======================================
# Python Sample for Wasabi AiR
# No guaranty from Wasabi Inc.
# ======================================

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
# Listing All Keys for a User
# https://docs.wasabi.com/docs/api-keys
# -----------------------------------------------

############################################################################# 
# Listing All Keys for a User
# -----------------------------------------
# List for all key for a user what is associated with the access key
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
#     "api-keys": [
#         {
#             "id": "abc123",
#             "jwt": "APIKEY",
#             "active": true,
#             "user_id": "591481bf1940f20c341b9386a9a192f4",
#             "created_at": "2017-05-31T20:56:04.002433Z",
#             "updated_at": "2017-05-31T20:56:04.002433Z"
#         },
#         {
#             "id": "abc124",
#             "jwt": "APIKEY",
#             "active": true,
#             "user_id": "591481bf1940f20c341b9386a9a192f4",
#             "created_at": "2017-05-31T20:56:04.002433Z",
#             "updated_at": "2017-05-31T20:56:04.002433Z"
#         },
#         {
#             "id": "abc125",
#             "jwt": "APIKEY",
#             "active": false,
#             "user_id": "591481bf1940f20c341b9386a9a192f4",
#             "created_at": "2017-05-31T20:56:04.002433Z",
#             "updated_at": "2017-05-31T20:56:04.002433Z"
#         }
#     ]
# }
# FAIL
# {} # NULL (dictionary)
#
############################################################################# 
def curio_list_keys():

    response = {}

    logger.debug(f" Input parameter : NONE")
    # Call list_keys()    
    response = list_keys()
    logger.debug(f"list_keys()) called")

    return response

# list_keys
# Call Wasabi AiR API for listing keys
def list_keys():

    from curio_config import parse_conf # type: ignore

    # read CURIO config file (~/.wasabi/curio.conf)
    # TODO
    api_conf = parse_conf("wasabi")

    url = api_conf['endpoint']
    # url = 'https://us.metafarm.dev'
    ## API Key value
    bearer_token = api_conf['api_key']
    
    # logger.debug(f"API Key is {bearer_token}")

    ## Request Header with API Key Authentication
    #Authorization: Bearer {{token}}
    auth_bearer = 'Bearer {}'.format(bearer_token)
    api_head = {
        'Authorization': auth_bearer,
        'Content-Type': 'application/json',
        # 'X-Wasabi-Service': 'partner',
    }
    # "Content-Type: application/json; charset=utf-8" # request( ,json=data )
    # Content-Type: application/json
    # X-Wasabi-Service: partner

    #GET /api/data/api-keys
    url = "{}/api/data/api-keys".format(url)

    logger.debug(f"GET {url}")
    logger.info(f"Target URL is {url}")

    # HTTPS GET
    logger.debug(f"HTTPS GET Request start from here .............. ")
    logger.debug(f"URL =  {url}")
    logger.debug(f"headers =  {api_head}")
    logger.debug(f"data =  NONE")

    r = requests.get( url, headers=api_head)

    ## Response status code
    logger.info(f"status: {r.status_code}") ; 

    ## Response RAW
    logger.debug(f"{r.reason}");  
    logger.debug(f"{r.text}");
      
    # logger.debug(f"{r.json()}");  
    # logger.debug(f"{type(r.json())}");  
 
    #print(f"{r.json()}");  
    #print(f"{type(r.json())}");  
    ## Sub-Accounts Information
    response = {} # default NULL
    if r.status_code == 200:
        response = r.json()
        logger.debug("===================================================================================");
        logger.debug(response);
        logger.debug("-----------------------------------------------------------------------------------");
        logger.info(f"Response: {response}");
    return response

# for the execution of this script only
def main():
    
    logger.debug(f"Calling curio_list_keys() ...")

    response = curio_list_keys()

    logger.debug(f"curio_list_keys() completed.")  

    ## return value 
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");  

if __name__ == "__main__":
    main()