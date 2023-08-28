import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.header_user)


response = post_new_user(data.user_body)

auth_token = data.header_kit
user_token = "Bearer " + response.json()["authToken"]
auth_token["Content-Type"] = data.header_user["Content-Type"]
auth_token["Authorization"] = user_token

print(response.status_code)
print(response.json())


def post_new_client_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATING_KIT,
                         json=body,
                         headers=auth_token)


response = post_new_client_kit(data.kit_body)

print(response.status_code)
print(response.json())
