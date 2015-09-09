#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#Python version: 3.3
exercise: 28
site: http://www.ling.gu.se/~lager/python_exercises.html

Write a function find_longest_word() that takes a list of words
and returns the length of the longest one. Use only higher order functions.
"""

__author__ = 'Paweł Hały'


def find_longest_word(words_list):
    '''
    Function that takes a list of words
    and returns the length of the longest one
    :param words_list: list words
    :return: lenth longest one word
    '''
    words_sorted = sorted(words_list, key=lambda word: len(word))
    return len(words_sorted[-1])


if __name__ == '__main__':
    words = {'one', 'two', 'three', 'four', 'five', 'six', 'seven'}
    print(find_longest_word(words))
