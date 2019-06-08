import pandas as pd

df = pd.read_json("./result.json")


dfSorted = df.sort_values(['price'], ascending=[0])
print(dfSorted)
