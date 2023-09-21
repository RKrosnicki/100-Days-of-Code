import os
import requests


class FlightData:
    def __init__(self):
        self.kiwi_header = {
            "apikey": os.environ['KIWI_API_KEY'],
            "accept": "application/json",
            "Content-Encoding": "gzip"
        }

    def city_code_search(self, city):
        tequila_loc_endpoint = "https://api.tequila.kiwi.com/locations/query"

        tequila_loc_params = {
            "term": city,
            "location_types": "airport",
            "limit": 10,
            "active-only": True
        }

        code_search_response = requests.get(url=tequila_loc_endpoint, params=tequila_loc_params, headers=self.kiwi_header)
        code_search_data = code_search_response.json()
        # print(code_search_response.text)
        return code_search_data["locations"][0]['city']['code']

