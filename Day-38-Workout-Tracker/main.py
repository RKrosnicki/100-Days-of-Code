import os
import requests
import datetime

NUTRITIONIX_API_ID = os.environ['NUTRITIONIX_API_ID']
NUTRITIONIX_API_KEY = os.environ['NUTRITIONIX_API_KEY']

nutritionix_headers = {
    "x-app-id": NUTRITIONIX_API_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-remote-user-id": "0",
    "Content-Type": "application/json",
}

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("Tell me about your workout: ")
nutritionix_params = {
    "query": query,
    "gender": "male",
    "weight_kg": 100,
    "height_cm": 185,
    "age": 33
}

response = requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers=nutritionix_headers)
data = response.json()

SHEETY_ENDPOINT = "https://api.sheety.co/f930d7e57b9984b2e78e7875178f5638/workoutTracking/workout"
sheety_header = {
        "Authorization": os.environ['SHEETY_AUTHORIZATION'],
        "Content-Type": "application/json",
    }

today = datetime.datetime.now()
time = today.strftime("%H:%M:%S")
today = today.strftime("%d/%m/%Y")

for exercise in data['exercises']:
    sheety_params = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
            }
        }

    response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers=sheety_header)
    print(response.text)
    print(response.status_code)
