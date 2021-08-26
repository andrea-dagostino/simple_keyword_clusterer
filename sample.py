from simple_keyword_clusterer import Clusterer

with open('./sample_jobs.txt', 'r', encoding='utf-8') as f:
    data = f.read().splitlines()

extractor = Clusterer(n_clusters=6)
df = extractor.extract(data)

print(df)