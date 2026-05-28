"""Reusable text preprocessing helpers for the Australian Election tweets project."""

import re
from typing import Iterable, Set

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


CUSTOM_STOPWORDS: Set[str] = {
    "amp", "abc", "ausvotes", "auspol", "auspol2019", "ausvotes2019",
    "ausvotes19", "ausvote19", "australiavotes", "australiavotes2019",
    "7news", "election2019results", "election", "qldpol", "australia",
    "australian", "via", "u", "lnp", "would", "tony", "clive", "2019",
    "auspol19", "election2019", "australiadecides", "rt",
}


def ensure_nltk_resources() -> None:
    """Download required NLTK resources if they are not already available."""
    for package in ["punkt", "stopwords", "wordnet", "averaged_perceptron_tagger"]:
        nltk.download(package, quiet=True)


def process_text(text: str, extra_stopwords: Iterable[str] | None = None) -> str:
    """Clean tweet text for NLP analysis.

    Steps:
    1. Lowercase text
    2. Remove links, mentions, and noisy encoding artifacts
    3. Tokenize
    4. Remove stopwords and non-alphabetic tokens
    5. Lemmatize
    6. Rejoin tokens into a clean string
    """
    if not isinstance(text, str) or not text.strip():
        return ""

    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english")) | CUSTOM_STOPWORDS
    if extra_stopwords:
        stop_words |= set(extra_stopwords)

    text = text.lower()
    text = re.sub(r"http\S+|www\S+", " ", text)
    text = re.sub(r"@\w+", " ", text)
    text = re.sub(r"[^a-zA-Z#\s]", " ", text)

    tokens = word_tokenize(text)
    cleaned_tokens = [
        lemmatizer.lemmatize(token)
        for token in tokens
        if token.isalpha() and token not in stop_words and len(token) > 1
    ]

    return " ".join(cleaned_tokens)
