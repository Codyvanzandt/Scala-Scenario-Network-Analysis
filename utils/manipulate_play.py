import networkx
from backend.play import Play


def update_with_complete_graph(play):
    play_graph = networkx.Graph()
    for scene in play.scenes.values():
        for u, v in scene.character_graph.edges():
            if play_graph.has_edge(u, v):
                play_graph[u][v]["weight"] += 1
            else:
                play_graph.add_edge(u, v, weight=1)
    return Play(title=play.title, scenes=play.scenes, graph=play_graph)
