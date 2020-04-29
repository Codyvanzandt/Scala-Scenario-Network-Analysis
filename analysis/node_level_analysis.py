from networkx.algorithms.centrality import (
    closeness_centrality,
    current_flow_betweenness_centrality,
)
from networkx.algorithms.distance_measures import eccentricity
from networkx.algorithms.cluster import clustering
from functools import lru_cache
from utils.load_play import get_all_plays
from backend.character import get_character
from csv import DictWriter


def degree(play, node):
    return play.graph.degree(node)


def weighted_degree(play, node):
    return sum(datadict["weight"] for _, datadict in play.graph[node].items())


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
        "weighted_degree": round( weighted_degree(play, node), 3 ),
        "closeness": round( closeness(play, node), 3 ),
        "flow_betweenness": round( flow_betweenness(play, node), 3 ),
        "clustering_coefficient": round( clustering_coefficient(play, node), 3 )
    }

def generate_all_character_data(output_file=None):
    character_data = _generate_all_character_data()
    if output_file is None:
        return character_data
    else:
        with open(output_file,"w") as output_file_object:
            fieldnames = ["character", "archetype", "gender", "play", "degree", "weighted_degree", "closeness", "flow_betweenness", "clustering_coefficient"]
            writer = DictWriter(output_file_object, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(character_data)

def _generate_all_character_data():
    for play in get_all_plays():
        for character_name in play.graph.nodes():
            character_summary = summarize_node(play, character_name)
            character_object = get_character(character_name)
            yield {
                "character" : character_object.name,
                "archetype" : character_object.archetype.name,
                "gender" : character_object.gender.name,
                "play" : play.title,
                "degree" : character_summary["degree"],
                "weighted_degree" : character_summary["weighted_degree"],
                "closeness" : character_summary["closeness"],
                "flow_betweenness" : character_summary["flow_betweenness"],
                "clustering_coefficient" : character_summary["clustering_coefficient"],
            }