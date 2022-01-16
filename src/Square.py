from src.Figure import Figure

class Square(Figure):

    def __init__(self, a):
        self.name = "Square"
        try:
            self.perimeter = a * 4
            self.area = a * a
        except (AttributeError, TypeError) as e:
            print("Error occured: ", e)
            self.perimeter = "N/A"
            self.area = "N/A"