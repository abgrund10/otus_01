class Figure:
    def __init__(self, name, area, perimeter):
        """Class constructor"""
        self.name = name
        self.area = area
        self.perimeter = perimeter

    def add_area(self, figure):
        try:
            self.area + figure.area
        except ValueError:
            raise ValueError("ValueError exception thrown")
