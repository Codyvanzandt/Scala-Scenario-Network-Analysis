import numpy
from networkx.generators.random_graphs import dense_gnm_random_graph
from analysis.node_level_analysis import summarize_node
from utils.load_play import get_all_plays
from collections import Counter
from csv import DictWriter
from backend.play import Play
import math
import os

def write_random_node_statistics(output_file_path):
    field_names = ["basis_play", "degree", "weighted_degree", "closeness", "flow_betweenness", "clustering_coefficient"]
    with open(output_file_path, "w") as output_file:
        writer = DictWriter(output_file, field_names)
        writer.writeheader()
        for i, play in enumerate(get_all_plays()):
            random_stats = get_random_node_statistics(play, 1000)
            random_stats.pop("name")
            random_stats["basis_play"] = play.title
            writer.writerow(random_stats)
            print(f"Play {i+1}/25")
        

def get_random_node_statistics(play, n):
    random_node_summaries = list(_yield_random_node_summaries(play, n))
    n_summaries = len(random_node_summaries)
    return { k : round( v / n_summaries, 3) for k,v in sum(random_node_summaries, Counter()).items() }
    

def _yield_random_node_summaries(play, n):
    for _ in range(n):
        random_play = Play(graph=generate_similar_random_graph(play))
        for node in random_play.graph.nodes():
            node_summary = summarize_node(random_play, node)
            yield Counter(node_summary)


def generate_similar_random_graph(play, as_play=False):
    num_nodes = len(play.graph.nodes())
    num_edges = len(play.graph.edges())
    random_graph = dense_gnm_random_graph(num_nodes, num_edges)
    for u, v in random_graph.edges():
        random_graph[u][v]["weight"] = generate_random_edge_weight()
    return random_graph


def generate_random_edge_weight():
    mu, std = (
        5.35,
        3.48,
    )  # result of analysis.collection_level_analysis.mean_and_std_edge_weight()
    return math.sqrt( numpy.random.normal(mu, std)**2 )
