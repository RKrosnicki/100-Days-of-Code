import requests
import os
from flight_search import FlightSearch
from flight_data import FlightData

flight_search = FlightSearch()
flight_data = FlightData()


class DataManager:
    def __init__(self):
        self.SHEETY_ENDPOINT = "https://api.sheety.co/0601f4b69e6a988854e44574d1eca957/flightDeals/"

        self.sheety_header = {
            "Authorization": os.environ['SHEETY_SECOND_AUTH'],
            "Content-Type": "application/json",
        }

    def get_destinations_data(self):
        response = requests.get(url=f"{self.SHEETY_ENDPOINT}price", headers=self.sheety_header)
        data = response.json()
        # print(data)
        self.update_codes(data)
        # print(response.text)
        return data

    def update_codes(self, cities_to_update_data):
        for city in cities_to_update_data['price']:
            if not city['iataCode']:
                print("=================================\n"
                      "Updating IATA Code\n"
                      "=================================\n")
                city_name = city['city']
                code = flight_data.city_code_search(city_name)
                # print(city)
                sheety_params = {
                    "price": {
                        "iataCode": code,
                    }
                }
                put_endpoint = f"{self.SHEETY_ENDPOINT}/{city['id']}"
                put_response = requests.put(url=put_endpoint, json=sheety_params, headers=self.sheety_header)
                # print(put_response.text)

    def get_customers(self):
        response = requests.get(url=f"{self.SHEETY_ENDPOINT}user", headers=self.sheety_header)
        return response.json()
