"""
    This module is needed for programming lab №8
"""
from Models.FeedingTable import FeedingTable
from Models.OfficeChair import OfficeChair


class ChairManager:
    """
    A class to manage chairs and demonstrate their functionality.
    """

    @staticmethod
    def print_chairs(chairs):
        """
        Prints the details of each chair in the list.
        """
        for chair in chairs:
            print(chair)


if __name__ == '__main__':
    chairs = [
        FeedingTable(1, 'wood', 100, 'John', 50, 100, 2),
        FeedingTable(2, 'plastic', 80, 'Alice', 40, 80, 3),
        OfficeChair(3, 'metal', 120, None, 'Executive', 'Leather', 30)
    ]

    ChairManager.print_chairs(chairs)
