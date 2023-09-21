from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


flight_data = FlightData()

data_manager = DataManager()
data = data_manager.get_destinations_data()

flight_search = FlightSearch()
notification_manager = NotificationManager()

email_text = ""

for record in data['price']:
    print(f"Checking {record['city']} >>>>>>>>>>>>>>")
    result = flight_search.search(record['iataCode'], record['lowestPrice'])
    if result['_results'] != 0:
        result = flight_search.search(record['iataCode'], record['lowestPrice'])
        notification_manager.send_sms(result)
        print("Sending direct flight info.")
    else:
        result = flight_search.search(destination=record['iataCode'], max_price=record['lowestPrice'], stop_overs=1)
        notification_manager.send_sms(result, direct=False)
        print("Sending non-direct flight info.")
    print("===================================")

    email_text += f"{notification_manager.formatted_message}\n=============================================\n"

customers = data_manager.get_customers()
# print(customers['user'])

for customer in customers['user']:
    notification_manager.send_email(customer, email_text)

