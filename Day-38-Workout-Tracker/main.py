import os
import requests

APP_ID = os.environ['NUTRITIONIX_API_ID']
APP_KEY = os.environ['NUTRITIONIX_API_KEY']

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    # "x-remote-user-id": "0",
    "Content-Type": "application/json",
}

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("Tell me about your workout: ")
exercise_params = {
    "query": query,
    "gender": "male",
    "weight_kg": 100,
    "height_cm": 185,
    "age": 33
}

response = requests.post(url=endpoint, json=exercise_params, headers=headers)
print(response.text)
