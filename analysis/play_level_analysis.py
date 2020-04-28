from analysis.node_level_analysis import summarize_node


def n_nodes(play):
    return play.graph.number_of_nodes()


def n_edges(play):
    return play.graph.size()


def summarize_play(play, include_node_summary=True):
    play_summary = {
        "title": play.title,
        "num_nodes": n_nodes(play),
        "num_edges": n_edges(play),
    }
    if include_node_summary:
        node_summary_data = {
            node: summarize_node(play, node) for node in play.graph.nodes()
        }
        play_summary["node_summary"] = node_summary_data
    return play_summary
