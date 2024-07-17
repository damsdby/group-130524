import requests
import json

pdf_url = 'https://chtyvo.org.ua/authors/Falkovych_Hryhorii/Smyk-tyndyk.pdf'
pdf_response = requests.get(pdf_url)
if pdf_response.status_code == 200:
    with open('Smyk-tyndyk.pdf', 'wb') as pdf_file:
        pdf_file.write(pdf_response.content)

api_url = 'http://api.open-notify.org/astros.json'
api_response = requests.get(api_url)
if api_response.status_code == 200:
    data = api_response.json()
    with open('astros.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
