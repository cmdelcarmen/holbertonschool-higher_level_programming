#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

        print("DEBUGGING: 10, (string)2. -> height TypeError")
        try:
            Rectangle(10, "2")
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
        print()

        print("DEBUGGING: width = -10-> width ValueError")
        try:
            r = Rectangle(10, 2)
            r.width = -10
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
        print()

        print("DEBUGGING: x = None -> x TypeError")
        try:
            r = Rectangle(10, 2)
            r.x = {}
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
        print()

        print("DEBUGGIN: y = -1 -> ValueError")
        try:
            Rectangle(10, 2, 3, -1)
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
