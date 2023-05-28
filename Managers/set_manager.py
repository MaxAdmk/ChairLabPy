"""
This module is needed for lab №9
"""


class SetManager:

    def __init__(self, chair_manager):
        self.chair_manager = chair_manager
        self.index = 0
        self.iter_set = self.create_iter_set()

    def create_iter_set(self):
        iter_set = set()
        for chair in self.chair_manager.chairs:
            iter_set.update(chair.get_colors_set())
        return iter_set

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.iter_set)

    def __getitem__(self, item):
        if item >= len(self):
            raise IndexError("Index out of range")
        return list(self.iter_set)[item]

    def __next__(self):
        if self.index >= len(self):
            self.index = 0
            raise StopIteration
        item = self[self.index]
        self.index += 1
        return item
