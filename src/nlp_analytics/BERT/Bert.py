from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd

print('Getting vector representations for BERT...')

data = pd.read_csv('/Users/abdulnaser/Desktop/CER_Pro/data/processed_data/data_full_processed.csv')


model = SentenceTransformer('bert-base-nli-max-tokens')

embeddings = np.array(model.encode(data.processed_abstract.to_list(), show_progress_bar=True))

data['embeddings'] = list(embeddings)

data.to_csv('/Users/abdulnaser/Desktop/CER_Pro/data/processed_data/data_full_processed_with_embeddings.csv')

print('Getting vector representations for BERT. DONE')
