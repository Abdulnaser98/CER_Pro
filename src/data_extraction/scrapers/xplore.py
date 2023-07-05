import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import math
import csv

search_terms = [
    """
    (("All Metadata":artificial intelligence) OR ("All Metadata":AI)) 
    AND (("All Metadata":sustainable) OR ("All Metadata":sustainability)) 
    AND ("All Metadata":energy)""",
    """(("All Metadata":artificial intelligence) OR ("All Metadata":AI)) 
    AND (("All Metadata":sustainable) OR ("All Metadata":sustainability)) 
    AND (("All Metadata":energy sector) OR ("All Metadata":energy industry))""",
    """
    (("All Metadata":artificial intelligence) OR ("All Metadata":AI)) 
    AND (("All Metadata":sustainable) OR ("All Metadata":sustainability) OR ("All Metadata":renewable)) 
    AND ("All Metadata":energy)""",
    """
    (("All Metadata":artificial intelligence) OR ("All Metadata":AI)) 
    AND (("All Metadata":sustainable) OR ("All Metadata":sustainability))""",
]
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

keys = {"date": None, "abstract": None, "title": None, "link": None}

for query in range(len(search_terms)):
    with open(
        "code_base/data_extraction/raw_data/xplore_" + str(query) + ".csv",
        "w",
        newline="",
    ) as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()

    page_no = 1
    while True:
        payload = {
            "newsearch": True,
            "queryText": search_terms[query],
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
                "Query "
                + str(query)
                + ": "
                + "Processing page "
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
            abstract = div.get("content", None).replace("\n", "")

            output.append(
                {
                    "date": "None",
                    "abstract": abstract,
                    "title": record["articleTitle"],
                    "link": link,
                }
            )

        if len(output) == 0:
            continue
        keys = output[0].keys()

        with open(
            "code_base/data_extraction/raw_data/xplore_" + str(query) + ".csv",
            "a",
            newline="",
        ) as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writerows(output)

        page_no += 1
