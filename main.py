import sys
sys.path.append('./src/data_preprocessing')
sys.path.append('./src/nlp_analytics')

from preprocessing_new import *
from Topic_Model_Class import *
from utils import *
import pandas as pd


def main():
    method = "LDA_BERT"
    samp_size = 30
    ntopic = 9

    data = pd.read_csv('./data/processed_data/data_full_processed.csv')
    data = data.fillna('')  # only the comments has NaN's
    rws = data.abstract
    print(rws.shape)
    sentences, token_lists, idx_in = preprocess(rws, samp_size=samp_size)
    # Define the topic model object
    #tm = Topic_Model(k = 10), method = TFIDF)
    tm = Topic_Model(k = ntopic, method = method)
    # Fit the topic model by chosen method
    tm.fit(sentences, token_lists)

    print('Coherence:', get_coherence(tm, token_lists, 'c_v'))
    print('Silhouette Score:', get_silhouette(tm))
    # visualize and save img
    #visualize(tm)
    #for i in range(tm.k):
    #    get_wordcloud(tm, token_lists, i)


main()

