from utils.load_play import load_play_from_file
from analysis.node_level_analysis import summarize_node, generate_all_character_data
from analysis.play_level_analysis import summarize_play
from analysis.collection_level_analysis import *
from utils.random_graphs import generate_similar_random_graph
import matplotlib.pyplot as plt
import networkx
from pprint import pprint
import time

play = load_play_from_file("data/scala_plays/the_deserved_punishment")

generate_all_character_data("data/all_character_data.csv")
