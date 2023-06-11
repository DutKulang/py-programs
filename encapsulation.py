#!/usr/bin/python3

# __ private variable/method not access outside of the class
# _ partial private not can not protect the attribute from being accessed from outside of the class.
# self MUST be used to access both private methods and private attributes

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

    # setting a private method
    def __details(self):
        return "color: {:s}\nspeed: {:d}".format(self.__color, self.__speed)

    def get_details(self):
        # Use the self.method_name to access the private methods.
        return self.__details()

tesla = Car(350, "black")

# will give an error because now color is set to a private attribute
#tesla.color = "red"

print(tesla.get_color()) # black

tesla.set_color("red") # changes the color

print(tesla.get_color()) # now prints the new color


tesla.set_speed(750)
print(tesla.get_speed())

print(tesla.get_details())


v8 = Car(260, "grey")
print(v8.get_details())
