import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
webpage = response.text
soup = BeautifulSoup(webpage, 'html.parser')

all_sections = soup.find_all(name="section")
section_headings = soup.find_all(name="h3", class_="title")
titles_list = [title.getText() for title in section_headings]
titles_list = titles_list[::-1]

with open("movies_list.txt", "w", encoding="utf-8") as file:
    for i in titles_list:
        file.write(f"{i}\n")
