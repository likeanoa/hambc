# Imports and variables

import requests, psutil, json

with open("config.json", "r") as f:
    data = json.load(f)

url = data["url"]
token = data["token"]
entity_id = data["entity_id"]
verbose = data["verbose"]

battery = round(psutil.sensors_battery().percent)

# Payload and header configuration

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
}

payload = {
    "state": battery,
    "attributes": {
        "unit_of_measurement": "%",
        "friendly_name": "Battery Sensor"
    }
}

response = requests.post(
    f"{url}/api/states/{entity_id}",
    headers=headers,
    json=payload,
    timeout=10
)

# Response functions and handling

def print_response():
    if response.status_code == 200:
        print("200 OK")
    else:
        print("Failed:", response.status_code, response.text)

if(verbose.casefold() == "True".casefold()):
    print_response()
