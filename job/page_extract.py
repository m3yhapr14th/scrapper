import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=842ba3860fb8aa0c")
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
pagination = indeed_soup.find("div", {"class":"pagination"})
pages = pagination.find_all('a')
spans = []

#print(indeed_soup.prettify())
#print(pagination)
for link in pages[:-1]:
    spans.append(int(link.string))

max_page = spans[-1]
