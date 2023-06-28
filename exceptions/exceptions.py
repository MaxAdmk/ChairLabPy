"""
This module is needed for lab №10
"""


class HeightOutOfRangeException(Exception):
    def __init__(self, message="Height is out of range"):
        self.message = message
        super().__init__(self.message)


class AdjustPositionError(Exception):
    def __init__(self, message="Error occurred while adjusting position"):
        self.message = message
        super().__init__(self.message)
