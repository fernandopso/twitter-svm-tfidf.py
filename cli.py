# !/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import sys

class Cli(object):
    """Command-line Application"""

    file_path = './locale/en.yaml'

    def __init__(self):
        self.text = yaml.load(open(self.file_path).read())
        self.option = False
        self.args = []

    def dashboard(self):
        print self.text['dashboard']

    def waiting_input(self):
        raw = raw_input("Type an option: ")
        self.option = raw.split()[0]
        self.args   = raw.split()[1:]
        return self.option, self.args

    def training(self):
        print self.text['training']

    def clear_terminal(self):
        sys.stderr.write("\x1b[2J\x1b[H")

    def finished(self):
        print 'Finished'

    def help(self):
        print self.text['help']

    def tweets_colleted(self, tweets):
        for tweet in tweets:
            print self.text['tweet'].format(
                username = tweet['user']['screen_name'],
                tweet    = tweet['text'].encode('ascii', 'ignore'),
                date     = tweet['created_at']
            )

    def tweets_trained(self, tweets, evaluation = False):
        for tweet in tweets:
            if evaluation:
                if evaluation == tweet['evaluation']:
                    print self.text['tweet_trained'].format(
                        username   = tweet['user'],
                        tweet      = tweet['original'].encode('ascii', 'ignore'),
                        evaluation = tweet['evaluation']
                    )

            else:
                print self.text['tweet_trained'].format(
                    username   = tweet['user'],
                    tweet      = tweet['original'].encode('ascii', 'ignore'),
                    evaluation = tweet['evaluation']
                )

    def tweets_metrics(self, collected, trained):
        quantity_collected = len(collected)
        quantity_trained   = len(trained)

        print self.text['metrics'].format(
            total   = quantity_collected,
            trained = quantity_trained,
            predict = quantity_collected - quantity_trained
        )
