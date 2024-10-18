#Wasabi AiR SDK for Python

This is a sample of python code that can be positioned as a Wasabi AiR SDK for Python. It implements a high-level function wrapping the REST API call with a simple function call.

It is based on [Wasabi AiR API Reference]
(https://docs.wasabi.com/docs/wasabi-air-api-reference) which is officially published and maintenanced by Wasabi Technologies LLC.

## Profile and Wasabi AiR SDK configurations
Just like the AWS CLI credentials file, Wasabi AiR SDK config file is introduced.
This is to provide a way to switch target endpoint URLs and the associated API Key without changing the source codes.

You can define a "Profile" that holds the endpoint URL and the associated WAsabi AiR API Key, and it is possible to define multiple profiles. These information are managed by the Wasabi AiR SDK configuration file named curio.conf, which is to be installed on the following path:
~/.wasabi/curio.conf

*(Important)* Please create the .wasabi folder, under your home directory, and the curio.conf manually as at this moment, there is no installer created to automate the setup.

(note) Please refer to the following AWS document explaining details of the configuration files:
https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html

### ~/.wasabi/curio.conf
The following is a sample of the Wasabi Air SDK Configuration file for the use with the sample code provided here:
```
[default]
endpoint_url = https://partner.wasabibeta.com
api_key_value = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
[wasabibeta]
endpoint_url = https://us.metafarm.dev
api_key_value = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
[wasabisys]
endpoint_url = https://partner.wasabisys.com
api_key_value = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```