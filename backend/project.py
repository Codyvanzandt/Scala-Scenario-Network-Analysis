from collections import OrderedDict


class Project:
    def __init__(self, title=str()):
        self.plays = OrderedDict()
        self.title = title

    def __repr__(self):
        return f"{self.__class__.__name__}(title='{self.title}')"

    def __contains__(self, play_obj_or_str):
        if isinstance(play_obj_or_str, str):
            return play_obj_or_str in self.plays
        else:
            return play_obj_or_str.title in self.plays

    def change_title(self, new_title):
        self.title = new_title

    def add_play(self, new_play):
        if new_play not in self:
            self.plays[new_play.title] = new_play
        else:
            raise ValueError(f"{new_play.title} already exists in {self.title}")

    def remove_play(self, play_obj):
        if play_obj in self:
            self.plays.pop(play_obj.title)
