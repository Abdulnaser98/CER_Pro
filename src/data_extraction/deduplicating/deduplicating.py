import pandas as pd
from itertools import combinations
import tqdm
import json

xplore = pd.read_csv("./data/filtered/xplore.csv")
acm = pd.read_csv("./data/filtered/filtered_acm_data.csv")
science_direct = pd.read_csv("./data/filtered/science_direct_filtered_data.csv")

# create uniform columns
xplore = xplore.drop(["link", "date"], axis=1)
acm = acm.drop(["link", "datum"], axis=1)
science_direct = science_direct.drop(["Unnamed: 0", "month", "year"], axis=1)

# concatenate dataframes
data_concat = pd.concat([xplore, acm, science_direct])

print(data_concat.info())

# excat duplicates
duplicate_rows_exact = data_concat[data_concat.duplicated()]
print(duplicate_rows_exact)  # 2

# title duplicates
duplicate_rows_title = data_concat[data_concat.duplicated(["title"])]
print(duplicate_rows_title)  # 3


def distance_matrix(s1, s2):
    res = [[i for i in range(len(s1) + 1)]]
    for i in range(1, len(s2) + 1):
        res.append([i if j == 0 else None for j in range(len(s1) + 1)])

    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            case_1 = (
                res[i - 1][j - 1] if s1[j - 1] == s2[i - 1] else res[i - 1][j - 1] + 1
            )
            case_2 = res[i][j - 1] + 1
            case_3 = res[i - 1][j] + 1
            res[i][j] = min(case_1, case_2, case_3)

    return res


def levenshtein_similarity(s1, s2):
    if (len(s1) == 0) or (len(s2) == 0):
        return 0.0
    elif s1 == s2:
        return 1.0

    edit_dist = 0

    m = distance_matrix(s1, s2)
    edit_dist = m[len(s2)][len(s1)]
    edit_sim = 1 - edit_dist / max(len(s1), len(s2))

    assert 0.0 <= edit_sim <= 1.0

    return edit_sim


record_combinations = list(combinations(data_concat["title"], 2))

matches = [
    {"pair": s, "sim": levenshtein_similarity(*s)}
    for s in tqdm.tqdm(record_combinations)
    if levenshtein_similarity(*s) > 0.7
]

with open("./data/concatenated/matches.json", "w") as f:
    json.dump(matches, f)  # keine matches über 0.7 außer exact

data_concat = data_concat.drop_duplicates(subset=["title"])

data_concat.to_csv("./data/concatenated/concat_dedup.csv", index=False)
