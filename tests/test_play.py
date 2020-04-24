from backend.play import Play
from backend.scene import Scene
import pytest
from collections import OrderedDict


# Fixtures


@pytest.fixture
def default_play():
    return Play()


@pytest.fixture
def default_scene():
    return Scene("Scene0")


@pytest.fixture
def play_title():
    return "Play0"


@pytest.fixture
def character():
    return "Character0"


# Tests


def test_default_play(default_play):
    # Characters
    assert len(default_play.characters) == 0

    # Title
    assert default_play.title == str()

    # Scenes
    assert isinstance(default_play.scenes, OrderedDict)
    assert len(default_play.scenes) == 0


def test_play_repr(play_title):
    titled_play = Play(title=play_title)
    assert repr(titled_play) == f"Play(title='{titled_play.title}')"


def test_play_contains(default_play, default_scene):
    default_play.add_scene(default_scene)
    assert default_scene in default_play
    assert default_scene.title in default_play


def test_change_title(default_play, play_title):
    default_play.change_title(play_title)
    assert default_play.title == play_title


def test_add_character(default_play, character):
    # Case 1: adding a non-extant character
    default_play.add_character(character)
    assert character in default_play.characters

    # Case 2: adding an extant character, should raise ValueError
    with pytest.raises(ValueError) as add_character_error:
        default_play.add_character(character)
    assert (
        str(add_character_error.value)
        == f"{character} already exists in {default_play.title}"
    )


def test_remove_character(default_play, character):

    default_play.add_character(character)

    # Case 1: removing an extant character
    default_play.remove_character(character)
    assert character not in default_play.characters

    # Case 2: removing a non-extant character; should fail quietly
    default_play.remove_character(character)


def test_add_scene(default_play, default_scene):

    default_play.add_scene(default_scene)
    assert default_scene in default_play

    with pytest.raises(ValueError) as add_scene_error:
        default_play.add_scene(default_scene)
    assert (
        str(add_scene_error.value)
        == f"{default_scene.title} already exists in {default_play.title}"
    )


def test_remove_scene(default_play, default_scene):
    # Case 1: removing an extant scene
    default_play.add_scene(default_scene)
    default_play.remove_scene(default_scene)
    assert default_scene not in default_play

    # Case 2: removing a non-extant scene; should fail quietly
    default_play.remove_scene(default_scene)
