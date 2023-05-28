from managers.chair_manager import ChairManager
from models.feeding_table import FeedingTable
from models.office_chair import OfficeChair

if __name__ == '__main__':

    chair_manager = ChairManager()
    wooden_feeding_table = FeedingTable(1, 'wood', 100, 'John', 50, 100, 2)
    plastic_feeding_table = FeedingTable(2, 'plastic', 80, 'Alice', 40, 80, 3)
    metalic_office_chair = OfficeChair(3, 'metal', 120, None, 'Executive', 'Leather', 30)
    chair_manager.add_chair(wooden_feeding_table, plastic_feeding_table, metalic_office_chair)

    print(chair_manager.get_chairs_occupied_statuses())
    print(chair_manager.get_objects_with_indexes())
    print(chair_manager.get_chairs_with_occupied_statuses())

    print(wooden_feeding_table.get_attributes_by_type(int))

    def is_max_weight_greater_than_10(chair):
        return chair.max_weight > 10

    print(chair_manager.check_objects(is_max_weight_greater_than_10))
