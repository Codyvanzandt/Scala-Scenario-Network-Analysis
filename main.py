from backend.play_parser import load_play_from_file
from utils import get_entire_play_graph
import networkx

two_old_twins_graph = get_entire_play_graph( load_play_from_file("data/scala_plays/the_two_old_twins") )
networkx.draw(two_old_twins_graph)