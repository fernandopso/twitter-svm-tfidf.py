#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import environ
from tweepy import OAuthHandler, API
from time import gmtime, strftime
from json import dump

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
        self.consumer_key = environ.get("CONSUMER_KEY", None)
        self.consumer_secret = environ.get("CONSUMER_SECRET", None)
        self.access_token_key = environ.get("ACCESS_TOKEN_KEY", None)
        self.access_token_secret = environ.get("ACCESS_TOKEN_SECRET", None)
        self.api = None
        self.tweets = []

    def connect_with_twitter(self):
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token_key, self.access_token_secret)
        self.api = API(auth)
        return self.api

    def search_tweets(self):
        """"
        reference: https://github.com/tweepy/tweepy/blob/master/tweepy/api.py

        :allowed_param: 'q', 'lang', 'locale', 'since_id', 'geocode', max_id',
        'since', 'until', 'result_type', 'count', 'include_entities', 'from',
        'to', 'source'
        """
        self.tweets = self.api.search(q='ufla')
        return self.tweets

    def save(self):
        file_path = './data/collect/' + strftime("%Y_%m_%d", gmtime())
        outfile = open(file_path, 'a')
        for tweet in self.tweets:
            dump(tweet._json, outfile)
            # This is necessary beacause lib json cannot load many jsons
            # Save a tweet per line and this will work fine
            outfile.write("\n")

        outfile.close()
        return True
