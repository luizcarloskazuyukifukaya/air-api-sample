# ======================================
# Python Sample for Wasabi AiR
# No guaranty from Wasabi Inc.
# ======================================

import functools
import requests
import json
import os

# Retrieve Wasabi AiR Environment specific variables
from curio_config import parse_conf # type: ignore

# Set environment variable for SSL key log file
os.environ["SSLKEYLOGFILE"] = "ssl-key.log"

# The default profile to be used
DEFAULT_CURIO_PROFILE = "default"

# Change profile from default to specific one
# IMPORTANT: the profile should be defined on ~/.wasabi/curio.conf
def curio_set_profile(profile_name):
    global DEFAULT_CURIO_PROFILE  # Declare the variable as global
    print(f"Set profile to {profile_name}")
    DEFAULT_CURIO_PROFILE = profile_name

# define decorator for REST API calls
def curio_rest_request(method='GET'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            # read CURIO config file (~/.wasabi/curio.conf)
            # Refer to the global variable defined for the profile
            global DEFAULT_CURIO_PROFILE  # Declare the variable as global
            # profile to be used can be changed by curio_set_profile

            api_conf = parse_conf(DEFAULT_CURIO_PROFILE)

            api_endpoint = api_conf['endpoint']
            # url = 'https://us.metafarm.dev'
            ## API Key value
            bearer_token = api_conf['api_key']
            ## Request Header with API Key Authentication
            # Authorization: Bearer {{token}}
            auth_bearer = 'Bearer {}'.format(bearer_token)
            api_head = {
                'Authorization': auth_bearer,
                'Content-Type': 'application/json',
                # 'X-Wasabi-Service': 'partner',
            }
            api_url = kwargs.get('url')
            # url example:
            # api_endpoint: https://us.graymeta.dev
            # api_url: /api/data/search
            url = '{}{}'.format(api_endpoint, api_url)
            body = kwargs.get('body', {})
            headers = api_head

            print(f"ENDPOINT : {api_endpoint}")
            print(f"API URI: {api_url}")
            print(f"URL: {url}")
            print(f"HEADER: {headers}")
            print(f"BODY: {body}")

            try:
                if method == 'GET':
                    response = requests.get(url, headers=headers)
                elif method == 'POST':
                    response = requests.post(url, data=json.dumps(body), headers=headers)
                elif method == 'PUT':
                    response = requests.put(url, data=json.dumps(body), headers=headers)
                elif method == "PATCH":
                    response = requests.patch(url, data=json.dumps(body), headers=headers)
                elif method == "DELETE":
                    response = requests.delete(url, headers=headers)
                elif method == "OPTIONS":
                    response = requests.options(url, headers=headers)
                else:
                    raise ValueError(f"Unsupported HTTP method: {method}")

                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"HTTP Request Error: {e}")
                return None

        return wrapper
    return decorator

# Curio GET, POST, PUT, PATCH and DELETE REST API CALL
# URI to be specified along with the body, if any
@curio_rest_request(method='GET')
def curio_get_data(url):
    pass

@curio_rest_request(method='POST')
def curio_post_data(url, body):
    pass

@curio_rest_request(method='PUT')
def curio_put_data(url, body):
    pass

@curio_rest_request(method="PATCH")
def curio_patch_data(url, body):
    pass

@curio_rest_request(method="DELETE")
def curio_delete_data(url):
    pass

@curio_rest_request(method="OPTIONS")
def curio_options_data(url):
    pass

# # Using the decorated functions
# List Keys
# https://docs.wasabi.com/docs/api-keys
# get_result = curio_get_data(url='/api/data/api-keys')
# if get_result:
#     print("GET Result:", get_result)

# post_result = curio_post_data(url='/api/data/api-keys', body={'key': 'value'})
# if post_result:
#     print("POST Result:", post_result)
