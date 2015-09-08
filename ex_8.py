#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#Python version: 3.3
exercise: 8
site: http://www.ling.gu.se/~lager/python_exercises.html

Define a function is_palindrome() that recognizes
palindromes (i.e. words that look the same written backwards).
For example, is_palindrome("radar") should return True.
"""

import unittest

__author__ = 'Paweł Hały'


def is_palindrome(word):
    '''
    Arguments:
    word => string

    if word == "reverse word":
        return True
    else:
        return False

    :return: True or False
    '''
    word = word.lower()
    reverse_word = word[::-1]

    if word == reverse_word:
        return True
    else:
        return False


class is_palindromeTestSace(unittest.TestCase):
    '''
    Unittest function is_palindrome
    '''
    def test_Success(self):
        '''
        Check if word == "reverse word"
        '''
        result = is_palindrome('radar')
        self.assertEqual(result, True)

    def test_Failure(self):
        '''
        Check if word != "reverse word"
        '''
        result = is_palindrome('dog')
        self.assertNotEqual(result, True)


if __name__ == "__main__":
    unittest.main()