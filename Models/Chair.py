"""
    This module is needed for programming lab №8
"""
from abc import ABC, abstractmethod


class Chair(ABC):
    """
    A class to represent a chair.
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

    Methods
    _______
    occupy(owner):
        this method changes owner parameter to given
    release():
        this method changes owner parameter to None
    is_occupied()
        This method shows whether owner parameter != None
    """

    DEFAULT_ID = 1
    DEFAULT_MAX_WEIGHT = 0

    def __init__(self, id_of_chair=DEFAULT_ID, material='',
                 max_weight=DEFAULT_MAX_WEIGHT, owner=None):
        self.__id_of_chair = id_of_chair
        self.__material = material
        self.__max_weight = max_weight
        self.__owner = owner

    @property
    def chair_id_of_chair(self):
        """
        Returns id_of_chair
        """
        return self.__id_of_chair

    @property
    def chair_material(self):
        """
        Returns material
        """
        return self.__material

    @property
    def chair_owner(self):
        """
        Returns owner
        """
        return self.__owner

    @property
    def chair_max_weight(self):
        """
        Returns max_weight
        """
        return self.__max_weight

    @chair_id_of_chair.setter
    def chair_id_of_chair(self, new_id_of_chair):
        self.__id_of_chair = new_id_of_chair

    @chair_owner.setter
    def chair_owner(self, new_owner):
        self.__owner = new_owner

    @chair_max_weight.setter
    def chair_max_weight(self, new_max_weight):
        self.__max_weight = new_max_weight

    @chair_material.setter
    def chair_material(self, new_material):
        self.__material = new_material

    def __str__(self):
        """
        Returns line with chair object parameters
        """
        return f"Id: {self.__id_of_chair}, Material: {self.__material}," \
               f" Max Weight: {self.__max_weight}, Owner: {self.__owner}"

    def __repr__(self):
        """
        Returns line with chair object parameters
        """
        return f"Chair(id - {self.__id_of_chair}, material - {self.__material}," \
               f" max weight - {self.__max_weight}, owner - {self.__owner})"

    def occupy(self, owner):
        """
        This method changes owner parameter to the given one
        """
        self.__owner = owner if self.__owner is None else print("This chair is occupied")

    def release(self):
        """
        This method changes owner parameter to None
        """
        self.__owner = None

    def is_occupied(self):
        """
        This method shows if owner parameter != None:
        """
        return self.__owner is not None

    @staticmethod
    def get_instance():
        """
        This method returns instance of class
        """
        if Chair.__instance is None:
            Chair.__instance = Chair()
        return Chair.__instance
