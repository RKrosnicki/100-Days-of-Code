import requests
import os
from twilio.rest import Client

ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
OWM_KEY = os.environ['OWM_API_KEY']

def send_sms(message:str):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
             body=message,
             from_='+16072282842',
             to=os.environ['MY_NUMBER']
         )
    print(message.status)

weather_parameters = {
    "lat": 52.229675,
    "lon": 21.012230,
    "appid": OWM_KEY,
    "exclude": "current,minutely,daily,alerts",
    }

OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"

response = requests.get(url=OWM_ENDPOINT, params=weather_parameters)
print(response.raise_for_status())
weather_data = response.json()

#print(weather_data)

weather_slice = weather_data['hourly'][:12]
for hour in weather_slice:
    weather_status_code = hour['weather'][0]['id']
    #print(weather_status_code)
    if weather_status_code < 700:
        print("Sending message...")
        send_sms("\nIt's gonna rain in next 12 hours.\nYou better take an umbrella!\n☔☔☔")
        break

