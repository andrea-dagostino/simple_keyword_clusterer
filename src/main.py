from . import preprocessing
from . import clustering


class Extractor:

    def __call__(self, corpus) -> None:
        cleaned = [
            preprocessing.sanitize_text(item, remove_stopwords=True) for item in corpus
        ]
        cleaned = [preprocessing.normalize_role(item) for item in cleaned]
        output = clustering.make_clusters(cleaned)
        return output