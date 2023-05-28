"""
    This module is needed for programming lab №8
"""


class ChairManager:
    """
    A class to manage chairs and demonstrate their functionality.
    """

    def __init__(self):
        self.chairs = []

    def __len__(self):
        return len(self.chairs)

    def __getitem__(self, item):
        return self.chairs[item]

    def __iter__(self):
        return iter(self.chairs)

    def get_chairs_occupied_statuses(self):
        """
        This method returns occupied statuses of objects
        """
        return [chair.is_occupied() for chair in self.chairs]

    def get_objects_with_indexes(self):
        """
        This method returns objects with their indexes
        """
        return [f"{index}: {obj}" for index, obj in enumerate(self.chairs)]

    def get_chairs_with_occupied_statuses(self):
        """
        Returns objects with their occupied statuses
        """
        return [f"Object: {obj}, is occupied: {occupied_status}" for obj, occupied_status in
                zip(self.chairs, self.get_chairs_occupied_statuses())]

    def check_objects(self, condition):
        """
        This method checks if condition is performed and returns true or false for any and all
        """
        return {'all': all(condition(chair) for chair in self.chairs),
                'any': any(condition(chair) for chair in self.chairs)}

    def add_chair(self, *args):
        """
        This method adds chair to list of chairs
        """
        self.chairs.extend(args)

    def print_chairs(self):
        """
        Prints the details of each chair in the list.
        """
        for chair in self.chairs:
            print(chair)

    def find_all_made_with_material(self, material_to_find):
        """
        This method returns list of chairs with material which we want to find
        """
        return list(filter(lambda chair: chair.material == material_to_find, self.chairs))

    def find_all_with_max_weight_greater_than(self, value: int):
        """
        This method returns list of chairs with max weight greater than max_weight_to_find
        """
        return list(filter(lambda chair: chair.max_weight > value,
                           self.chairs))
