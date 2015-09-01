#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import tweepy
import pickle

from time import gmtime, strftime

class Collect(object):
    """
    Collect tweet from Twitter

    options:
      --consumer-key    : the twitter consumer key
      --consumer-secret : the twitter consumer secret
      --access-key      : the twitter access token key
      --access-secret   : the twitter access token secret
    """

    def __init__(self):
        self.consumer_key = os.environ.get("CONSUMER_KEY", None)
        self.consumer_secret = os.environ.get("CONSUMER_SECRET", None)
        self.access_token_key = os.environ.get("ACCESS_TOKEN_KEY", None)
        self.access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET", None)
        self.api = None
        self.tweets = []

    def connect_with_twitter(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token_key, self.access_token_secret)
        self.api = tweepy.API(auth)

    def search_tweets(self):
        """"
        reference: https://github.com/tweepy/tweepy/blob/master/tweepy/api.py

        :allowed_param: 'q', 'lang', 'locale', 'since_id', 'geocode', max_id',
        'since', 'until', 'result_type', 'count', 'include_entities', 'from',
        'to', 'source'
        """
        self.tweets = self.api.search(q='ufla')

    def save(self):
        file_path = './data/collect_' + strftime("%Y_%m_%d", gmtime())
        file_trained = open(file_path, 'a')
        for tweet in self.tweets:
            pickle.dump(tweet, file_trained)

        file_trained.close()

