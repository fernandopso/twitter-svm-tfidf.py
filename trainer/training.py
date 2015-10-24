# !/usr/bin/env python
# -*- coding: utf-8 -*-
from cli import Cli

from processing import Processing

class Training(object):

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
                'processed': Processing(data['text']).execute(),
                'evaluation': 0
            }
            self.tweets.append(t)

        return self.tweets

    def evaluate(self):
        """
        Display all tweets collected for training
        """
        self.process_tweets()
        cli = Cli()

        for t in self.tweets:
            print "@%s: %s" % (t['user'], t['original'])

            cli.training()

            t['evaluation'] = cli.waiting_input()

            if t['evaluation'] != 4:
                self.tuples.append(t)

        return self.tuples
