#!/usr/bin/python3
'''
    Write a program that prints all the names defined by
    the compiled module hidden_4.pyc (please download it locally)
'''
if __name__ == "__main__":

    import hidden_4

    dir_names = dir(hidden_4)

    for count in dir_names:
        if count[:2] != "__":
            print(count)
