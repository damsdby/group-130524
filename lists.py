import requests

url_ = "http://api.open-notify.org/astros.json"
responce = requests.get(url_)
data = responce.json()

astros_list = [astronaut["name"] for astronaut in data["people"]]
for astronaut in astros_list:
    print(astronaut)

url_second = "https://dummyjson.com/users"
responce_second = requests.get(url_second)
data_second = responce_second.json()


#for user in data_second:
    #if user["age"] == 28:
        #print(f"{user['firstName']}{user['lastName']}")


users_age_special = [f"{user['firstName']} {user['lastName']}"
            for user in data_second['users']
            if user['age'] is 28]
for user in users_age_special:
    print(user)



