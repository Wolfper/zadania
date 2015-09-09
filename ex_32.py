#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#Python version: 3.3
exercise: 32
site: http://www.ling.gu.se/~lager/python_exercises.html

Write a version of a palindrome recogniser that accepts a file name
from the user, reads each line, and prints the line
to the screen if it is a palindrome.
"""

__author__ = 'Paweł Hały'


def palindrome(word):
    '''
    Checks if the word what is palindrome

    :param word: word from file
    :return: true if is palindrome else false
    '''
    if word == word[::-1]:
        return True
    else:
        return False


def read_file(name='data_ex_32.txt', readtype='r'):
    '''
    Read file and parse

    :param name: name file
    :param readtype: type read file
    :return: palindrome word and sentence with palindrom
    '''
    special_char = {',', '.', '-', ':', '"', "'"}
    with open(name, readtype) as file:
        list_lines = [line.strip().split() for line in file]
    for line in list_lines:
        for word in line:
            for special_character in special_char:
                word = word.replace(special_character, "")
            if palindrome(word):
                print('\npalindrome: "' + word, end='"\n')
                print(" ".join(line))


if __name__ == "__main__":
    fileName = input("Enter the name file: ")
    read_file(fileName)
