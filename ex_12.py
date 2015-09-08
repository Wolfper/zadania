#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#Python version: 3.3
exercise: 12
site: http://www.ling.gu.se/~lager/python_exercises.html

Define a procedure histogram() that
takes a list of integers and prints a histogram to the screen.
For example, histogram([4, 9, 7]) should print the following:
    ****
    *********
    ******
"""

__author__ = 'Paweł Hały'


def histogram(var_list):
    '''
    Change number from list on "*" and funtion will create histogram

    var_list => list of integer
    '''
    for number in var_list:
        print("*" * number)
    # list(map(lambda x : print("*" * x), var_list))


if __name__ == "__main__":
    histogram([3, 4, 5])