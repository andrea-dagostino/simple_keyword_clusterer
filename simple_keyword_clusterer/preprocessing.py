import re
import nltk
from nltk.corpus import stopwords

STOPWORDS = list(set(stopwords.words("english")))
with open("./src/blacklist.txt", "r", encoding="utf-8") as f:
    to_remove = f.read().splitlines()
STOPWORDS.extend(to_remove)


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
    with open("./src/to_normalize.txt", "r", encoding="utf-8") as f:
        roles_to_normalize = f.read().splitlines()
        roles_to_normalize = [eval(x) for x in roles_to_normalize]

    for wrong, right in roles_to_normalize:
        if wrong in text:
            return right + " " + text[len(wrong) + 1 :]
        else:
            return text
