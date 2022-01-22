from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


def test_square_positive():
    sq = Square(2)
    assert sq.name == "Square"
    assert sq.area == 4
    assert sq.perimeter == 8

def test_square_negative():
    sq = Square('n')
    assert sq.name == "Square"

def test_circle_positive():
    cir = Circle(1)
    assert cir.name == "Circle"
    assert cir.perimeter == 6.28
    assert cir.area == 3.14

def test_circle_negative():
    cir = Circle('k')
    assert cir.name == "Circle"

def test_rect_positive():
    rect = Rectangle(2, 4)
    assert rect.name == "Rectangle"
    assert rect.perimeter == 6
    assert rect.area == 8

def test_rect_negative():
    rect = Rectangle('k', 6)
    assert rect.name == "Rectangle"

def test_triangle_positive():
    tri = Triangle(13, 14, 15)
    assert tri.name == "Triangle"
    assert tri.perimeter == 6
    assert tri.area == 8

def test_triangle_negative():
    tri = Triangle(13, 14, 150)
    assert tri.name == "Triangle"
