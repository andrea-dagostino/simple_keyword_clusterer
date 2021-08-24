from . import preprocessing
from . import clustering


class Extractor:
    def __init__(self, corpus) -> None:
        self.X = corpus

    def __call__(self) -> None:
        cleaned = [
            preprocessing.sanitize_text(item, remove_stopwords=True) for item in self.X
        ]
        cleaned = [preprocessing.normalize_role(item) for item in cleaned]
        output = clustering.make_clusters(cleaned)
        return output