from datetime import datetime
from twilio.rest import Client
import os


class NotificationManager:
    def __init__(self):
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']

        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self, data):
        destination = data['data'][0]["cityTo"]
        destination_code = data['data'][0]["cityCodeTo"]

        odlot = data['data'][0]['dTime']
        dt_object = datetime.fromtimestamp(odlot)
        cena = data['data'][0]['fare']['adults']
        formatted_message = (f"Znaleziono tani lot!\n"
              f"Do {destination}({destination_code})\n"
              f"Czas odlotu: {dt_object}\n"
              f"Cena: EUR {cena}\n")

        message = self.client.messages.create(
             body=formatted_message,
             from_='+16072282842',
             to=os.environ['MY_NUMBER']
         )

