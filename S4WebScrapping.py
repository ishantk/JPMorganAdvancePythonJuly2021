import requests
from bs4 import BeautifulSoup

url = "https://www.espncricinfo.com/series/ipl-2021-1249214/points-table-standings"
response = requests.get(url)
print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())
team_name_tags = soup.find_all("h5", class_="header-title label")
for tag in team_name_tags:
    print(tag.text.strip())