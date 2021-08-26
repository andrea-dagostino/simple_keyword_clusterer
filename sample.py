from src.main import Extractor

with open('./data/jobs.txt', 'r', encoding='utf-8') as f:
    data = f.read().splitlines()

extractor = Extractor(n_clusters=None)
df = extractor.extract(data)

print(df)