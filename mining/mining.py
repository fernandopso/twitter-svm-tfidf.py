#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tfidf import TermFrequency
from vectorizer import Vectorizer
from modules.svm import Model
from training import Training

class Mining(object):
    """
    Twitter Mining
    """
    def __init__(self, file_test, trained):
        # list of tweets to classify
        self.classify = Training(file_test).process_tweets()

        # list of tweets trained
        self.trained = trained

    def start(self):
        bag_of_words, words = TermFrequency(self.trained).create_vocabulary()

        v = Vectorizer(self.trained, self.classify, words, bag_of_words)

        evaluations = v.evaluations
        tfidf_trained = v.tfidf_for_tweets_trained
        tfidf_to_classify = v.tfidf_for_tweets_to_classify

        #=== STOPPED HERE ====================================================#
        print "Iniciando classicação..."
        appSVM = Model()
        appSVM.svm(tfidf_trained, evaluations, tfidf_to_classify)
        print "Predição de arquivos finalizada!"
