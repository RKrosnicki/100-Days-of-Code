# Automated on pythonanywhere.com

import datetime as dt
import csv
import random
import smtplib

MY_EMAIL = "p97909805@gmail.com"
MY_PASSWORD = "uqtflyxjddanvnin"

today = dt.datetime.now()
letters_list = ["letter_templates\letter_1.txt", "letter_templates\letter_2.txt", "letter_templates\letter_3.txt"]

with open("birthdays.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row["month"]) == today.month and int(row["day"]) == today.day:
            random_letter = random.choice(letters_list)
            with open(random_letter, "r") as data:
                letter = data.read()
                letter = letter.replace("[NAME]", row["name"])
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=row["email"],
                    msg=f"Subject: Happy Birthday, {row['name']}!\n\n{letter}"
                )
