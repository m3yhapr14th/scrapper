import requests
from bs4 import BeautifulSoup

job_url = requests.get("https://stackoverflow.com/jobs?q=python")
soup = BeautifulSoup(job_url.text, "html.parser")
div_get = soup.find("div", {"class":"listResults"})
title = div_get.find_all("a", {"class":"s-link stretched-link"})
val = []

for a in title:
    val.append(a.string)

print(val)