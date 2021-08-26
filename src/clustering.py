from sklearn import feature_extraction
from sklearn import metrics
from sklearn import cluster
from sklearn import decomposition

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from tqdm import tqdm


def find_elbow(X):
    range_n_clusters = range(2, 20)  # clusters range you want to select
    best_clusters = 0  # best cluster number which you will get
    previous_silh_avg = 0.0

    for n_clusters in tqdm(range_n_clusters, desc="Finding clusters..."):
        clusterer = cluster.KMeans(n_clusters=n_clusters)
        cluster_labels = clusterer.fit_predict(X)
        silhouette_avg = metrics.silhouette_score(X, cluster_labels)
        if silhouette_avg > previous_silh_avg:
            previous_silh_avg = silhouette_avg
            best_clusters = n_clusters
    return best_clusters


def make_clusters(raw_data, n_clusters=None):

    vectorizer = feature_extraction.text.TfidfVectorizer(
        ngram_range=(2, 3),
        max_features=100,
        max_df=0.5,
        smooth_idf=True,
        sublinear_tf=True,
        norm="l1",
    )

    X = vectorizer.fit_transform(raw_data).toarray()
    voc = vectorizer.get_feature_names()

    if n_clusters != None:
        n_clusters = n_clusters
    else:
        n_clusters = find_elbow(X)

    print(f"Found number of optimal clusters: {n_clusters}")

    clusterer = cluster.KMeans(n_clusters=n_clusters, random_state=42).fit(X)
    clusters = clusterer.predict(X)

    decomposer = decomposition.PCA(n_components=2, random_state=42)
    reduced = decomposer.fit_transform(X)

    centers = decomposer.transform(clusterer.cluster_centers_)

    component_1, component_2 = reduced[:, 0], reduced[:, 1]
    df = pd.concat(
        [
            pd.Series(component_1, name="PCA1"),
            pd.Series(component_2, name="PCA2"),
            pd.Series(clusters, name="cluster"),
        ],
        axis=1,
    )

    order_centroids = clusterer.cluster_centers_.argsort()[:, ::-1]
    kws = []
    for i in range(len(centers)):
        for ind in order_centroids[i, :1]:
            kws.append(voc[ind])

    df["cluster"] = df["cluster"].map({key: value for (key, value) in enumerate(kws)})
    df["input"] = raw_data


    plt.figure(figsize=(10, 8))
    sns.scatterplot(
        data=df, x="PCA1", y="PCA2", hue="cluster", palette="coolwarm", s=100
    )
    plt.title(f"Num items {len(raw_data)}, Ideal num. clusters: {n_clusters}", fontsize=18)
    plt.legend(fontsize=10, title="Clusters")
    plt.show()

    return df[["input", "cluster"]]
