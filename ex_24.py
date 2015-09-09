#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#Python version: 3.3
exercise: 24
site: http://www.ling.gu.se/~lager/python_exercises.html

The third person singular verb form in English is distinguished
by the suffix -s,which is added to the stem of the
infinitive form: run -> runs.
A simple set of rules can be given as follows:

    If the verb ends in y, remove it and add ies
    If the verb ends in o, ch, s, sh, x or z, add es
    By default just add s

Your task in this exercise is to define a function make_3sg_form()
which given a verb in infinitive form returns its third person singular form.
Test your function with words like try, brush, run and fix. Note however that
the rules must be regarded as heuristic, in the sense that you must not expect
them to work for all cases. Tip: Check out the string method endswith().

"""

import unittest

__author__ = 'Paweł Hały'


def make_3sg_form(word):
    """
    Function which given a verb in infinitive form
    returns its third person singular form.

    :param word: string word
    :return: string
    """
    es_suffix = {'o', 'ch', 's', 'sh', 'x'}
    if word.endswith('y'):
        result = word[0:-1] + word[-1].replace('y', 'ies')
    elif word[-1] in es_suffix or word[len(word)-2::] in es_suffix:
        result = word + "es"
    else:
        result = word + "s"
    return result


class Make_3sg_formTestCase(unittest.TestCase):
    '''
    unittest fun make_3sg_form
    '''

    def test_Success(self):
        '''
        test words
        '''
        count = 0
        words = ['try', 'brush', 'run', 'fix']
        good_form = ['tries', 'brushes', 'runs', 'fixes']
        for word in words:
            result = make_3sg_form(word)
            self.assertEqual(result, good_form[count])
            count += 1


if __name__ == "__main__":
    unittest.main()
