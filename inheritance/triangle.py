# importing the Polygon class from polygon.py file
from polygon import Polygon
class Triangle(Polygon):
    def area(self):
        return (self.get_height() * self.get_width()) / 2

tria = Triangle()
tria.set_width(50)
tria.set_height(25)

print(tria.area())
