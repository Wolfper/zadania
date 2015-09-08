#!/usr/bin/python
#-*- coding: utf- -*-
'''
#Python version: 3.3
exercise: 4
site: http://www.ling.gu.se/~lager/python_exercises.html

Write a function that takes a character (i.e. a string of length 1)
and returns True if it is a vowel, False otherwise.
'''

import unittest


def character_vowel(character):
    '''
    Arguments:
    character => string character

    if character in vowel:
        return True
    else:
        return False

    :return: True or False
    '''

    character = character.lower()
    vowel_character = 'aeoiuy'
    if character in vowel_character:
        return True
    else:
        return False


class Character_vowelTest(unittest.TestCase):
    '''
    Unittest function character_vowel
    '''

    def test_Success(self):
        '''
        Check if character is in vowel
        '''
        result = character_vowel('a')
        self.assertEqual(result, True)

    def test_Failure(self):
        '''
        Check if character is not in vowel
        '''
        result = character_vowel('N')
        self.assertNotEqual(result, True)


if __name__ == "__main__":
    unittest.main()