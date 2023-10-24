from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/newest")
# print(response.text)
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, 'html.parser')

art_score = soup.find_all(name="span", class_="score")
art_tag = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
article_upvotes = []

for i in range(len(art_tag)):
    article_texts.append(art_tag[i].get_text())
    article_links.append(art_tag[i].a.get("href"))
    article_upvotes.append(int(art_score[i].getText().split()[0]))

print(article_texts)
print(article_links)
print(article_upvotes)
highest_upvote = max(article_upvotes)
max_index = article_upvotes.index(highest_upvote)
print(article_texts[max_index])
print(article_links[max_index])















# with open("website.html") as file:
#     contents = file.read()
#     # print(contents)
#
# # soup = BeautifulSoup(contents, 'html.parser')
# soup = BeautifulSoup(contents, 'lxml')
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup)
# # print(soup.prettify())
# # print(soup.a)
# all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.get_text())
# print(section_heading.name)
# print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(selector=".heading")
# print(headings)
