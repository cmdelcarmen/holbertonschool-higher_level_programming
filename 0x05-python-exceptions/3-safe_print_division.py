#!/usr/bin/python3
'''
    Write a function that divides 2 integers and prints the result.
'''
def safe_print_division(a, b):

    float_result = 0

    try:
        float_result = (a / b)

    except:
        return None

    finally:
        if b == 0:
            print("Inside result: None")
        else:
            print("Inside result: {:.1f}".format(float_result))

    return float_result
