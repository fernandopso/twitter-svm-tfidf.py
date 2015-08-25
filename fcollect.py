#!/usr/bin/python
# -*- coding: utf-8 -*-
import twitter_oauth
import os

OAUTH_KEYS = {
    'consumer_key': os.environ.get('CONSUMER_KEY'),
    'consumer_secret': os.environ.get('CONSUMER_SECRET'),
    'access_token_key': os.environ.get('ACCESS_TOKEN_KEY'),
    'access_token_secret': os.environ.get('ACCESS_TOKEN_SECRET')
}

class Fcollect:
    def get_connection(self):
        api = twitter_oauth.Api(
            OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'],
            OAUTH_KEYS['access_token_key'], OAUTH_KEYS['access_token_secret'])

        print api


if __name__ == '__main__':
    fc = Fcollect()
    fc.get_connection()
