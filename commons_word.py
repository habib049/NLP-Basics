import nltk
from nltk.book import text7

# this code is used to download the nltk modules
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('book')
nltk.download("punkt")

# finding 50 most frequent words
words_tokens = text7.tokens
clean_corpus = nltk.Text([word.lower() for word in words_tokens if word.isalnum()])
words_frequency = nltk.FreqDist(clean_corpus)
most_50_common = (words_frequency.most_common(50))

print("\nMost common words are : ",most_50_common)



