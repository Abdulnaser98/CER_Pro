import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

# read csv file
df = pd.read_csv("./src/data.csv")

# for each link in the dataframe, request the page and scrape the abstract
abstracts = []
for link in df["link"]:
    print(f"Getting abstract from {link}")
    link = "https://dl.acm.org" + link
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    abstract = soup.find(class_="abstractSection abstractInFull").get_text()
    abstracts.append(abstract)
    time.sleep(12)

# add abstracts to dataframe
df["abstract"] = abstracts

# save dataframe to csv
df.to_csv("data.csv", index=False)
