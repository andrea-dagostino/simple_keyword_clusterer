# Simple Keyword Clusterer
A simple machine learning package to cluster keywords in higher-level groups.

Example:<br>
*"Senior Frontend Engineer" --> "Frontend Engineer"*<br>
*"Junior Backend developer" --> "Backend developer"*
___
## Installation
```
pip install simple_keyword_clusterer
```
## Usage
```python
# import the package
from simple_keyword_clusterer import Clusterer

# read your keywords in list
with open("../my_keywords.txt", "r") as f:
    data = f.read().splitlines()

# instantiate object
clusterer = Clusterer()

# apply clustering
df = clusterer.extract(data)

print(df)
```
<img src="https://github.com/Tangelus/simple_keyword_clusterer/raw/master/images/clustering_sample.png" alt="clustering_example" width="600"/>


## Performance
The algorithm will find the optimal number of clusters automatically based on the best Silhouette Score.

You can specify the number of clusters yourself too

```python
# instantiate object
clusterer = Clusterer(n_clusters=4)

# apply clustering
df = clusterer.extract(data)
```

For best performance, try to reduce the variance of data by providing the same semantic context <br>
(the *job title* keywords file should remain coherent, in that it shouldn't contain other stuff like *gardening* keywords). <br>

If items are clearly separable, the algorithm should still be able to provide a useable output.

## Customization
You can customize the clustering mechanism through the files 
- blacklist.txt
- to_normalize.txt

If you notice that the clustering identifies unwanted groups, you can blacklist certain words simply by appending them in the blacklist.txt file.

The to_normalize.txt file contains tuples that identify a transformation to apply to the keyword. For instance
```
("back end", "backend), ("front end", "frontend), ("sr", "Senior"), ("jr", "junior")
```
Simply add your tuples to use this functionality.


## Dependencies
- Scikit-learn
- Pandas
- Matplotlib
- Seaborn
- Numpy
- NLTK
- Tqdm

Make sure to download NLTK English Stopwords with the command

```python
nltk.download("stopwords")
```

## Contact
If you feel like contacting me, do so and send me a mail. You can find my contact information on my [website](https://andreadagostino.com).
