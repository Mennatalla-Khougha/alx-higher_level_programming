#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    Rectangle.save_to_file([r1, r2])

    with open("Rectangle.json", "r") as file:
        print(file.read())
        
    s = Square(2, 5)
    s2 = Square(12, 22)
    Square.save_to_file([s, s2])
    with open ("Square.json", 'r') as file:
        print(len(file.read()))
