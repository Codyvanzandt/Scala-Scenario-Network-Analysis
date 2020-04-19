from collections import OrderedDict


class Play:
    def __init__(self, title=str()):
        self.title = title
        self.scenes = OrderedDict()
        self.characters = list()

    def __repr__(self):
        return f"{self.__class__.__name__}(title='{self.title}')"

    def __contains__(self, scene_title_or_object):
        if isinstance(scene_title_or_object, str):
            return scene_title_or_object in self.scenes
        else:
            return scene_title_or_object.title in self.scenes

    def change_title(self, new_play_title):
        self.title = new_play_title

    def add_character(self, character):
        if character not in self.characters:
            self.characters.append(character)
        else:
            raise ValueError(f"{character} already exists in {self.title}")

    def remove_character(self, character):
        try:
            self.characters.remove(character)
        except ValueError:
            pass

    def add_scene(self, new_scene_obj):
        if new_scene_obj not in self:
            self.scenes[new_scene_obj.title] = new_scene_obj
        else:
            raise ValueError(f"{new_scene_obj.title} already exists in {self.title}")

    def remove_scene(self, scene_obj):
        if scene_obj in self:
            self.scenes.pop(scene_obj.title)
