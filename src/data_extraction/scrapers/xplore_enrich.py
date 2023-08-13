# enrich the extracted documents with the publishing date
# follow each link and scrape the information from the publication's page

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# import requests
# from bs4 import BeautifulSoup

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")

# homedir = os.path.expanduser("~")
webdriver_service = Service("./chromedriver/stable/chromedriver")

# Choose Chrome Browser
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)


def getDate(link):
    date = ""

    browser.get(link)
    div = browser.find_elements_by_class_name("doc-abstract-confdate")
    browser.close()

    return date


df = pd.read_csv("./data/filtered/xplore.csv")[:1]
df["date"] = df.apply(lambda row: getDate(row["link"]), axis=1)

print(df)
