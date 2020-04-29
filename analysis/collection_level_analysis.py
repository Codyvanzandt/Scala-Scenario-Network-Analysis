from utils.load_play import get_all_plays
from analysis.play_level_analysis import summarize_play
import statistics


def mean_and_std_edge_weight():
    edges = list()
    for play in get_all_plays():
        for node in play.graph.nodes():
            edges.extend(
                play.graph.get_edge_data(node, neighbor, default={"weight": 0})[
                    "weight"
                ]
                for neighbor in play.graph.neighbors(node)
            )
    return (statistics.mean(edges), statistics.pstdev(edges))


def summarize_collection(include_play_summary=True, include_node_summary=True):
    collection_summary = {}

    if include_play_summary:
        play_summary = {
            play.title: summarize_play(play, include_node_summary=include_node_summary)
            for play in get_all_plays()
        }
        collection_summary["play_summary"] = play_summary
    return collection_summary
