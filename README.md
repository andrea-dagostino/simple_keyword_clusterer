# Simple Keyword Clusterer
A simple, machine learning package to cluster keywords in higher-level groups.

Example:<br>
*"Senior Frontend Engineer" --> "Frontend Engineer"*
*"Junior Backend developer" --> "Backend developer"*
___

## Usage
```python
# import the package
from simple_keyword_clusterer import Clusterer

# read your keywords in list
with open("../my_keywords.txt", "r") as f:
    data = f.read().splitlines()

# instantiate object
clusterer = Clusterer()

#apply clustering
df = clusterer.extract(data)

print(df)
```

