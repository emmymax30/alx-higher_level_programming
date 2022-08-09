"""
   module to create a square class from rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
       Square - Square class
                __width (int): width of the square
                __height (int): height of the square.
                __x (int): x.
                __y (int): y.
                size (int): size of the square
                           NB: size = height = width
                area(): calculate area of the square.
                display(): print the square with #.
                __str__(): [Square] (<id>) <x>/<y> - <size>
                update(): updates the value of id, width, height, x and y
                            with args, otherwise kwargs.
       Args:
           width: width of the square.
           height: height of the square.
           x: co-ordinate x.
           y: co-ordinate y.
       Raises:
           TypeError: <name of the attribute> must be an integer.
           ValueError: <name of the attribute> must be > 0.
           ValueError: <name of the attribute> must be >= 0.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Prints string when instance is called by name """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """ Update by assigning the args or kwargs to attrs """
        if args:
            if len(args) == 4:
                self.id = args[0]
                self.width = self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            if len(args) == 3:
                self.id = args[0]
                self.width = self.height = args[1]
                self.x = args[2]
            if len(args) == 2:
                self.id = args[0]
                self.width = self.height = args[1]
            if len(args) == 1:
                self.id = args[0]
        else:
            if kwargs.__contains__("id"):
                self.id = kwargs.get("id")
            if kwargs.__contains__("size"):
                self.width = self.height = kwargs.get("size")
            if kwargs.__contains__("x"):
                self.x = kwargs.get("x")
            if kwargs.__contains__("y"):
                self.y = kwargs.get("y")

    def to_dictionary(self):
        """ returns dictionary representation of square """
        return {'id': self.id, 'size': self.width, 'x': self.x,
                'y': self.y}
