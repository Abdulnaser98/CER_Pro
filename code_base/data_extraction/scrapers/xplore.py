import requests
import json
from bs4 import BeautifulSoup
from tqdm import tqdm
import math

search_term = """
    (("All Metadata":artificial intelligence) OR ("All Metadata":AI)) 
    AND (("All Metadata":sustainable) OR ("All Metadata":sustainability)) 
    AND ("All Metadata":energy)"""
ranges = ["2004_2023_Year"]
refinements = ["ContentType:Conferences", "ContentType:Journals"]

headers = {
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://ieeexplore.ieee.org",
    "Content-Type": "application/json",
}

# fake user agent
headers_doc = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

with open("code_base/data_extraction/raw_data/xplore.json", "w") as f:
    json.dump([], f)

page_no = 1
while True:
    payload = {
        "newsearch": True,
        "queryText": search_term,
        "highlight": True,
        "returnFacets": ["ALL"],
        "returnType": "SEARCH",
        "rowsPerPage": 100,
        "pageNumber": page_no,
        "ranges": ranges,
        "refinements": refinements,
    }
    r = requests.post(
        "https://ieeexplore.ieee.org/rest/search", json=payload, headers=headers
    )
    page_data = r.json()

    if page_data["startRecord"] > page_data["totalRecords"]:
        break

    output = []
    pbar = tqdm(page_data["records"])
    for record in pbar:
        pbar.set_description(
            "Processing page "
            + str(page_no)
            + " out of "
            + str(math.ceil(page_data["totalRecords"] / 100))
        )
        if not "documentLink" in record:
            continue
        link = "https://ieeexplore.ieee.org" + record["documentLink"]

        page = requests.get(link, headers=headers_doc)

        soup = BeautifulSoup(page.content, "html.parser")
        div = soup.find("meta", property="og:description")
        if not div:
            continue
        abstract = div.get("content", None)

        output.append(
            {
                "title": record["articleTitle"],
                "link": link,
                "abstract": abstract,
            }
        )
    with open("code_base/data_extraction/raw_data/xplore.json", "r") as f:
        current_arr = json.load(f)

    new_arr = current_arr + output

    with open("code_base/data_extraction/raw_data/xplore.json", "w") as f:
        json.dump(new_arr, f)

    page_no += 1
