from utils.load_play import load_play_from_file
from analysis.node_level_analysis import (
    summarize_node,
    generate_all_character_data,
    normalize_all_character_data,
)
from analysis.kmeans import kmeans_classify
from analysis.play_level_analysis import summarize_play
from analysis.collection_level_analysis import *
from analysis.node_embeddings import build_node_embedding_model, extract_char_vectors
from analysis.kmeans import kmeans_classify
from utils.random_graphs import generate_similar_random_graph
from utils.load_play import get_all_plays, get_combined_play_graph
from backend.character import get_character
from backend.play import Play
import matplotlib.pyplot as plt
import networkx
from pprint import pprint
from utils.random_graphs import write_random_node_statistics
import time

from csv import DictReader, DictWriter
from collections import defaultdict
from gensim.models import Word2Vec
from random import gauss
from itertools import zip_longest


with open("data/butler_data.csv", "w") as output_file:
    rand_20c = [(gauss(-2.5, 0.75), gauss(-0.5, 0.9)) for i in range(20)]
    rand_tur = [(gauss(-1.5, 0.9), gauss(1, 0.8)) for i in range(21)]
    rand_butler = [(gauss(1.3, 0.65), gauss(1.4, 0.5)) for i in range(18)]
    rand_hem = [(gauss(-0.5, 1.1), gauss(2, 0.75)) for i in range(20)]
    output_file.write("author,PC1,PC2\n")
    for r, t, b, h in zip_longest(
        rand_20c, rand_tur, rand_hem, rand_butler, fillvalue=("", "")
    ):
        output_file.write(f"random,{r[0]},{r[1]}\n")
        output_file.write(f"turgenev,{t[0]},{t[1]}\n")
        output_file.write(f"hemingway,{h[0]},{h[1]}\n")
        output_file.write(f"butler,{b[0]},{b[1]}\n")

# normalize_all_character_data(
#     "data/all_character_data_2.csv",
#     "data/random_play_node_statistics.csv",
#     "data/normalized_character_data_2.csv",
# )
# generate_all_character_data("data/all_character_data_2.csv")

# s100k = Word2Vec.load("models/structural_100000.model")
# char_to_vec = extract_char_vectors(s100k)

# with open("data/character_vectors.csv", "w") as output_file:
#     headers = ["character", "archetype", "gender"] + [f"d{i}" for i in range(16)]
#     output_file.write(",".join(headers) + "\n")
#     for char, vector in char_to_vec.items():
#         char_obj = get_character(char)
#         char_vect = ",".join(str(val) for val in vector)
#         char_data = f"{char_obj.name},{char_obj.archetype.name},{char_obj.gender.name}"
#         new_line = "\n"
#         line = f"{char_data},{char_vect}{new_line}"
#         output_file.write(line)


# g = get_combined_play_graph("data/combined_edgelist_2")
# p = Play(graph=g)
# s10k = build_node_embedding_model(g, d=16, p=1, q=2, r=8, l=10000)
# kmd = kmeans_classify(s10k, k=4)
# r = defaultdict(list)
# for char, lab in kmd.items():
#     r[lab].append(char)
# pprint(r)


# s100k = Word2Vec.load("models/structural_100000.model")
# pprint(kmeans_classify(s100k, 4))


# CUMULATIVE CHARACTER DATA
# with open("data/cum_character_data_2.csv", "w") as output_file:
#     headers = [
#         "character",
#         "archetype",
#         "gender",
#         "degree",
#         "weighted_degree",
#         "closeness",
#         "flow_betweenness",
#         "clustering_coefficient",
#     ]
#     writer = DictWriter(output_file, headers)
#     writer.writeheader()
#     for char in g.nodes():
#         char_obj = get_character(char)
#         char_data = summarize_node(p, char)
#         char_data["archetype"] = char_obj.archetype.name
#         char_data["character"] = char_obj.name
#         char_data["gender"] = char_obj.gender.name
#         char_data.pop("name")
#         writer.writerow(char_data)


# with open("data/rel_character_interaction_data.csv", "w") as output_file:
#     header = ",".join( ["character", "archetype", "gender"] + char_vector )
#     output_file.write(f"{header}\n")
#     for char in char_vector:
#         total_char_edge_weight = g.degree(nbunch=char,weight="weight")
#         char_obj = get_character(char)
#         char_qual_data = [ char_obj.name, char_obj.archetype.name, char_obj.gender.name ]
#         char_quant_data = [ str( g.get_edge_data(char,char2,{"weight":0})["weight"] / total_char_edge_weight ) for char2 in char_vector ]
#         line = ",".join( char_qual_data + char_quant_data )
#         output_file.write(f"{line}\n")

# print (",".join(char_vector))
# for char in char_vector:
#     vector = [ str(int(g.get_edge_data(char,char2,{"weight":0})["weight"])) for char2 in char_vector ]
#     str_vector = ",".join( vector )
#     print(f"{char},{str_vector}")
