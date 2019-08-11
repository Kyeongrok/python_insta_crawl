import pandas as pd
from libs.singleExcelSaver import save

df = pd.read_json("./result.json")

save(df, "hello.xlsx")
