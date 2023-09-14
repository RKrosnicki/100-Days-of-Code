import requests
import os
from twilio.rest import Client

ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

def send_sms(message:str):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
             body=message,
             from_='+16072282842',
             to='+48511345587'
         )
    print(message.status)

weather_parameters = {
    "lat": 47.793301,
    "lon": 22.877081,
    "appid": "0fcac87a96e0eea68813a009605ab016",
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

