import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 52.229675 # Your latitude goes here
MY_LNG = 21.012230 # Your longitude goes here
MY_EMAIL = "p97909805@gmail.com"
MY_PASSWORD = "uqtflyxjddanvnin"

def iss_is_above():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    data = iss_response.json()
    iss_lng = float(data['iss_position']['longitude'])
    iss_lat = float(data['iss_position']['latitude'])

    if (MY_LAT - 5) < iss_lat < (MY_LAT + 5) and (MY_LNG - 5) < iss_lng < (MY_LNG + 5):
        return True
    else:
        return False

def send_look_up():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look up!\n\nLook up!\nISS is above you!"
        )

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted" : 0,
    }
    sunrise_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

    sunrise_response.raise_for_status()
    data_sunrise = sunrise_response.json()
    sunrise = int(data_sunrise['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data_sunrise['results']['sunset'].split("T")[1].split(":")[0])
    time_now = datetime.utcnow().hour

    if sunrise <= time_now <= sunset:
        return False
    else:
        return True

def sky_is_clear():
    weather_response = requests.get(url=f"http://api.weatherapi.com/v1/current.json?key=e53dc32be220486cb92182455230609&q={MY_LAT}, {MY_LNG}&aqi=no")
    weather_data = weather_response.json()['current']['cloud']
    if weather_data == 0:
        return True
    else:
        return False

while True:
    if is_night() and iss_is_above() and sky_is_clear():
        send_look_up()
    else:
        print("HOLD !!!")
    sky_is_clear()
    time.sleep(60)
