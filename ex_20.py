#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#Python version: 3.3
exercise: 20
site: http://www.ling.gu.se/~lager/python_exercises.html

Represent a small bilingual lexicon as a Python dictionary in the following fashion
{"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"}
and use it to translate your Christmas cards from English into Swedish.
That is, write a function translate() that takes a list of English words and returns a list of Swedish words.
"""

__author__ = 'Paweł Hały'


def translate(eng_list_words):
    '''
    Function translate() that takes a list of English words
    and returns a list of Swedish words

    :param eng_list_words: string or list words
    :return: translate words list
    '''
    base = {"merry": "god",
            "christmas": "jul",
            "and": "och",
            "happy": "gott",
            "new": "nytt",
            "year": "år"}
    if type(eng_list_words) == str:
        eng_list_words = eng_list_words.lower().split()
    translate_list = [base[word] for word in eng_list_words if word in base.keys()]
    print(translate_list)

if __name__ == '__main__':
    eng_list_words = " and AND "
    translate(eng_list_words)
