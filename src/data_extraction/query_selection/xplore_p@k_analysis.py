import json
from functools import reduce

with open(
    "code_base/data_extraction/query_selection/xplore_p@k_evaluated.json", "r"
) as f:
    data = json.load(f)

for query in data:
    print(query)
    for cp in data[query]:
        val = reduce(lambda x, y: x + y["eval"], data[query][cp], 0)
        print(cp + ": " + str(val))
    print("\n")
