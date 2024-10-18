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
# Search API in Wasabi AiR
# https://docs.wasabi.com/docs/search-api
# -----------------------------------------------

############################################################################# 
# Search the metadata in Wasabi AiR
# -----------------------------------------
# Search contents based on the metadata
# =========================================
# ******************* 
#  Parameters
# *******************
# Input parameter
# NONE
# dict 
# {
#   "query": "",                             # string    (MANDATORY: search query)
# }
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
#   searchQuery = {
#       "query": "ship",
#   }
#   result = search_query(**searchQuery)
#
############################################################################# 
def curio_search(**searchQuery):
    query = {
        "query": "",                             # string    (MANDATORY: search query)
        }

    response = {}
    # check mandatory information required    
    # searchQuery (dictionary)
    # searchQuery['AcctName'] (Mandatory)
    if "query" in searchQuery:
        query["query"] = searchQuery["query"]
    else:
        # Missing mandatory parameters
        return response
            
    # check if all given parameters are correct or not
    hasUnknownParameter = False
    keyList = list(searchQuery.keys())
    for key in keyList:
        logger.debug(f"{key} is passed as a parameter")
        if key in searchQuery:
            # found matching parameter
            logger.debug(f"Matching parameter : {key} = {searchQuery[key]}")
            # query corresponding key's value is overwritten by the given parameter key's value
            query[key] = searchQuery[key]
        else:
            # Unknown parameter found
            logger.error(f"Wrong parameter is given.: {key} = {searchQuery[key]}")
            hasUnknownParameter = True
            break                        
    
    if hasUnknownParameter != True:
        logger.debug(f" Input parameter : {query}")
        # Call put_accounts()    
        response = search_query(query)
        logger.debug(f"search_query(query) called")
    return response

# search_query
# Call Wasabi AiR API for search
def search_query(q):

    from curio_config import parse_conf # type: ignore

    # read CURIO config file (~/.wasabi/curio.conf)
    # TODO
    api_conf = parse_conf("wasabi")

    url = api_conf['endpoint']
    # url = 'https://us.metafarm.dev'
    ## API Key value
    api_key_value = api_conf['api_key']
    # logger.debug(f"API Key is {api_key_value}")

    ## Request Header with API Key Authentication
    api_head = {
        'Authorization': api_key_value,
        'Content-Type': 'application/json',
        # 'X-Wasabi-Service': 'partner',
    }
    # "Content-Type: application/json; charset=utf-8" # request( ,json=data )
    # Content-Type: application/json
    # X-Wasabi-Service: partner

    #PUT /v1/accounts
    url = "{}/api/data/search".format(url)

    logger.debug(f"PUT {url}")
    logger.info(f"Target URL is {url}")

    # HTTPS PUT
    # data = acct
    # acct is confirmed to have all keys and values required to create the sub-account    
    logger.debug(f"HTTPS PUT Request start from here .............. ")
    logger.debug(f"URL =  {url}")
    logger.debug(f"headers =  {api_head}")
    logger.debug(f"data =  {q}")

    ## PUT request
    ## requests.put(url, params={key: value}, args)
    ## requests.put( url, headers=api_head, data=q);
    # ********* requests.put only works with 'json=q' *************

    # ********** THIS WORKS ALSO *************************************
    #r = requests.put( url, headers=api_head, json=q);

    logger.debug(f"data JSON =  {json.dumps(q)}")
    r = requests.put( url, headers=api_head, data=json.dumps(q))

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
        
    param = {
        "query": "ship",                              # string    (MANDATORY: search query)
        }

    logger.debug(f"Search query = {param['query']}")  
    
    logger.debug(f"Calling curio_search() ...")

    response = curio_search(**param)

    logger.debug(f"curio_search() completed.")  

    ## return value 
    logger.debug(f"{response}");  
    logger.debug(f"{type(response)}");  

if __name__ == "__main__":
    main()