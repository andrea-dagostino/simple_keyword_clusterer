from src.job_title_extractor import Extractor

with open('./src/data/jobs.txt', 'r', encoding='utf-8') as f:
    data = f.read().splitlines()

extractor = Extractor(n_clusters=None)
df = extractor.extract(data)

print(df)