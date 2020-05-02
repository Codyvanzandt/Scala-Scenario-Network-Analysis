import node2vec
from node2vec import Node2Vec


def build_node_embedding_model(G, d, p, q, r, l):
    return Node2Vec(graph=G, dimensions=d, walk_length=l, num_walks=r, p=p, q=q, weight_key="weight", workers=16).fit()

def extract_char_vectors(model):
    char_vectors = dict()
    for char in model.wv.vocab.keys():
        char_vectors[char] = model.wv[char]
    return char_vectors
