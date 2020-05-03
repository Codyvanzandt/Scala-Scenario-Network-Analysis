from networkx.algorithms.centrality import (
    closeness_centrality,
    betweenness_centrality,
)
from networkx.algorithms.distance_measures import eccentricity
from networkx.algorithms.cluster import clustering
from functools import lru_cache
from utils.load_play import get_all_plays
from backend.character import get_character
from csv import DictWriter, DictReader


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
    return betweenness_centrality(play.graph, weight="weight")


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
        "weighted_degree": round(weighted_degree(play, node), 3),
        "closeness": round(closeness(play, node), 3),
        "flow_betweenness": round(flow_betweenness(play, node), 3),
        "clustering_coefficient": round(clustering_coefficient(play, node), 3),
    }


def normalize_all_character_data(
    character_file_path, normalizing_file_path, output_file_path
):
    character_data = _read_character_data(character_file_path)
    normalizing_data = _read_normalizing_data_by_play(normalizing_file_path)

    for character_row in character_data:
        play_title = character_row["play"]
        play_specific_normalizing_data = normalizing_data[play_title]
        for (
            statistic_name,
            norm_statistic_value,
        ) in play_specific_normalizing_data.items():
            char_statistic_value = float(character_row[statistic_name])
            norm_statistic_value = float(norm_statistic_value)
            character_row[statistic_name] = round(
                char_statistic_value / norm_statistic_value, 3
            )

    with open(output_file_path, "w") as output_file:
        norm_data_writer = DictWriter(output_file, fieldnames=character_data[0].keys())
        norm_data_writer.writeheader()
        norm_data_writer.writerows(character_data)


def _read_character_data(character_file_path):
    with open(character_file_path, "r") as char_data_file_obj:
        character_data_reader = DictReader(char_data_file_obj)
        return [row for row in character_data_reader]


def _read_normalizing_data_by_play(normalizing_file_path):
    with open(normalizing_file_path, "r") as norm_file_obj:
        normalizing_data_reader = DictReader(norm_file_obj)
        return {
            row["basis_play"]: {
                norm_statistic_name: norm_statistic_val
                for norm_statistic_name, norm_statistic_val in row.items()
                if norm_statistic_name != "basis_play"
            }
            for row in normalizing_data_reader
        }


def generate_all_character_data(output_file=None):
    character_data = _generate_all_character_data()
    if output_file is None:
        return character_data
    else:
        with open(output_file, "w") as output_file_object:
            fieldnames = [
                "character",
                "archetype",
                "gender",
                "play",
                "degree",
                "weighted_degree",
                "closeness",
                "flow_betweenness",
                "clustering_coefficient",
            ]
            writer = DictWriter(output_file_object, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(character_data)


def _generate_all_character_data():
    for play in get_all_plays():
        for character_name in play.graph.nodes():
            character_summary = summarize_node(play, character_name)
            character_object = get_character(character_name)
            yield {
                "character": character_object.name,
                "archetype": character_object.archetype.name,
                "gender": character_object.gender.name,
                "play": play.title,
                "degree": character_summary["degree"],
                "weighted_degree": character_summary["weighted_degree"],
                "closeness": character_summary["closeness"],
                "flow_betweenness": character_summary["flow_betweenness"],
                "clustering_coefficient": character_summary["clustering_coefficient"],
            }
