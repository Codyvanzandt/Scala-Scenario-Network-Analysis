from backend.scene import Scene
import pytest


@pytest.fixture
def default_scene():
    return Scene()


def test_default_scene(default_scene):
    assert default_scene.character_graph is not None
