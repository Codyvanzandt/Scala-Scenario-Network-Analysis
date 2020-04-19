import networkx as nx
from itertools import combinations


class Scene:
    def __init__(self, title=str()):
        self.character_graph = nx.Graph()
        self.title = title

    def __contains__(self, character):
        return self.character_graph.has_node(character)

    def __repr__(self):
        return f"{self.__class__.__name__}(title='{self.title}')"

    def change_title(self, new_scene_title):
        self.title = new_scene_title

    def add_character(self, character):
        self.character_graph.add_node(character)

    def remove_character(self, character):
        self.character_graph.remove_node(character)

    def add_all_character_relationships(self):
        for character_pair in self._get_unique_character_pairs():
            self._add_character_relationship(*character_pair)

    def _add_character_relationship(self, u, v):
        self.character_graph.add_edge(u, v, weight=1)

    def _get_unique_character_pairs(self):
        return combinations(self.character_graph.nodes(), 2)
