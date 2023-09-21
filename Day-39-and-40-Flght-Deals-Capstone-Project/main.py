from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


flight_data = FlightData()

data_manager = DataManager()
data = data_manager.get_sheet()
print(data)

flight_search = FlightSearch()

# data_manager.update_codes(data)    # Run this function just once, to update IATA codes in your Google Sheet:
notification_manager = NotificationManager()

for record in data['price']:
    print(f"Checking {record['city']} >>>>>>>>>>>>>>")
    result = flight_search.search(record['iataCode'], record['lowestPrice'])
    if result['_results'] != 0:
        result = flight_search.search(record['iataCode'], record['lowestPrice'])
        print(result)
        notification_manager.send_message(result)
    print("===================================")

# print(prices_dict)
