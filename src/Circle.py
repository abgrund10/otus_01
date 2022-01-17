import math

from src.Figure import Figure


class Circle(Figure):

    def __init__(self, r):
        self.name = "Circle"
        try:
            self.perimeter = 2 * math.pi * r
            self.area = math.pi * r * r
        except (AttributeError, TypeError) as e:
            print("Error occured: ", e)
