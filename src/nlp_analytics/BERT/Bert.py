#from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
"""
print('Getting vector representations for BERT...')

data = pd.read_csv('../../../data/processed_data/data_full_processed.csv')

model = SentenceTransformer('bert-base-nli-max-tokens')

embeddings = np.array(model.encode(data.processed_abstract.to_list(), show_progress_bar=True))

data['embeddings'] = list(embeddings)

data.to_csv('../../../data/processed_data/data_full_processed_with_embeddings.csv')
"""

print('Getting vector representations for BERT. DONE')

data = pd.read_csv('/Users/abdulnaser/Desktop/CER_Pro/data/processed_data/data_full_processed_with_embeddings.csv')


print(data['embeddings'])
# Create the k-means model
n_clusters = 8  # You can change the number of clusters as per your requirement
kmeans = KMeans(n_clusters=n_clusters)

# Fit the k-means model to the data
kmeans.fit(data['embeddings'][1:10])


# Get the labels assigned to each data point
#labels = kmeans.labels_

#data['Cluster'] = labels





