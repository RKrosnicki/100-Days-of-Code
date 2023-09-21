from datetime import datetime
from twilio.rest import Client
import os
import smtplib


class NotificationManager:
    def __init__(self):
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']

        self.client = Client(self.account_sid, self.auth_token)

        self.MY_EMAIL = "p97909805@gmail.com"
        self.MY_PASSWORD = "uqtflyxjddanvnin"
        self.formatted_message = ""

    def send_sms(self, data, direct=True):
        destination = data['data'][0]["cityTo"]
        destination_code = data['data'][0]["cityCodeTo"]

        departure_date = data['data'][0]['dTime']
        dt_object = datetime.fromtimestamp(departure_date)
        price = data['data'][0]['fare']['adults']
        if direct:
            self.formatted_message = (f"Znaleziono tani lot!\n"
                                      f"Do {destination}({destination_code})\n"
                                      f"Czas odlotu: {dt_object}\n"
                                      f"Cena: EUR {price}\n")
        else:
            via_city = data['data'][0]['route'][0]
            self.formatted_message = (f"Znaleziono tani lot!\n"
                                      f"Do {destination}({destination_code})\n"
                                      f"Czas odlotu: {dt_object}\n"
                                      f"Przez: {via_city['cityTo']}({via_city['cityCodeTo']})\n"
                                      f"Cena: EUR {price}\n")

        message = self.client.messages.create(
            body=self.formatted_message,
            from_='+16072282842',
            to=os.environ['MY_NUMBER']
        )

    def send_email(self, customer, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.MY_EMAIL, password=self.MY_PASSWORD)
            connection.sendmail(
                from_addr=self.MY_EMAIL,
                to_addrs=customer["email"],
                msg=f"Subject: {customer['firstName']}! We found flight deal!\n\n{message}"
            )
