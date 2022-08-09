"""
   Module to create a rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
       Rectangle - Rectangle class
       Attribute:
                __width (int): width of the rectangle.
                __height (int): height of the rectangle.
                __x (int): x.
                __y (int): y.
                area(): calculate area of the rectangle.
                display(): print the retangle with #.
                __str__(): [Rectangle] (<id>) <x>/<y> - <width>/<height>
                update(): updates the value of id, width, height, x and y
                            with args, otherwise kwargs.
                to_dictionary(): convert attributes to dictionary
       Args:
           width: width of the rectangle.
           height: height of the rectangle.
           x: co-ordinate x.
           y: co-ordinate y.
       Raises:
           TypeError: <name of the attribute> must be an integer.
           ValueError: <name of the attribute> must be > 0.
           ValueError: <name of the attribute> must be >= 0.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ Calculate the area of the rectangle """
        return self.__height * self.__width

    def display(self):
        """ Prints out the rectangle with character # """
        if self.__y > 0:
            print("\n" * self.__y, end="")
        for i in range(0, self.__height):
            if self.__x > 0:
                print(" " * self.__x, "#" * self.__width)
            else:
                print("#" * self.__width)

    def __str__(self):
        """ Prints out when instance is called with name """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """
           Updates the value of id, width, height, x and y
           args is used to update when specified, otherwise kwargs is used
        """
        if args:
            if len(args) == 5:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            if len(args) == 4:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            if len(args) == 3:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
            if len(args) == 2:
                self.id = args[0]
                self.__width = args[1]
            if len(args) == 1:
                self.id = args[0]
        else:
            if kwargs.__contains__("id"):
                self.id = kwargs.get("id")
            if kwargs.__contains__("width"):
                self.__width = kwargs.get("width")
            if kwargs.__contains__("height"):
                self.__height = kwargs.get("height")
            if kwargs.__contains__("x"):
                self.__x = kwargs.get("x")
            if kwargs.__contains__("y"):
                self.__y = kwargs.get("y")

    def to_dictionary(self):
        """ Return the dictionary representation of attrs """
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
