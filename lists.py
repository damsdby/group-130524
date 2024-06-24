import requests

url_ = "http://api.open-notify.org/astros.json"
responce = requests.get(url_)
data = responce.json()

astros_list = [person["name"] for person in data["people"]]
for astronaut in astros_list:
    print(astronaut)

url_second = "https://dummyjson.com/users"
responce_second = requests.get(url_second)
data_second = responce_second.json()

user_age_special = [f" {user['first_name']} {user['last_name']}" for user in data_second[" users "] if
                    user["age"] is 28]
for user in user_age_special:
    print(user_age_special)

