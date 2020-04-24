import re
from backend.play import Play
from backend.scene import Scene


def load_play_from_file(file_path):
    with open(file_path, "r") as play_file:
        play_string = play_file.read()
    return load_play_from_string(play_string)


def load_play_from_string(play_string):
    title = parse_title(play_string)
    scene_strings = parse_scenes(play_string)

    new_play = Play(title=title)
    for scene_index, scene_string in enumerate(scene_strings):
        previous_scene = new_play.scenes.get(f"Scene {scene_index - 1}", Scene())
        new_scene = Scene(
            title=f"Scene {scene_index}", characters=previous_scene.get_characters()
        )
        update_scene_with_new_directions(
            new_scene, scene_string,
        )
        new_play.add_scene(new_scene)
    return new_play


def update_scene_with_new_directions(scene_obj, new_scene_string):
    directions_and_characters = parse_characters_from_scene(new_scene_string)
    for (direction, character) in directions_and_characters:
        if direction == "+":
            scene_obj.add_character(character)
        elif direction == "-":
            scene_obj.remove_character(character)
        else:
            raise ValueError(
                "Invalid character prefix '{direction}' for character '{character}'"
            )
    scene_obj.add_all_character_relationships()
    return scene_obj


def parse_title(play_string):
    title, _, _ = play_string.partition("\n")
    return title


def parse_scenes(play_string):
    return play_string.split("\n")[1:]


def parse_characters_from_scene(scene_string):
    return re.findall(r"(\+|-)(\w+)", scene_string)