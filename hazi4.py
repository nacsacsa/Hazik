#!/usr/bin/env python
# coding: utf8

def DivByZero():
    while 0 < 1:
        a = int(input("Enter 'a' value: "))
        b = int(input("Enter 'b' value: "))
        try:
            c = a/b
            print(c)
        except ZeroDivisionError:
            print("Division by zero not allowed")
        finally:
            print("Out of try except blocks")

if __name__ == "__main__":
	DivByZero()