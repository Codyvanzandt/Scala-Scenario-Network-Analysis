from backend.scene import Scene
import pytest
import networkx as nx
from unittest.mock import patch
from itertools import chain, product, combinations


# Fixtures


@pytest.fixture
def default_scene():
    return Scene()


@pytest.fixture
def character():
    return "Character0"


@pytest.fixture
def two_characters():
    return ("Character0", "Character1")


@pytest.fixture
def multiple_characters():
    return ("Character0", "Character1", "Character2", "Character3")


@pytest.fixture
def scene_title():
    return "Scene0"


# Tests


def test_default_scene(default_scene):
    assert isinstance(default_scene.character_graph, nx.Graph)

    assert default_scene.character_graph.number_of_nodes() == 0
    assert default_scene.character_graph.size() == 0
    assert default_scene.title == str()


def test_scene_repr(scene_title):
    titled_scene = Scene(scene_title)
    assert repr(titled_scene) == f"Scene(title='{titled_scene.title}')"


def test_update_scene_title(default_scene, scene_title):
    assert default_scene.title == str()
    default_scene.change_title(scene_title)
    assert default_scene.title == scene_title


def test_add_character(default_scene, character):
    assert character not in default_scene

    default_scene.add_character(character)
    assert character in default_scene

    # Adding the same character multiple times will fail quietly
    default_scene.add_character(character)
    assert character in default_scene
    assert len(default_scene.character_graph.nodes()) == 1


def test_remove_character(default_scene, character):

    # Removing an extant character
    default_scene.add_character(character)
    assert character in default_scene
    default_scene.remove_character(character)
    assert character not in default_scene

    # Removing an non-extant character should raise a networkx error
    with pytest.raises(nx.exception.NetworkXError) as nx_error:
        default_scene.remove_character(character)
    assert str(nx_error.value) == f"The node {character} is not in the graph."


def test_add_all_character_relationships(default_scene, multiple_characters):
    onstage, entering = multiple_characters[:2], multiple_characters[2:]
    default_scene.add_all_character_relationships(onstage=onstage, entering=entering)
    expected_edges = set(chain(product(onstage, entering), combinations(entering, 2)))
    for u, v in default_scene.character_graph.edges():
        assert ((u, v) in expected_edges) ^ ((v, u) in expected_edges)


def test__add_character_relationship(default_scene, two_characters):
    default_scene._add_character_relationship(*two_characters)
    assert default_scene.character_graph.has_edge(*two_characters)
    assert default_scene.character_graph.get_edge_data(*two_characters)["weight"] == 1
