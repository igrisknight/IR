from nltk.stem import PorterStemmer
nltk.download('punnkt')

# Instantiate the PorterStemmer
stemmer = PorterStemmer()

# List of words to stem
words = ["running", "runner", "easily", "fairly", "cats", "happiness", "studies", "stemmer"]

# Stem each word and print the result
for word in words:
    print(f"Original: {word} -> Stemmed: {stemmer.stem(word)}")
