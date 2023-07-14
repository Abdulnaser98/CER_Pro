import pandas as pd
import re

xplore = pd.read_csv("./data/raw_data/filtered_xplore_2_data.csv")

CLEANR = re.compile("<.*?>")


def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, "", raw_html)
    return cleantext


xplore["cleaned_abstract"] = xplore.apply(
    lambda row: cleanhtml(row["abstract"]), axis=1
)

xplore = xplore.drop("abstract", axis=1)
xplore = xplore.rename(columns={"cleaned_abstract": "abstract"})

xplore.to_csv("./data/filtered/xplore.csv", index=False)
