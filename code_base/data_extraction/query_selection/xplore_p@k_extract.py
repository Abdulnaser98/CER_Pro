import json
import pandas as pd

checkpoints = [(1, 10), (21, 30), (51, 60), (101, 110)]

output = {}

for i in range(4):
    output["Query_" + str(i)] = {}
    for cp in checkpoints:
        # skip first 10 lines = skiprows=range(1, 11)
        df = pd.read_csv(
            "code_base/data_extraction/raw_data/xplore_" + str(i) + ".csv",
            skiprows=range(1, cp[0]),
            nrows=10,
        )

        abstracts = df.iloc[:, 1].tolist()
        titles = df.iloc[:, 2].tolist()

        docs = [
            {"title": elem[0], "abstract": elem[1], "eval": 99}
            for elem in zip(titles, abstracts)
        ]

        output["Query_" + str(i)][str(cp[0]) + "-" + str(cp[1])] = {}
        output["Query_" + str(i)][str(cp[0]) + "-" + str(cp[1])] = docs

with open("code_base/data_extraction/query_selection/xplore_p@k.json", "w") as f:
    json.dump(output, f)
