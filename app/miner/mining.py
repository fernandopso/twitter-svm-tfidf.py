#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models import Models
from tfidf import TermFrequency
from vectorizer import Vectorizer

class Mining(object):
    """
    Twitter Mining
    """
    def __init__(self, classify, trained):
        # list of tweets to classify
        self.classify = classify

        # list of tweets trained
        self.trained = trained

    def start(self):
        bag_of_words, words = TermFrequency(self.trained).create_vocabulary()

        v = Vectorizer(self.trained, self.classify, words, bag_of_words)

        tfidf_trained     = v.tfidf_for_tweets_trained
        evaluations       = v.evaluations
        tfidf_to_classify = v.tfidf_for_tweets_to_classify

        models     = Models(tfidf_trained, evaluations, tfidf_to_classify)
        prediction = models.svm_linear()

        return prediction
