#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))
    r = Rectangle(2, 5, 10, 12, 3)
    r2 = Rectangle(3, 12, 5, 2, 1)
    print(len(Base.to_json_string([r.to_dictionary(), r2.to_dictionary()])))
    s = Square(2, 5, 10, 12)
    s2 = Square(14, 5, 22, 70)
    print(len(Base.to_json_string([s.to_dictionary(), s2.to_dictionary()])))
    
