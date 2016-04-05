# !/usr/bin/env python
# -*- coding: utf-8 -*-
from app.cli import Cli

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
        cli.training_title()

        for t in self.tweets:
            print "@%s say:" % t['user']
            print "\n"
            print t['original']

            cli.training()

            evaluation = cli.waiting_input()
            t['evaluation'] = evaluation[0]

            if t['evaluation'] != 4:
                self.tuples.append(t)

            cli.divider()

        cli.clear_terminal()
        cli.dashboard()

        return self.tuples
