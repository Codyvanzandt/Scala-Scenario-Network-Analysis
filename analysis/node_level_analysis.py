from networkx.algorithms.centrality import closeness_centrality, current_flow_betweenness_centrality
from networkx.algorithms.distance_measures import eccentricity
from networkx.algorithms.cluster import clustering
from functools import lru_cache

def degree(play, node):
    return play.graph.degree(node)


def weighted_degree(play, node):
    return sum(
        datadict["weight"] for _, datadict in play.graph[node].items()
    )

def closeness(play, node):
    return closeness_centrality(play.graph, u=node, distance="weight",)

def flow_betweenness(play, node):
    betweenness_dict = _get_flow_betweenness_dict(play)
    return betweenness_dict[node]

@lru_cache(maxsize=2)
def _get_flow_betweenness_dict(play):
    return current_flow_betweenness_centrality(play.graph, weight="weight")

def clustering_coefficient(play, node):
    clustering_dict = _get_clustering_dict(play)
    return clustering_dict[node]

@lru_cache(maxsize=2)
def _get_clustering_dict(play):
    return clustering(play.graph, weight="weight")

def summarize_node(play, node):
    return {
        "name": node,
        "degree": degree(play, node),
        "weighted_degree": weighted_degree(play, node),
        "closeness" : closeness(play, node),
        "flow_betweenness" : flow_betweenness(play, node),
        "clustering_coefficient" : clustering_coefficient(play, node)
    }
