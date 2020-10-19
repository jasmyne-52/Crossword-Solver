#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "Jasmyne Ford with help from Bethsheba"


def getDictionary():

    dictionaryOpen = open('dictionary.txt', 'r')
    dictionary = dictionaryOpen.read().split()
    dictionaryOpen.close()
    return dictionary


dictionary = getDictionary()


def checkWord(testword, dictionary):
    nonBlanks = len(testword)-testword.count(' ')
    for word in dictionary:
        incLetter = 0
        incMatch = 0
        if len(word) == len(testword):
            for letter in testword:
                if letter == " ":
                    incLetter += 1
                elif letter == word[incLetter]:
                    incLetter += 1
                    incMatch += 1
                else:
                    incLetter += 1
        if incMatch == nonBlanks:
            print(word)
    return


def main():
    testword = input(
        'Please enter a word to solve.\nUse spaces to signify unknown letters: ').lower()
    getDictionary()
    checkWord(testword, dictionary)


if __name__ == '__main__':
    main()

