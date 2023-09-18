import requests
import os
import datetime

TOKEN = os.environ["PIXELA_TOKEN"]
USERNAME = "uwazajzatoba"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

## We've already created a user, so there's no need for it to be active anymore.
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
header = {'X-USER-TOKEN': TOKEN}
create_params = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "int",
    "color": "shibafu",
}

## If you want to create another graph you can simply change create_params, and uncomment 2 lines below:
# response = requests.post(url=graph_endpoint, json=create_params, headers=header)
# print(response.text)

edit_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
put_params = {
    "unit": "Hours",
}
## I just wanted to see how updating a graph works by changing units. Comment lines below to try that:
# response = requests.put(url=edit_endpoint, json=put_params, headers=header)
# print(response.text)

date = datetime.datetime.now()
# date = datetime.datetime(year=2023, month=9, day=17) ## Uncomment, and edit if you want to post data not from today.
date = date.strftime("%Y%m%d")

post_params = {
    "date": date,
    "quantity": input("How many hours did you code today?"),
}

## Uncomment those lines to post today's progress:
# response = requests.post(url=edit_endpoint, json=post_params, headers=header)
# print(response.text)

## You can edit a pixel using these lines (don't forget to edit date):
# update_endpoint = f"{edit_endpoint}/{date}"
#
# update_params = {
#     "quantity": "5",
# }
#
# response = requests.put(url=update_endpoint, json=update_params, headers=header)
# print(response.text)

## You can delete a pixel using these lines:
# response = requests.delete(url=update_endpoint, headers=header)
# print(response.text)
