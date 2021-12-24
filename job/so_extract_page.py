import requests
from bs4 import BeautifulSoup

so_get = requests.get("https://stackoverflow.com/jobs?q=python")
soup_get = BeautifulSoup(so_get.text, "html.parser")
pagin = soup_get.find("div", {"class":"s-pagination"})
pages = pagin.find_all("a")
span = []

#print(soup_get.prettify())
for x in pages:
    span.append(x.find("span"))

print(span[:-1])