#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    r1 = Base(None)
    r2 = Base()
    r3 = Base()
    r4 = Base()
    r5 = Base()
    print(Base().id)