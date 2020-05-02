import re
import os
import copy
import networkx
from backend.play import Play
from backend.scene import Scene
from utils.manipulate_play import update_with_complete_graph


def get_combined_play_graph(edge_list_path):
    g = networkx.Graph()
    with open(edge_list_path, "r") as input_file:
        for line in input_file:
            u,v,w = line.split()
            if g.has_edge(u,v):
                g[u][v]["weight"] += int(w)
            else:
                g.add_edge(u, v, weight=1)
    return g


def get_all_plays():
    for play_file in _get_play_file_names():
        yield load_play_from_file(play_file)


def _get_play_file_names():
    play_dir = "data/scala_plays"
    return [os.path.join(play_dir, play_name) for play_name in os.listdir(play_dir)]


def load_play_from_file(file_path):
    with open(file_path, "r") as play_file:
        play_string = play_file.read()
    return load_play_from_string(play_string)


def load_play_from_string(play_string):
    title = parse_title(play_string)
    scene_strings = parse_scenes(play_string)

    new_play = Play(title=title)
    for scene_index, scene_string in enumerate(scene_strings):
        previous_scene = new_play.scenes.get(f"Scene {scene_index}", Scene())
        new_scene = Scene(
            title=f"Scene {scene_index+1}", characters=previous_scene.get_characters()
        )
        update_scene_with_new_directions(
            new_scene, scene_string,
        )
        new_play.add_scene(new_scene)
    return update_with_complete_graph(new_play)


def update_scene_with_new_directions(scene_obj, new_scene_string):
    directions_and_characters = parse_characters_from_scene(new_scene_string)
    onstage = list(scene_obj.get_characters())
    entering = list()
    for (direction, character) in directions_and_characters:
        if direction == "+":
            scene_obj.add_character(character)
            entering.append(character)
        elif direction == "-":
            scene_obj.remove_character(character)
            onstage.remove(character)
        else:
            raise ValueError(
                "Invalid character prefix '{direction}' for character '{character}'"
            )
    scene_obj.add_all_character_relationships(onstage=onstage, entering=entering)
    return scene_obj


def parse_title(play_string):
    title, _, _ = play_string.partition("\n")
    return title


def parse_scenes(play_string):
    return play_string.split("\n")[1:]


def parse_characters_from_scene(scene_string):
    return re.findall(r"(\+|-)(\w+)", scene_string)
