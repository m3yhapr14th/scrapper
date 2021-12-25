import requests
from bs4 import BeautifulSoup

cert_url = requests.get("https://www.krcert.or.kr/data/secNoticeList.do")
soup = BeautifulSoup(cert_url.text, "html.parser")
page_get = soup.find("div", {"class":"paging rwdP"})
table_get = soup.find("table", {"class":"basicList default"})

page = page_get.find_all("a")
title = table_get.find_all("a")
pval = []
tval = []

for a in page[0:-2]:
    pval.append(a.string)

print("Pages is ", 1, "~", pval[-2])

for b in title:
    tval.append(b.string)

print("##Security Title##")
for read in tval:
    print(read)
