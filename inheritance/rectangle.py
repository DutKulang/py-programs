# importing the Polygon class from polygon.py file
from polygon import Polygon

class Rectangle(Polygon):
    def area(self):
        return self.get_height() * self.get_width()

rect = Rectangle()
rect.set_width(23)
rect.set_height(19)

print(rect.get_width())
