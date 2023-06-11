class Polygon:
    """
    The Polgon class is acting as the parent class that rectangle and triangle classes inherit from

    __width and __height --> are private public attributes and can not be accessed by the child classes
    
    We created getter and setter for each private public attribute so that we can get to modify them from child classes.

    Here the getter and setter are public method of the polygon class.
    """
    __width = None
    __height = None

    def get_width(self):
        return self.__width
    
    def set_width(self, new_width):
        self.__width = new_width

    def get_height(self):
        return self.__height
    
    def set_height(self, new_height):
        self.__height = new_height
