#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-
from re import UNICODE
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer("[\w’]+", flags=UNICODE)

class Vectorizer(object):
    """
    Vectorizer create a list of term frequency–inverse document frequency for
    tweets trained and tweets to classification
    """

    def __init__(self, tweets_trained, tweets_to_classify, words, bag_of_words):
        self.words        = words
        self.bag_of_words = bag_of_words
        self.evaluations  = self.create_list_of_evaluations(tweets_trained)

        self.tfidf_for_tweets_trained     = self.calcule(tweets_trained)
        self.tfidf_for_tweets_to_classify = self.calcule(tweets_to_classify)

    def create_list_of_evaluations(self, tweets_trained):
        """
        Create vectors list of evaluations of tweets trained
        """
        evaluations = list()

        for tupla in tweets_trained:
            evaluations.append(int(tupla["evaluation"]))

        return evaluations

    def calcule(self, tweets):
        """
        Create vectors list of tf-idf for tweets
        """
        vector = list()

        for tweet in tweets:
            vector.append(self.tfidf_calculator(tweet["processed"]))

        return vector

    def tfidf_calculator(self, tweet):
        """
        Create a list of term frequency–inverse document frequency by tweet
        """
        vector = list()
        tokens = tokenizer.tokenize(tweet)

        # TODO: Verify that loop is correct, I suspect that the right is this:
        # for token in tokens:
        #     if token not in self.words:
        for word in self.words:
            if word not in tokens:
                vector.append(int(0))

            else:
                vector.append(float(self.tfidf(word)))

        return vector

    def tfidf(self, word):
        """
        Get tf-idf of word in bag of words
        """
        for term in self.bag_of_words:
            try:
                return term[word]

            except:
                pass