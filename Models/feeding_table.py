"""
    This module is needed for programming lab №8
"""
from models.chair import Chair


class FeedingTable(Chair):
    """
    A class to represent a feeding table, a subclass of Chair.
    ...
    Attributes
    __________
    id_of_chair : int
        id of chair
    material : str
        material of chair
    max_weight : int
        max weight of chair
    owner : str
        name of owner of chair
    min_height : int
        minimum height of the chair
    max_height : int
        maximum height of the chair
    child_age : int
        age of the child the chair is designed for

    Methods
    _______
    adjust_position(value):
        this method increases the height for a feeding table chair
    """

    def __init__(self, id_of_chair=Chair.DEFAULT_ID, material='', # pylint: disable=too-many-arguments
                 max_weight=Chair.DEFAULT_MAX_WEIGHT, owner=None,
                 min_height=0, max_height=0, child_age=0):
        super().__init__(id_of_chair, material, max_weight, owner)
        self.__min_height = min_height
        self.__max_height = max_height
        self.__child_age = child_age
        self.colors_set = set()

    @property
    def min_height(self):
        """
        Returns min_height
        """
        return self.__min_height

    @property
    def max_height(self):
        """
        Returns max_height
        """
        return self.__max_height

    @property
    def child_age(self):
        """
        Returns child_age
        """
        return self.__child_age

    def adjust_position(self, value):
        """
        This method increases the height for a feeding table chair
        """
        self.__max_height += value

    def __str__(self):
        """
        Returns line with feeding table chair object parameters
        """
        return super().__str__() + f", Min Height: {self.__min_height}, " \
                                   f"Max Height: {self.__max_height}, " \
                                   f"Child Age: {self.__child_age}"

    def __repr__(self):
        """
        Returns line with feeding table chair object parameters
        """
        return super().__repr__() + f", min height - {self.__min_height}, " \
                                    f"max height - {self.__max_height}, " \
                                    f"child age - {self.__child_age}"

    def get_colors_set(self):
        """
        This method returns colors_set
        """
        return self.colors_set
