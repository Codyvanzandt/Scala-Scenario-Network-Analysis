import node2vec
from node2vec import Node2Vec

def build_node_embedding_model(G, d, p, q):
    return Node2Vec(graph=G, dimensions=d, sampling_strategy={"p":p, "q":q}).fit()

