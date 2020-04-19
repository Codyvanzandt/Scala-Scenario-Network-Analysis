from backend.play import Play
import pytest


@pytest.fixture
def default_play():
    return Play()


def test_default_play(default_play):
    assert len(default_play.characters) == 0
