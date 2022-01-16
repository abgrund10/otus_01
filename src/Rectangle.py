from src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, a, b):
        self.name = "Rectangle"
        try:
            self.perimeter = (a + b) * 2
            self.area = a * b
        except (AttributeError, TypeError) as e:
            print("Error occured: ", e)
            self.perimeter = "N/A"
            self.area = "N/A"