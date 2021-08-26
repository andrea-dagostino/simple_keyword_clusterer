import preprocessing
import clustering


class Clusterer:
    def __init__(self, n_clusters=None) -> None:
        self.n_clusters = n_clusters

    def extract(self, corpus) -> None:
        cleaned = [
            preprocessing.sanitize_text(item, remove_stopwords=True) for item in corpus
        ]
        cleaned = [preprocessing.normalize_role(item) for item in cleaned]
        output = clustering.make_clusters(cleaned, self.n_clusters)
        return output