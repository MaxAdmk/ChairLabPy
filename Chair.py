class Chair:

    DEFAULT_ID = 1
    DEFAULT_MAX_WEIGHT = 0

    def __init__(self, id_of_chair=DEFAULT_ID, material='', max_weight=DEFAULT_MAX_WEIGHT, owner=None):
        self.__id_of_chair = id_of_chair
        self.__material = material
        self.__max_weight = max_weight
        self.__owner = owner

    @property
    def chair_id_of_chair(self):
        return self.__id_of_chair

    @property
    def chair_material(self):
        return self.__material

    @property
    def chair_owner(self):
        return self.__owner

    @property
    def chair_max_weight(self):
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
        return f"Id: {self.__id_of_chair}, Material: {self.__material}," \
               f" Max Weight: {self.__max_weight}, Owner: {self.__owner}"

    def __repr__(self):
        return f"Chair(id - {self.__id_of_chair}, material - {self.__material}," \
               f" max weight - {self.__max_weight}, owner - {self.__owner})"

    def occupy(self, owner):
        self.__owner = owner if self.__owner is None else print("This chair is occupied")

    def release(self):
        self.__owner = None

    def is_occupied(self):
        return self.__owner is not None

if __name__ == '__main__':
    chairs = [Chair(1, 'wood', 100, 'John'),
    Chair(2, 'plastic', 80, 'Alice'),
    Chair(3, 'metal', 120, None)]

    for chair in chairs:
        print(chair)