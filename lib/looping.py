#!/usr/bin/env python3

def happy_new_year():
    i = 10
    for i in range(10, 0,-1):
        print(i)
        i -= 1
    print('Happy New Year!')

happy_new_year()

def square_integers(int_list):
    return [ints ** 2 for ints in int_list]


def fizzbuzz():
    for i in range(1,101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)
