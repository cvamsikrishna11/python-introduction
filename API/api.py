"""
To explain the APIs flow & request module in python
https://reqres.in/
"""
# install pip requests with command --> pip install requests
import requests  # https://pypi.org/project/requests/

# we are gonna use the fake data end point https://reqres.in/
API_END_POINT = "https://reqres.in"


def get_all_users():
    # /api/users
    print("\n# Getting all the users list")
    # response = requests.get("https://reqres.in/api/users")
    response = requests.get("{}{}".format(API_END_POINT, "/api/users"))
    print("Response status code: {}".format(response))
    print("Response: {}".format(response.json()))
    return response.json()

# get_all_users()


def get_user(user_id):
    # /api/users/ID
    print("\n# Getting user with the id: {}".format(user_id))
    response = requests.get(
        "{}{}/{}".format(API_END_POINT, "/api/users", user_id))
    print("Response status code: {}".format(response))
    print("Response: {}".format(response.json()))
    return response.json()

# get_user(user_id=1)


def create_user(user_data):
    # /api/users
    print("\n# Creating a new user with the data: {}".format(user_data))
    response = requests.post(url="{}{}".format(
        API_END_POINT, "/api/users"), data=user_data)
    print("Response status code: {}".format(response))
    print("Response: {}".format(response.json()))
    return response.json()

# create_user({
#     "name": "avinash",
#     "job": "architect" 
# })


def update_user(user_id, user_data):
    # /api/users/ID
    print("\n# Update an existing user with id: {}, new details: {}".format(
        user_id, user_data))
    response = requests.put(url="{}{}/{}".format(
        API_END_POINT, "/api/users", user_id), data=user_data)
    print("Response status code: {}".format(response))
    print("Response: {}".format(response.json()))
    return response.json()


# update_user(user_id=40, user_data={
#             "name": "Iron man", "job": "part of avengers", "email": "ironnman@avengers.com"})

def delete_user(user_id):
    # /api/users/ID
    print("\n# Deleting user with the id: {}".format(user_id))
    response = requests.delete(
        "{}{}/{}".format(API_END_POINT, "/api/users", user_id))
    print("Response status code: {}".format(response))    
    return response

delete_user(user_id=100)