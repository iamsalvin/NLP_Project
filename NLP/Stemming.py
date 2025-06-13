# Stemming Example
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

text = ("A serious environmental threat looms over the Arabian Sea off the Kerala "
        "coast due to a fire aboard the Singapore-flagged vessel MV Wan Hai 503, "
        "which is carrying a large quantity of hazardous chemicals.")

stemmer = PorterStemmer()
tokens = word_tokenize(text)
filtered = [word for word in tokens if word.isalpha()]
stemmed = [stemmer.stem(word.lower()) for word in filtered]
print("Stemmed words:", stemmed)
