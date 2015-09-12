#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cli import Cli

from modules.processing import Processing

class Training(object):

    OPTIONS = ["Positive", "Negative", "Neutral", "Unknown"]

    def __init__(self, datas):
        self.datas  = datas
        self.tweets = []
        self.tuples = []

    def process_tweets(self):
        """
        Process all tweets collected
        """
        for data in self.datas:
            t = {
                'id': data['id'],
                'user': data['user']['screen_name'],
                'original': data['text'],
                'processed': self.process(data['text']),
                'evaluation': 0
            }
            self.tweets.append(t)

        return self.tweets

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

    def evaluate(self):
        """
        Display all tweets collected for training
        """
        self.process_tweets()
        cli = Cli()

        for t in self.tweets:
            print "@%s: %s" % (t['user'], t['original'])

            cli.training()
            rate = cli.waiting_input()

            t['evaluation'] = rate

            self.tuples.append(t)

        return self.tuples
