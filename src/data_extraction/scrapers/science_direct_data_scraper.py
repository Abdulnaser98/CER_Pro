"""
The objective of this python file is tp scrape data from the "ScienceDirect"
website regarding the topic of Artificial Intelligence for Sustainability in the Energy
Industry. Once the data is scraped, it should be evaluated to determine how many of the
scraped papers contain the three specified keywords in their abstract: "Artifical Intelligence" or
"AI" , "sustainable" or "sustainability," and "energy".
"""
import time
import pandas as pd
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager




# get the chrome driver for the ScienceDirect website
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

# Path to the raw data folder
path_to_raw_data_folder = "/Users/abdulnaser/Desktop/CER_Pro/code_base/data_extraction/raw_data/"

# Path to the folder , where the links that were extracted from the website are saved
path_to_article_links_folder = "./code_base/data_extraction/papers_links"


# data of the papers
dates = []
titles = []
abstracts = []
introductions = []


def extract_links():
    print("Extracting the links from the science direct website: ")
    offset = 0
    offset_str = ""
    paper_links_temp = []
    url = "https://www.sciencedirect.com/search?qs=%28%22artificial%20intelligence%22%20OR%20%22AI%22%29%20AND%20%28%22sustainable%22%20OR%20%22sustainability%22%29%20AND%20%22energy%22&years=2004%2C2005%2C2006%2C2007%2C2009%2C2008%2C2010%2C2011%2C2012%2C2013%2C2014%2C2015%2C2016%2C2017%2C2018%2C2019%2C2020%2C2021&show=100&lastSelectedFacet=articleTypes&articleTypes=FLA"
    for _ in range(60):
        driver.get(url + offset_str)
        time.sleep(10)
        papers_links = driver.find_elements("xpath", "//div[@id='srp-results-list']//li//div[@class='result-item-content']//h2//a[@href]")
        for link in papers_links:
            paper_links_temp.append(link.get_attribute("href"))
        offset = offset + 100
        offset_str = "&offset=" + str(offset)

    df = pd.DataFrame(paper_links_temp , columns = ['link'])
    print("The links are successfually extracted!!!")
    df.to_csv("./papers_links/sciencedirect_papers_links.csv")



def extract_papers_data():
    print("Extracting the papers data:")
    data = pd.read_csv("/Users/abdulnaser/Desktop/CER_Pro/code_base/data_extraction/raw_data/sciencedirect_papers_links.csv")
    dates = []
    abstracts = []
    titles = []

    # Use tqdm to track the progress of the loop
    for link in tqdm(data['link'].tolist()[200:250], desc="Progress", unit="link", total=len(data['link'].tolist()[200:300])):
        try:
            driver.get(link)
            time.sleep(3)
            date = extract_date()
            abstract = extract_abstract()
            title = extract_title()

            # Append the data
            dates.append(date)
            abstracts.append(abstract)
            titles.append(title)

        except Exception as e:
            print(f"An error occurred for link: {link}")
            print(f"Error message: {str(e)}")

    data = {'date': dates, 'abstract': abstracts, 'title': titles}
    df = pd.DataFrame(data)
    df.to_csv("/Users/abdulnaser/Desktop/CER_Pro/code_base/data_extraction/raw_data/sciencedirect_papers_data_uncleaned_new_200_300.csv", index=False)



def extract_title():
    title = driver.find_element("xpath","//span[@class='title-text']").text
    return title

def extract_date():
    date = driver.find_element("xpath","//div[@class='text-xs']").text
    return date


def extract_abstract():
    abstract = driver.find_element("xpath", "//div[@id='abstracts']//div[@class='abstract author']//p").text
    return abstract


if __name__ == "__main__":
    #extract_links()
    extract_papers_data()






