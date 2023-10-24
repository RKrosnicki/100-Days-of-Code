import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
# print(response.text)
webpage = response.text
soup = BeautifulSoup(webpage, 'html.parser')
# print(soup.prettify())

all_sections = soup.find_all(name="section")
# print(all_sections)
section_headings = soup.find_all(name="h3", class_="title")
# print(section_headings)
titles_list = []
for title in section_headings:
    # print(title.getText())
    titles_list.append(str(title.getText()))

titles_list = titles_list[::-1]
# print(titles_list)

with open("movies_list.txt", "w", encoding="utf-8") as file:
    for i in titles_list:
        file.write(f"{i}\n")
