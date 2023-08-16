# enrich the extracted documents with the publishing date
# follow each link and scrape the information from the publication's page

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from tqdm import tqdm

counter = 0

def getDate(link):
    date = None
    
    global counter
    if counter % 5 == 0:
        result.to_csv("./data/filtered/xplore_with_date.csv", index=False)

    driver.get(link)

    try: 
        div = driver.find_element(By.CLASS_NAME, "doc-abstract-confdate")
        text = div.text
        date = text.replace("Date of Conference: ", "")
    except NoSuchElementException:
        try:
            div = driver.find_element(By.CLASS_NAME, "doc-abstract-pubdate")
            text = div.text
            date = text.replace("Date of Publication: ", "")
        except NoSuchElementException:
            pass

    counter = counter+1
    return date

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

df = pd.read_csv("./data/filtered/xplore.csv")
current_state = pd.read_csv("./data/filtered/xplore_with_date.csv")
result = pd.DataFrame(columns = ['date', 'title', 'link', 'abstract'])

for index, row in tqdm(df.iterrows()):
    if index >= len(current_state):
        date = getDate(row['link'])
        row['date'] = date
    else:
        row['date'] = current_state.iloc[index]['date']
    result.loc[len(result)] = row

result.to_csv("./data/filtered/xplore_with_date.csv", index=False)

driver.close()
