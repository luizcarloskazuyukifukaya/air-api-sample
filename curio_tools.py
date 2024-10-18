# ======================================
# Python Sample for Wasabi AiR
# No guaranty from Wasabi Inc.
# ======================================

import functools
import requests
import json

# define decorator for REST API calls
def rest_request(method='GET'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
          
            # Retrieve Wasabi AiR Environment specific variables
            from curio_config import parse_conf # type: ignore

            # read CURIO config file (~/.wasabi/curio.conf)
            # TODO
            api_conf = parse_conf("wasabi")

            api_endpoint = api_conf['endpoint']
            # url = 'https://us.metafarm.dev'
            ## API Key value
            bearer_token = api_conf['api_key']
            ## Request Header with API Key Authentication
            #Authorization: Bearer {{token}}
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

            try:
                if method == 'GET':
                    response = requests.get(url, headers=headers)
                elif method == 'POST':
                    response = requests.post(url, data=json.dumps(body), headers=headers)
                elif method == 'PUT':
                    response = requests.put(url, data=json.dumps(body), headers=headers)
                elif method == 'DELETE':
                    response = requests.delete(url, headers=headers)
                else:
                    raise ValueError(f"Unsupported HTTP method: {method}")

                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"HTTP Request Error: {e}")
                return None

        return wrapper
    return decorator

# Curio GET, POST, PUT, DELETE REST API CALL
# URI to be specified along with the body, if any
@rest_request(method='GET')
def curio_get_data(url):
    pass

@rest_request(method='POST')
def curio_post_data(url, body):
    pass

@rest_request(method='PUT')
def curio_put_data(url, body):
    pass

@rest_request(method='DELETE')
def curio_delete_data(url):
    pass

# # Using the decorated functions
# List Keys
# https://docs.wasabi.com/docs/api-keys
# get_result = get_data(url='/api/data/api-keys')
# if get_result:
#     print("GET Result:", get_result)

# post_result = post_data(url='/api/data/api-keys', body={'key': 'value'})
# if post_result:
#     print("POST Result:", post_result)
