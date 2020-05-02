from utils.load_play import load_play_from_file
from analysis.node_level_analysis import summarize_node, generate_all_character_data, normalize_all_character_data
from analysis.play_level_analysis import summarize_play
from analysis.collection_level_analysis import *
from analysis.node_embeddings import build_node_embedding_model
from utils.random_graphs import generate_similar_random_graph
from utils.load_play import get_all_plays, get_combined_play_graph
from backend.character import get_character
import matplotlib.pyplot as plt
import networkx
from pprint import pprint
from utils.random_graphs import write_random_node_statistics
import time

dim=16

g = get_combined_play_graph()
structure_model = build_node_embedding_model(g, d=dim, p=1, q=2)

with open("data/structural_node_embeddings.csv", "w") as output_file:
    output_file.write("character,archetype,gender," + ",".join(f"D{i}" for i in range(dim)) + "\n")
    for char in structure_model.wv.vocab.keys():
        char_obj = get_character(char)
        char_data = f"{char_obj.name},{char_obj.archetype},{char_obj.gender},"
        char_vector = ",".join( map(str, structure_model.wv[char]))
        output_file.write(char_data + char_vector + "\n")