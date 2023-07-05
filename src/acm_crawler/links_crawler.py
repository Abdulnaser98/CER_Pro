import pandas as pd
import requests
from bs4 import BeautifulSoup

links = []
titles = []

for i in range(0, 2):
    print(f"Page {i}")

    # URL
    url = f"https://dl.acm.org/action/doSearch?fillQuickSearch=false&target=advanced&ContentItemType=research-article&expand=all&AfterYear=2004&BeforeYear=2022&AllField=Abstract%3A%28%28artificial+intelligence+OR+%22ai%22%29+AND+%28sustainable+OR+sustainability%29+AND+energy%29+OR+Title%3A%28%28artificial+intelligence+OR+%22ai%22%29+AND+%28sustainable+OR+sustainability%29+AND+energy%29+OR+Keyword%3A%28%28artificial+intelligence+OR+%22ai%22%29+AND+%28sustainable+OR+sustainability%29+AND+energy%29&startPage={i}&pageSize=100"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Find class
    titel = soup.find_all(class_="hlFld-Title")

    # Find all links in titel
    for link in titel:
        links.append(link.find("a")["href"])

    # Find title
    for title in titel:
        titles.append(title.find("a").get_text())

# Create dataframe from links and titles
df = pd.DataFrame({"title": titles, "link": links})

# Save dataframe to csv
df.to_csv("acm_links.csv", index=False)
