import requests
import os
from datetime import datetime, timedelta
from notification_manager import NotificationManager


class FlightSearch:
    def __init__(self):
        self.kiwi_header = {
            "apikey": os.environ['KIWI_API_KEY'],
            "accept": "application/json",
            "Content-Encoding": "gzip"
        }

        self.endpoint = "https://api.tequila.kiwi.com/search"

        self.fly_from = "WAW"
        self.now = datetime.now()
        self.today = self.now.strftime("%d/%m/%Y")
        self.day_in_6m = (self.now + timedelta(days=180)).strftime("%d/%m/%Y")

    def search(self, destination, max_price, stop_overs=0):
        search_params = {
            "fly_from": self.fly_from,
            "fly_to": destination,
            "date_from": self.today,
            "date_to": self.day_in_6m,
            "price_to": max_price,
            "max_stopovers": stop_overs,
            "limit": 10
        }
        response = requests.get(url=self.endpoint, params=search_params, headers=self.kiwi_header)
        # print(response.text)
        return response.json()


# try_it = FlightSearch()
# data = try_it.search("ORY", 500)
# notification_manager = NotificationManager()
# notification_manager.send_message(data)

