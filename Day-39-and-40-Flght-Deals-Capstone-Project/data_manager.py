import requests
import os
from flight_search import FlightSearch

flight_search = FlightSearch()


class DataManager:
    def __init__(self):
        self.SHEETY_ENDPOINT = "https://api.sheety.co/f930d7e57b9984b2e78e7875178f5638/flightDeals/price"

        self.sheety_header = {
            "Authorization": os.environ['SHEETY_AUTHORIZATION'],
            "Content-Type": "application/json",
        }

    def get_sheet(self):
        response = requests.get(url=self.SHEETY_ENDPOINT, headers=self.sheety_header)
        data = response.json()
        # print(response.text)
        return data

    def update_codes(self, cities_to_update_data):
        for city in cities_to_update_data['price']:
            city_name = city['city']
            code = flight_search.city_code_search(city_name)

            sheety_params = {
                "price": {
                    "iataCode": code,
                }
            }
            put_endpoint = f"{self.SHEETY_ENDPOINT}/{city['id']}"
            put_response = requests.put(url=put_endpoint, json=sheety_params, headers=self.sheety_header)
            print(put_response.text)
