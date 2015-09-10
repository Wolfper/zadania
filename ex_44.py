#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#Python version: 3.3
exercise: 44
site: http://www.ling.gu.se/~lager/python_exercises.html

Your task in this exercise is as follows:
    Generate a string with N opening brackets ("[") and N closing
    brackets ("]"), in some arbitrary order. Determine whether
    the generated string is balanced; that is, whether it consists
    entirely of pairs of opening/closing brackets (in that order),
    none of which mis-nest.

Examples:
   []        OK   ][        NOT OK
   [][]      OK   ][][      NOT OK
   [[][]]    OK   []][[]    NOT OK
"""

import random

__author__ = 'Pawel'


def is_balanced(final_brackets):
    """

    :param final_brackets: list brackets
    :return:
    """
    if len(final_brackets) % 2 != 0:
        final_brackets.extend(random.choice(['[', ']']))

    if final_brackets[0] == '[' and final_brackets[-1] == ']':
        count = 1
        lenth_final_brackets = len(final_brackets)
        for x in final_brackets[1:-1]:
            if count < lenth_final_brackets:
                if x == "[":
                    if final_brackets[count + 1] == "]":
                        count += 1
                        continue
                    else:
                        print("NOT OK")
                        break
                elif x == "]":
                    if final_brackets[count+1] == "[":
                        count += 1
                        continue
                    else:
                        print("NOT OK")
                        break
                else:
                    print("NOT OK")
            else:
                print("OK")
        else:
            print("OK")
    else:
        print("NOT OK")


def bracket(word):

    brackets = ['[', ']']
    N_brackets = []

    try:
        N_brackets.extend(random.choice(brackets))
        N_brackets.extend(random.choice(brackets) for character in word if character == 'N')
        N_brackets.extend(random.choice(brackets))
    except IndexError:
        N_brackets = [random.choice(brackets)for _ in range(2)]

    if len(N_brackets) % 2 != 0:
        N_brackets.extend(random.choice(brackets))

    print("".join(N_brackets))
    is_balanced(N_brackets)

if __name__ == '__name__':
    for x in range(30):
        bracket("No")
        print("")
