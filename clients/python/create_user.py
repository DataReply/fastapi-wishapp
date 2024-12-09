import sys

sys.path.append('out/python')
import openapi_client
from openapi_client.models.user_create import UserCreate
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host="http://localhost:8000"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UsersApi(api_client)
    user_create = UserCreate(email="a@b.c", password="a")

    try:
        # Create User
        api_response = api_instance.create_user(user_create)
        print("The response of UsersApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
