# import smtplib
#
# hotmail_SMTP = "smtp.live.com"
# my_email = "p97909805@gmail.com"
# password = "uqtflyxjddanvnin"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="pythonrrrrr@hotmail.com",
#         msg="Subject: Hello\n\nThis is te body of my email."
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# weekday = now.weekday()
# month = now.month
# year = now.year
#
# date_of_birt = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birt)

import datetime as dt
import random
import smtplib

MY_EMAIL = "p97909805@gmail.com"
MY_PASSWORD = "uqtflyxjddanvnin"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt", "r") as quotes:
        quotes_list = quotes.readlines()
        chosen_quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="pythonrrrrr@hotmail.com",
            msg=f"Subject: Monday quote\n\n{chosen_quote}"
        )


