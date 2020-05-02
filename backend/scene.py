import networkx as nx
from itertools import combinations, product, chain
import re


class Scene:
    def __init__(self, title=str(), characters=tuple()):
        self.character_graph = nx.Graph()
        self.title = title
        for character in characters:
            self.add_character(character)

    def __contains__(self, character):
        return self.character_graph.has_node(character)

    def __repr__(self):
        return f"Scene(title='{self.title}')"

    def __str__(self):
        return f"""{self.__class__.__name__}(
            title='{self.title}',
            characters=[{', '.join( repr(char) for char in self.get_characters())}],
        )"""

    def change_title(self, new_scene_title):
        self.title = new_scene_title

    def get_characters(self):
        return self.character_graph.nodes()

    def add_character(self, character):
        self.character_graph.add_node(character)

    def remove_character(self, character):
        self.character_graph.remove_node(character)

    def add_all_character_relationships(self, onstage=tuple(), entering=tuple()):
        old_with_new = product(onstage, entering)
        new_with_new = combinations(entering, 2)
        for char_pair in chain(old_with_new, new_with_new):
            self._add_character_relationship(*char_pair)

    def _add_character_relationship(self, u, v):
        if self.character_graph.has_edge(u, v):
            self.character_graph[u][v]["weight"] += 1
        else:
            self.character_graph.add_edge(u, v, weight=1)
