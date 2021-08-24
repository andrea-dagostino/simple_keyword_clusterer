import pandas as pd
from src.main import Extractor

# with open('./prototyping/marketing.txt', 'r', encoding='utf-8') as f:
#     data = f.read().splitlines()

data = pd.read_excel("./prototyping/kwset.xlsx")
data = list(data.keyword)

extractor = Extractor(n_clusters=None)
df = extractor.extract(data[:20])

# df.to_csv("output.csv", sep=";", encoding="utf-8")