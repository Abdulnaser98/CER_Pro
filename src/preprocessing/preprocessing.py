import re
import nltk
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download("stopwords")
nltk.download("punkt")


def preprocess_text(corpus):
    """Preprocesses a list of documents by:
    - Lowercasing
    - Tokenizing
    - Removing punctuation, digits, extra white spaces, repetitions, words in parenthesis and stop words
    - Joining the tokens back together into a string
    - Returning the processed corpus

    Parameters:
        corpus (list): A list of documents

    Returns:
        processed_corpus (list): A list of processed documents
    """
    processed_corpus = []

    # Initialize the NLTK's stopword list and add additional exclusion words
    stop_words = set(stopwords.words("english"))
    exclusion_list = [
        "artificial intelligence",
        "AI",
        "energy",
        "sustainable",
        "sustainability",
    ]
    stop_words.update(exclusion_list)

    for doc in corpus:
        # Lowercase the document
        doc = doc.lower()

        # Tokenize the document
        tokens = word_tokenize(doc)

        # Remove punctuation, digits, extra white spaces, repetitions, words in parenthesis, and stop words
        processed_doc = []
        for token in tokens:
            if (
                re.fullmatch("[a-zA-Z]+", token) # Only keep tokens that are composed of letters
                and re.search("\(.*?\)", token) is None # Remove words in parenthesis
                and token not in stop_words # Remove stop words
            ):
                processed_doc.append(token)
                
        # Append the processed document only if it's not empty
        if processed_doc:
            processed_corpus.append(" ".join(processed_doc))

    return processed_corpus


def calculate_tfidf(corpus):
    """Calculates the TF-IDF scores for a corpus and filters the corpus by keeping only words with TF-IDF scores higher than the median.

    Parameters:
        corpus (list): A list of documents

        Returns:
            relevant_corpus (list): A list of documents with only words with TF-IDF scores higher than the median
    """

    # Initialize the TfidfVectorizer with unigrams and bigrams
    vectorizer = TfidfVectorizer(ngram_range=(1, 2))

    # Calculate TF-IDF values for the corpus
    tfidf_matrix = vectorizer.fit_transform(corpus)

    # Get median of all TF-IDF scores
    median_tfidf = np.median(tfidf_matrix.data)

    # Create a dictionary mapping words to indices
    word_to_index = {
        word: index for index, word in enumerate(vectorizer.get_feature_names_out())
    }

    # Keep only words with TF-IDF scores higher than the median
    relevant_corpus = []
    for i, doc in enumerate(corpus):
        relevant_doc = []
        for word in doc.split():
            if (
                word in word_to_index
                and tfidf_matrix[i, word_to_index[word]] > median_tfidf
            ):
                relevant_doc.append(word)
        relevant_corpus.append(" ".join(relevant_doc))

    return relevant_corpus


def main():
    # Given your original corpus
    df = pd.read_csv("data/data_full.csv")
    corpus = df["abstract"].tolist()

    # Preprocess the corpus
    processed_corpus = preprocess_text(corpus)

    # Calculate and filter by TF-IDF scores
    relevant_corpus = calculate_tfidf(processed_corpus)

    # Save the processed corpus as a column in the dataframe
    df["processed_abstract"] = relevant_corpus
    df.to_csv("data/data_full_processed.csv", index=False)


if __name__ == "__main__":
    main()
