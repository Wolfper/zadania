#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#Python version: 3.3
exercise: 16
site: http://www.ling.gu.se/~lager/python_exercises.html

Write a function filter_long_words()
that takes a list of words and an integer n and returns
the list of words that are longer than n.
"""

import unittest

__author__ = 'Paweł Hały'


def filter_long_words(list_words, var_n):
    '''
    Function that takes a list of words and an integer n and returns
    the list of words that are longer than n.
    '''
    result = list(filter(lambda x: len(x) > var_n, list_words))
    return ", ".join(result)


class filter_long_wordsTestCase(unittest.TestCase):
    '''
    unittest function filter_long_words
    '''
    def test_Success(self):
        '''
        test
        '''
        result = filter_long_words(['dom', 'kot', 'mlotek', 'placek'], 3)
        self.assertEqual(result, 'mlotek, placek')

    def test_Failure(self):
        '''
        test
        '''
        result = filter_long_words(['dom', 'kot', 'mlotek', 'placek'], 3)
        self.assertNotEqual(result, 'dom, kot')

if __name__ == "__main__":
    print(filter_long_words(['dom', 'kot', 'mlotek', 'placek'], 2))
    unittest.main()

