#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#Python version: 3.3
exercise: 40
site: http://www.ling.gu.se/~lager/python_exercises.html

An anagram is a type of word play, the result of rearranging
the letters of a word or phrase to produce a new word or phrase,
using all the original letters exactly once; e.g., orchestra = carthorse,
A decimal point = I'm a dot in place. Write a Python program that,
when started 1) randomly picks a word w from given list of words, 2)
randomly permutesw (thus creating an anagram of w), 3) presents
the anagram to the user, and 4) enters an interactive loop in which
the user is invited to guess the original word. It may be a good idea
to work with (say)colour words only.
The interaction with the program may look like so:

>>> import anagram
Colour word anagram: onwbr
Guess the colour word!
black
Guess the colour word!
brown
Correct!
"""

import random

__author__ = 'Pawel'


def anaagram():
    '''
    anagram is a type of word play, the result of rearranging
    the letters of a word or phrase to produce a new word or phrase,
    using all the original letters exactly once; e.g., orchestra = carthorse
    '''
    words = ['black', 'brown', 'red', 'blue']
    is_word = random.choice(words)
    ag_word = "".join(random.sample(is_word, len(is_word)))
    while ag_word == is_word:
        print(ag_word, is_word)
        ag_word = "".join(random.sample(is_word[::-1], len(is_word)))
    print("Colour word anagram: ", ag_word)
    player = None
    while player != is_word:
        player = input("Guess the colour word!\n")
    print("Correct!")


if __name__ == "__main__":
    anaagram()
