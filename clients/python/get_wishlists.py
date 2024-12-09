import sys

sys.path.append('out/python')

import openapi_client
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8000"
)

USER_EMAIL = "a@b.c"
PASSWORD = "a"

def get_token():
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = openapi_client.AuthApi(api_client)
        username = USER_EMAIL
        password = PASSWORD
        grant_type = 'password'
        scope = '' # str |  (optional) (default to '')
        client_id = 'client_id_example' # str |  (optional)
        client_secret = 'client_secret_example' # str |  (optional)

        try:
            # Login
            api_response = api_instance.login(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)
            return api_response.access_token
        except Exception as e:
            print("Exception when calling AuthApi->login: %s\n" % e)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
def get_wishlists():
    token = get_token()
    configuration.access_token = token

    # Enter a context with an instance of the API client
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = openapi_client.WishlistsApi(api_client)

        try:
            # Get Wishlists
            api_response = api_instance.get_wishlists()
            print("The response of WishlistsApi->get_wishlists:\n")
            pprint(api_response)
        except Exception as e:
            print("Exception when calling WishlistsApi->get_wishlists: %s\n" % e)

get_wishlists()