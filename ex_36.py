#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#Python version: 3.3
exercise: 36
site: http://www.ling.gu.se/~lager/python_exercises.html

A hapax legomenon (often abbreviated to hapax) is a word which occurs
only once in either the written record of a language, the works of an author,
or in a single text. Define a function that given the file name of a text
will return all its hapaxes. Make sure your program ignores capitalization.
"""


def hapax(filename='data_ex36.txt'):
    '''
    Function that given the file name of a text
    will return all its hapaxes
    '''
    words_list = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().split()
            words_list += line
    words_list = list(map(lambda word: word.lower(), words_list))
    frequency_words = {key: 0 for key in words_list}
    for word in words_list:
        frequency_words[word] += 1
    for word in frequency_words:
        if frequency_words[word] == 1:
            print(word)


if __name__ == '__main__':
    hapax('data_ex36.txt')
