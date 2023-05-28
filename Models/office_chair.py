"""
    This module is needed for programming lab №8
"""
from models.chair import Chair


class OfficeChair(Chair):
    """
    A class to represent an office chair, a subclass of Chair.
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
    type : str
        type of the office chair
    upholstery_material : str
        material of the chair's upholstery
    backrest_angle : int
        current angle of the chair's backrest in degrees

    Methods
    _______
    adjust_position(value):
        this method increases the backrest angle for an office chair
    """

    def __init__(self, id_of_chair=Chair.DEFAULT_ID, material='', # pylint: disable=too-many-arguments
                 max_weight=Chair.DEFAULT_MAX_WEIGHT, owner=None,
                 type_of_chair='', upholstery_material='', backrest_angle=0):
        super().__init__(id_of_chair, material, max_weight, owner)
        self.__type_of_chair = type_of_chair
        self.__upholstery_material = upholstery_material
        self.__backrest_angle = backrest_angle
        self.colors_set = set()

    @property
    def type_of_chair(self):
        """
        Returns type_of_chair
        """
        return self.__type_of_chair

    @property
    def upholstery_material(self):
        """
        Returns upholstery_material
        """
        return self.__upholstery_material

    @property
    def backrest_angle(self):
        """
        Returns backrest_angle
        """
        return self.__backrest_angle

    def adjust_position(self, value):
        """
        This method increases the backrest angle for an office chair
        """
        self.__backrest_angle += value

    def __str__(self):
        """
        Returns line with office chair object parameters
        """
        return super().__str__() + f", Type: {self.__type_of_chair}, " \
                                   f"Upholstery Material: {self.__upholstery_material}, " \
                                   f"Backrest Angle: {self.__backrest_angle}"

    def __repr__(self):
        """
        Returns line with office chair object parameters
        """
        return super().__repr__() + f", type - {self.__type_of_chair}, " \
                                    f"upholstery material - {self.__upholstery_material}, " \
                                    f"backrest angle - {self.__backrest_angle}"

    def get_colors_set(self):
        return self.colors_set
