from analysis.node_embeddings import extract_char_vectors
from collections import defaultdict
from sklearn.cluster import KMeans

def kmeans_classify(model, k):
    chars_and_vecs = extract_char_vectors(model)
    chars, vecs = zip(*chars_and_vecs.items())
    preds = KMeans(n_clusters=4).fit_predict(vecs)
    return dict(zip(chars, preds))