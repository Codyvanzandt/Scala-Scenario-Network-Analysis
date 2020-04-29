import numpy
from networkx.generators.random_graphs import dense_gnm_random_graph

def generate_similar_random_graph(play):
    num_nodes = len(play.graph.nodes())
    num_edges = len(play.graph.edges())
    random_graph = dense_gnm_random_graph(num_nodes, num_edges)
    for u,v in random_graph.edges():
        random_graph[u][v]["weight"] = generate_random_edge_weight()
    return random_graph

def generate_random_edge_weight():
    mu, std = (
        5.35,
        3.48,
    )  # result of analysis.collection_level_analysis.mean_and_std_edge_weight()
    return numpy.log(numpy.random.lognormal(mu, std))
