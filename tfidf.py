import nltk
from nltk.corpus import stopwords
from collections import defaultdict
import math
import os

def display(vocab, tfidfs):
    for term in vocab:
        temp = [tfidf.get(term, 0) for tfidf in tfidfs]
        print(f"{term}: {temp}")

def stopword_removal(filename, folder):
    stopword_set = set(stopwords.words("english"))
    file_path = os.path.join(folder, filename)

    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: {filename} not found!")
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
        data = " ".join(char for char in text if char.isalnum() or char.isspace())

    tokens = data.lower().split()
    tokens = [token for token in tokens if token not in stopword_set]
    return tokens

def get_tf(tokens):
    tf = defaultdict(int)
    for token in tokens:
        tf[token] += 1
    return tf

def get_idf(doc_tokens, n):
    df = defaultdict(int)
    for document in doc_tokens:
        for token in set(document): 
            df[token] += 1  # ✅ Fixed missing increment

    idf = {}  
    for token, count in df.items(): 
        idf[token] = round(math.log10(n / count), 2)  # ✅ Fixed missing variable
    return idf

def get_tf_idf(tf, idf):
    tfidf = {}
    for term, term_freq in tf.items():
        tfidf[term] = term_freq * idf.get(term, 0)
    return tfidf

def main():
    corpus_size = 4
    num_docs = 3
    folder = "corpus2"

    docs = [f"file{i}.txt" for i in range(1, num_docs + 1)]

    # Check if files exist
    for doc in docs:
        if not os.path.exists(os.path.join(folder, doc)):
            print(f"Error: {doc} not found!")
            return  # Exit early if files are missing

    all_tokens = [stopword_removal(doc, folder) for doc in docs]
    print("Checkpoint 1: Tokenization Done")

    tfs = [get_tf(tokens) for tokens in all_tokens]  # ✅ Fixed incorrect variable name
    idfs = get_idf(all_tokens, corpus_size)
    tfidfs = [get_tf_idf(tf, idfs) for tf in tfs]  # ✅ Fixed incorrect function call

    print("Checkpoint 2: TF-IDF Computed")

    vocabulary = set()
    for tfidf in tfidfs:
        vocabulary.update(tfidf.keys())
    vocabulary = list(vocabulary)

    display(vocabulary, tfidfs)

    weights = []  # ✅ Fixed incorrect variable name
    for tfidf in tfidfs:
        weights.append(round(sum(tfidf.values()), 2))  # ✅ Corrected append statement

    for doc, weight in zip(docs, weights):
        print(f"{doc}: {weight}")

if __name__ == "__main__":
    main()
