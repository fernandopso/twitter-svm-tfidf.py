#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import environ
from tweepy import OAuthHandler, API

class Collect(object):
    """
    Collect tweet from Twitter

    environments vars:
        --consumer-key    : the twitter consumer key
        --consumer-secret : the twitter consumer secret
        --access-key      : the twitter access token key
        --access-secret   : the twitter access token secret

    required params:
        @arg is a argument for query in Twitter

        Ex.: Collect("python").search()
    """

    def __init__(self, arg):
        self.arg = arg
        self.consumer_key = environ.get("CONSUMER_KEY", None)
        self.consumer_secret = environ.get("CONSUMER_SECRET", None)
        self.access_token_key = environ.get("ACCESS_TOKEN", None)
        self.access_token_secret = environ.get("ACCESS_TOKEN_SECRET", None)
        self.api = self.connect_with_twitter()
        self.tweets = []

    def connect_with_twitter(self):
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token_key, self.access_token_secret)
        self.api = API(auth)
        return self.api

    def search(self):
        """"
        reference:
            https://github.com/tweepy/tweepy/blob/master/tweepy/api.py

        allowed_params:
            'q', 'lang', 'locale', 'since_id', 'geocode', 'since', 'until',
            'result_type', 'count', 'include_entities', 'from', 'to', 'source'
        """
        self.tweets = self.api.search(q=self.arg)
        return self.tweets
