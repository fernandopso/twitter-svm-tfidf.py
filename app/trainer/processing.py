# !/usr/bin/env python
# -*- coding: utf-8 -*-

import Stemmer

import pt_br_mapper as constants

class Processing(object):
    """
    All methods has more sense for Portuguese-BR language
    """

    def __init__(self, tweet):
        self.tweet = tweet

    def execute(self):
        """
        Execute all processes to reduce ambiguities
        """
        self.lower_case()
        self.accented_letters()
        self.double_letters()
        self.special_characters()
        self.similar_words()
        self.remove_mentions()
        self.remove_links()
        self.remove_solitary_letters()

        return self.tweet

    def lower_case(self):
        """
        All words in case letters
        """
        self.tweet = self.tweet.lower()

        return self.tweet

    def accented_letters(self):
        """
        Change all accented letters for unaccented
        """
        for key in constants.UNICODE_ACCENTED_LETTERS.keys():
            value = constants.UNICODE_ACCENTED_LETTERS[key]
            self.tweet = self.tweet.replace(key, value)

    	return self.tweet

    def double_letters(self):
        """
        Many words are written with double letters

        important!
            The double letters rr, ss and oo not considered in this case,
            this role has more sense for tweet portugues-br
        """
        wordList = self.tweet.split()

        for key in constants.DOUBLE_LETTERS.keys():
            while self.tweet.find(key) != -1:
                for word in wordList:
                    if word.find(key) != -1:
                        value = constants.DOUBLE_LETTERS[key]
                        self.tweet = self.tweet.replace(key, value)

        return self.tweet

    def special_characters(self):
        """
        Special characters are letters that make no sense to human readable
        """
        for key in constants.SPECIAL_CHARACTERS.keys():
            value = constants.SPECIAL_CHARACTERS[key]
            self.tweet = self.tweet.replace(key, value)

        return self.tweet

    def similar_words(self):
        """
        Many words are written the way they are pronounced or using analogies
        with other small words
        """
        word_list = self.tweet.split()

        for word in word_list:
            for key in constants.SIMILAR_WORDS.keys():
                if (len(key.strip()) == len(word.strip())) and (word == key):
                    value = constants.SIMILAR_WORDS[key]
                    self.tweet = self.near(self.tweet, key, value)

        return self.tweet

    def remove_mentions(self):
        """
        Remove mentions
        """
        if self.tweet.find('@') != -1:
            self.tweet = self.remove(self.tweet, '@')

        return self.tweet

    def remove_links(self):
        """
        Remove links
        """
        if self.tweet.find('http') != -1:
            self.tweet = self.remove(self.tweet, 'http')

        return self.tweet

    def remove_solitary_letters(self):
        """
        Solitary letters can be removed
        """
        for key in constants.SOLITARY_LETTERS:
    		self.tweet = self.near(self.tweet, key, '')

    	return self.tweet

    def remove_word(self, tweet, stopword):
        if tweet != None:
            t = ''

            for word in tweet.split():
                if word == stopword:
                    pass
                else:
                    t += word + ' '

            return t

        else:
            pass

    def remove(self, tweet, key):
        t = ''
        for word in tweet.split():
            if word.find(key) != -1:
                pass
            else:
                t += word + ' '

        return t

    def near(self, tweet, key, value):
        t = ''

        for word in tweet.split():
            if word == key:
                t += value + ' '
            else:
                t += word + ' '

        return t
