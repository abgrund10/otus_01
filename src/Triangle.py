import math

from src.Figure import Figure

class Triangle(Figure):

    def __init__(self, a, b, c):
        exists = bool
        self.name = "Triangle"
        try:
            if a + b > c and a + c > b and b + c > a:
                exists = True
            else:
                exists = False
                print("It's not a triangle")
        except (AttributeError, TypeError) as e:
            print("Error occured: ", e)
        if exists:
            self.perimeter = a + b + c
            p = self.perimeter / 2
            self.area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        else:
            self.perimeter = "N/A"
            self.area = "N/A"
