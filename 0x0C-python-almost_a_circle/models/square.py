#!/usr/bin/python3
"""Defining the 'square' module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defining the 'Square' class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instanciating the class instance"""

        super().__init__(id=id, width=size, height=size, x=x, y=y)

    def __str__(self):
        """Implementing the str() function"""

        return f"[{self.__class__.__name__}] ({self.id}) " +\
            f"{self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """getter of the size attr"""
        return self.width

    @size.setter
    def size(self, value):
        """setter of the size attr"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updating the instance attrs"""

        if args and len(args) != 0:
            s_args = list(args)

            if len(args) >= 2:
                s_args.insert(1, args[1])

            super().update(*s_args)

        elif kwargs and len(kwargs) != 0:
            s_kwargs = kwargs

            if "size" in kwargs.keys():
                s_kwargs["width"] = s_kwargs["size"]
                s_kwargs["height"] = s_kwargs.pop("size")

            super().update(**s_kwargs)

    def to_dictionary(self):
        """the dictionary representation of a Square"""

        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
