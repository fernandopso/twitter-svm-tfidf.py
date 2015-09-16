#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tfidf import TermFrequency
from modules.formatFile import FormatFile
from modules.svm import Model

class Mining(object):
    """
    Twitter Mining
    """
    def __init__(self, file_test, file_train):
        self.list_tweets = []
        self.tupleTweetTest = file_test
        self.tupleTweetTrain = file_train
        self.vector_train = list()
        self.train_prediction = list()
        self.vector_test = list()

    def start(self):
        idfs, words = TermFrequency(self.tupleTweetTrain).create_vocabulary()

        #=== STOPPED HERE ====================================================#
        appFormat = FormatFile()
        self.vector_train, self.train_prediction, self.vector_test = appFormat.formatFile(self.tupleTweetTrain, self.tupleTweetTest, words, idfs)

        print "Iniciando classicação..."
        appSVM = Model()
        appSVM.svm(vector_train, train_prediction, vector_test)
        print "Predição de arquivos finalizada!"

        for i in tupleTweetTest:
            self.list_tweets.append(i)
