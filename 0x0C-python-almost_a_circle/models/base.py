#!/usr/bin/python3
"""Defining the 'base' module"""

import json
import csv
import turtle
import time


class Base:
    """Defining the 'Base' class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the instance"""

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1

            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        list_dict = []
        if list_objs is not None and list_objs != []:
            for obj in list_objs:

                list_dict.append(obj.to_dictionary())

        data = cls.to_json_string(list_dict)

        with open(cls.__name__ + ".json", "w") as file:
            file.write(data)

    @staticmethod
    def from_json_string(json_string):
        """get the list of objects in the JSON string
            representation json_string
        """

        json_list = []

        if json_string is not None and json_string != "":

            json_list = json.loads(json_string)

        return json_list

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)

        elif cls.__name__ == "Square":
            obj = cls(1)

        else:
            return None

        obj.update(**dictionary)

        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from file containing a
            Json string
            representing a list of dictionary :
            "[{id: 12 ...}, {id: 1, ...}, ...]"
            then create the instances based on the dicts by calling
            ".create()"
        """

        try:
            with open(cls.__name__ + ".json", "r") as file:

                data_str = file.read()

                data_list = Base.from_json_string(data_str)

                list_obj = []
                for data_dict in data_list:

                    list_obj.append(cls.create(**data_dict))

                return list_obj

        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save a list object :[obj1, obj2]: into a '.csv' file"""

        # get a list of objects represented in dictionary: [{id, ..}, {...}...]
        list_dict = []
        fieldnames = []

        with open(cls.__name__ + ".csv", "w") as file:

            if list_objs is None or list_objs == []:
                file.write("[]")

            else:
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())

                fieldnames = list(list_dict[0].keys())

                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(list_dict)

    @classmethod
    def load_from_file_csv(cls):
        """load data from a 'file.csv' and return a list of objects"""

        try:
            # reading lines from '.csv' file to a list of lists:
            # list = [[id, width, ..], [1, 12, ..], ...]
            with open(cls.__name__ + ".csv", "r") as file:

                reader = csv.reader(file)

                list_data = []

                for row in reader:
                    list_data.append(row)

            # creating a list of dictionary:
            # [[id, w, ...], [1, 12, ...], ...] ==> [{'id': 1, 'w': 12,..},...]
            list_dict = []
            for i in list_data[1:]:
                obj_dict = {}

                for index, value in enumerate(i):
                    obj_dict[list_data[0][index]] = int(value)

                list_dict.append(obj_dict)

            # creating objects instances from previous list of dicts
            list_obj = []

            for obj_dict in list_dict:

                list_obj.append(cls.create(**obj_dict))

            return list_obj

        except Exception as e:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""

        list_rect_dicts = []
        for rec in list_rectangles:
            list_rect_dicts.append(rec.to_dictionary())

        list_sq_dicts = []
        for sq in list_squares:
            list_sq_dicts.append(sq.to_dictionary())

        # drawing
        sc = turtle.Screen()
        tr = turtle.Turtle()
        tr.speed(3)
        tr.fillcolor("green")

        for rect in list_rect_dicts:
            tr.setposition(rect["x"], rect["y"])
            tr.begin_fill()

            for i in range(2):
                tr.fd(rect["width"])
                tr.right(90)
                tr.fd(rect["height"])
                tr.right(90)

            tr.end_fill()
            time.sleep(1)

            tr.clear()

        for sq in list_sq_dicts:
            tr.setposition(sq["x"], sq["y"])
            tr.begin_fill()

            for i in range(4):
                tr.fd(sq["size"])
                tr.right(90)

            tr.end_fill()
            time.sleep(1)
