#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import listdir
from json import loads

from modules.processing import Processing

class Training(object):

    COLLECTION_FOLDER = './data/collect/'
    OPTIONS = ["Positive", "Negative", "Neutral", "Unknown"]

    def __init__(self):
        self.files = listdir(Training.COLLECTION_FOLDER)
        self.tweets = []
        self.tuples = []

    def load_files(self):
        """
        Open all files in directoy data/collect/ and restore json dump
        """
        for json_file_name in self.files:
            with open(Training.COLLECTION_FOLDER + json_file_name, 'r') as data:
                for tweet in data.readlines():
                    self.tweets.append(loads(tweet))

        return self.tweets

    def display_tweets(self):
        """
        Display all tweets collected for training and save in file
        """
        for tweet in self.tweets:
            t = {
                'id': tweet['id'],
                'user': tweet['user']['screen_name'],
                'original': tweet['text'],
                'processed': self.process(tweet['text']),
                'evaluation': 'TODO'
            }

            # TODO: show tweet to user choice an option and save

        return True

    def process(self, tweet):
        p = Processing()
        tweet = p.lower_case(tweet)
        tweet = p.accented_letters(tweet)
        tweet = p.loose_letters(tweet)
        tweet = p.special_characters(tweet)
        tweet = p.similar_words(tweet)
        tweet = p.remove_stopwords(tweet)
        tweet = p.remove_mentions(tweet)
        tweet = p.remove_links(tweet)
        tweet = p.remove_alpha_numeric(tweet)
        tweet = p.remove_solitary_letters(tweet)
        tweet = p.remove_spaces(tweet)
        tweet = p.stemmizator(tweet)

        return tweet
