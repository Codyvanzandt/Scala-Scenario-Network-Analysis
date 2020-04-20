from collections import OrderedDict

class App:
    def __init__(self):
        self.projects = OrderedDict()

    def __repr__(self):
        return f"App()"

    def __contains__(self, project_obj_or_str):
        if isinstance(project_obj_or_str, str):
            return project_obj_or_str in self.projects
        else:
            return project_obj_or_str.title in self.projects

    def add_project(self, new_project):
        if new_project not in self:
            self.projects[new_project.title] = new_project
        else:
            raise ValueError(f"{new_project.title} already exists in App")

    def remove_project(self, project_title):
        if project_title in self:
            self.projects.pop(project_title)

    

