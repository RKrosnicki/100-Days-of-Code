import smtplib

hotmail_SMTP = "smtp.live.com"
my_email = "p97909805@gmail.com"
password = "uqtflyxjddanvnin"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="pythonrrrrr@hotmail.com", msg="Hello")
connection.close()
