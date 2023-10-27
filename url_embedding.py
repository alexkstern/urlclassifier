from sentence_transformers import SentenceTransformer
import numpy as np

class URLEmbedder:
    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    
    def url_to_embedding(self, url):
        try:
            embedding = self.model.encode(url)
            embedding_list = embedding.tolist()
            return embedding_list
        except Exception as e:
            print(f"An error occurred: {e}")
            return np.nan
