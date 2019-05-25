import pandas as pd

# pandas에서 companyInfo.json을 df로 불러와 보세요.
# df 데이터 프레임 = 표

df = pd.read_json("companyInfo.json")

print(df.head(10))

dfFiltered = df[df['name'].str.contains("현대")]
print(dfFiltered.count())

dfFiltered.to_excel("contain현대.xlsx")
