import networkx
from backend.play import Play

def update_with_complete_graph(play):
    play_graph = networkx.Graph()
    for scene_name, scene in play.scenes.items():
        weighted_edges = scene.character_graph.edges(data="weight", default=0)
        play_graph.add_weighted_edges_from(weighted_edges)
    return Play(title=play.title, scenes=play.scenes, graph=play_graph )
