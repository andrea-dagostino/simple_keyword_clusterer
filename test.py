import pandas as pd
from src.main import Extractor

with open('./prototyping/engineer.txt', 'r', encoding='utf-8') as f:
    data = f.read().splitlines()

e = Extractor(data)
print(e())