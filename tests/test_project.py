from backend.project import Project
from backend.play import Play
from collections import OrderedDict
import pytest


# Fixtures


@pytest.fixture
def default_project():
    return Project()


@pytest.fixture
def default_play():
    return Play(title="Play0")


@pytest.fixture
def project_title():
    return "Project0"


# Tests


def test_default_project(default_project):
    # Plays
    assert isinstance(default_project.plays, OrderedDict)
    assert len(default_project.plays) == 0

    # Title
    assert default_project.title == str()


def test_repr(project_title):
    titled_project = Project(title=project_title)
    assert repr(titled_project) == f"Project(title='{project_title}')"


def test_contains(default_project, default_play):
    assert default_play not in default_project
    assert default_play.title not in default_project

    default_project.add_play(default_play)
    assert default_play in default_project
    assert default_play.title in default_project


def test_change_title(default_project, project_title):
    default_project.change_title(project_title)
    assert default_project.title == project_title


def test_add_play(default_project, default_play):
    # Case 1: add non-extant play
    default_project.add_play(default_play)
    assert default_play in default_project

    # Case 2: add extant play; should raise a ValueError
    with pytest.raises(ValueError) as add_play_error:
        default_project.add_play(default_play)
    assert (
        str(add_play_error.value)
        == f"{default_play.title} already exists in {default_project.title}"
    )


def test_remove_play(default_project, default_play):
    default_project.add_play(default_play)

    # Case 1: removing extant play
    default_project.remove_play(default_play)
    assert default_play not in default_project

    # Case 2: removing non-extant play; should fail quietly
    default_project.remove_play(default_play)
