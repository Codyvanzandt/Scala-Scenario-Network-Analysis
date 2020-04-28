def degree(play, node):
    return play.graph.degree(node)

def summarize_node(play, node):
    return {
        "name" : node,
        "degree" : play.graph.degree(node)
    }