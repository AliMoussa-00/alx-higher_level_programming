#!/usr/bin/python3
"""Defining the 'rectangle' module"""

from models.base import Base


class Rectangle(Base):
    """Defining the 'Rectangle' class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the constructure"""

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""

        if type(width) is not int:
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""

        if type(height) is not int:
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""

        if type(x) is not int:
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""

        if type(y) is not int:
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    def area(self):
        """calc the area of rectangle"""

        return self.height * self.width

    def display(self):
        """Display the rectangle"""

        print("\n" * self.y, end="")

        print((" " * self.x + "#" * self.width + "\n") * self.height, end="")

    def __str__(self):
        """overriding the str function"""

        txt = f"[{self.__class__.__name__}] ({self.id}) "
        txt += f"{self.x}/{self.y} - {self.width}/{self.height}"
        return txt

    def update(self, *args, **kwargs):
        """update the instance attributes"""

        if args and len(args) != 0:

            i = 0
            for arg in args:
                if i == 0 and arg is not None:
                    self.id = arg

                elif i == 1:
                    self.width = arg

                elif i == 2:
                    self.height = arg

                elif i == 3:
                    self.x = arg

                elif i == 4:
                    self.y = arg

                i += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if "id" == k and v is not None:
                    self.id = v

                elif "width" == k:
                    self.width = v

                elif "height" == k:
                    self.height = v

                elif "x" == k:
                    self.x = v

                elif "y" == k:
                    self.y = v

    def to_dictionary(self):
        """the dictionary representation of a Rectangle"""

        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
