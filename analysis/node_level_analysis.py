def degree(play, node):
    return play.graph.degree(node)

def weighted_degree(play, node):
    return sum( datadict["weight"] for _, datadict in play.graph[node].items() ) / play.graph.degree(node)

def summarize_node(play, node):
    return {
        "name": node,
        "degree" : degree(play, node),
        "weighted_degree" : weighted_degree(play, node)
    }