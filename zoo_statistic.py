import requests
from pywebio.output import put_success, put_error, put_warning, put_image, put_html, put_table
from pywebio.session import run_js
from pywebio import start_server

url = "https://script.google.com/macros/s/AKfycbyoPdk3GJHUN83Y5vbeCYUlfqjmIj38r2ZfTSEzFwgYlMGYSR3Gobe9nwYufw3DYIkJ/exec"


def get_zoo_data() -> dict:
    response = requests.get(url, timeout=5)
    data = response.json()
    return data


def get_zoo_details(zoo_data: dict) -> dict:
    result = {}
    result["monthly_price_for_poison_animals"] = 0
    result["animals_from_africa"] = 0

    for animal in zoo_data:
        if animal["poison"].lower() == "True":
            result["monthly_price_for_poison_animals"] += int(animal["monthlyprice"])


        if animal["location"].lower() == "африка":
            result["animals_from_africa"] += int(animal["quantity"])

    return result

if __name__ == "__main__":
    zoo_data = get_zoo_data()
    zoo_details = get_zoo_details(zoo_data)
    print(zoo_details)
