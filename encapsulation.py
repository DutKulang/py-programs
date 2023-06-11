#!/usr/bin/python3

# __ private variable not access outside of the class
# _ partial private not can not protect the attribute from being accessed from outside of the class.


class Car:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color

    # setter method for speed
    def set_speed(self, new_speed):
        self.__speed = new_speed

    # getter method for speed
    def get_speed(self):
        return self.__speed

    # setter method for color
    def set_color(self, new_color):
        self.__color = new_color

    # getter method for color
    def get_color(self):
        return self.__color


tesla = Car(350, "black")

# will give an error because now color is set to a private attribute
#tesla.color = "red"

print(tesla.get_color()) # black

tesla.set_color("red") # changes the color

print(tesla.get_color()) # now prints the new color


tesla.set_speed(750)
print(tesla.get_speed())
