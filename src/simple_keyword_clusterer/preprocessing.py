import re
import nltk
from nltk.corpus import stopwords

import pkgutil


STOPWORDS = list(set(stopwords.words("english")))

to_remove = pkgutil.get_data(__package__, 'blacklist.txt').decode('utf8').splitlines()

STOPWORDS.extend(to_remove)

KEYWORDS_TO_NORMALIZE = pkgutil.get_data(__package__, 'to_normalize.txt').decode('utf8').splitlines()
KEYWORDS_TO_NORMALIZE = [eval(x) for x in KEYWORDS_TO_NORMALIZE]

def sanitize_text(text: str, remove_stopwords: bool) -> str:
    """This utility function sanitizes a string by:
    - removing links
    - removing special characters
    - removing numbers
    - removing stopwords
    - transforming in lowercase
    - removing excessive whitespaces

    Args:
        text (str): the input text you want to clean
        language (str): the language used to remove stopwords
        remove_stopwords (bool): whether or not to remove stopwords

    Returns:
        str: the cleaned text
    """

    # remove links
    text = re.sub(r"http\S+", "", text)
    # remove special chars and numbers
    text = re.sub("[^A-Za-z]+", " ", text)
    # remove stopwords
    if remove_stopwords:
        # 1. tokenize
        tokens = nltk.word_tokenize(text)
        # 2. check if stopword
        tokens = [w for w in tokens if not w.lower() in STOPWORDS]
        # 3. join back together
        text = " ".join(tokens)
    # return text in lower case and stripped of whitespaces
    text = text.lower().strip()
    return text


def normalize_role(text):
    for wrong, right in KEYWORDS_TO_NORMALIZE:
        if wrong in text:
            return right + " " + text[len(wrong) + 1 :]
        else:
            return text
