import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

MY_EMAIL = "p97909805@gmail.com"
MY_PASSWORD = "uqtflyxjddanvnin"
TARGET_PRICE = 150

URL = "https://www.amazon.com/OnePlus-Buds-Audiophile-Grade-Best-Class/dp/B0BQ967JL7/ref=sr_1_2_sspa?crid=14HLK0A2KZCYL&keywords=oneplus%2B12&qid=1704200134&sprefix=oneplus%2B12%2Caps%2C181&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
header = {
    "upgrade-insecure-requests": '1',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    "sec-fetch-site": 'cross-site',
    "sec-fetch-mode": 'navigate',
    "sec-fetch-user": '?1',
    "sec-fetch-dest": 'document',
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": '?0',
    "sec-ch-ua-platform": "Windows",
    "Accept-Encoding": 'gzip, deflate, br',
    "Accept-Language": 'pl-PL,pl;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    "Cookie": 'PHPSESSID=18c80355e071c87e9e376a3b01941b6c; _ga=GA1.2.2066525678.1703944167; _gid=GA1.2.1214863669.1704196681; _ga_VL41109FEB=GS1.2.1704196680.2.0.1704196680.0.0.0',
    "x-forwarded-proto": 'https',
    "x-https": 'on',
    "X-Forwarded-For": '87.205.135.169'
}

response = requests.get(url=URL, headers=header)
soup = BeautifulSoup(response.content, 'lxml')
print(soup)

price_whole = soup.find(class_="a-price-whole")
price_whole = int(price_whole.getText().strip('.'))

price_fraction = soup.find(class_="a-price-fraction")
price_fraction = int(price_fraction.getText())

price = price_whole + price_fraction/100
print(f"${price}")

name = soup.find(id="productTitle")
name = name.getText()

if price < TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Alert promocyjny!  \n\nObecna cena {name.strip()}:\n${price}\nWejdz na: {URL}"
        )
