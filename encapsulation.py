#!/usr/bin/python3

class Car:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def set_color(self, new_color):
        self.color = new_color
    def get_color(self):
        return self.color


tesla = Car(350, "black")

print(tesla.color)
