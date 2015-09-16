#!/usr/bin/env python
# -*- coding: utf-8 -*-
from modules.tfidf import tfidf
from modules.fileDir import fileDir
from modules.formatFile import FormatFile
from modules.svm import Model
from modules.check import Check

class Mining:
    """
    Twitter Mining
    """
    list_tweets = []
    def __init__(self):
        if self.file_train == None:
            print "Você não selecionou nenhum arquivo de treinamento."

        if self.file_test == None:
            print "Você não selecionou nenhum arquivo de teste."

    def on_clickedStart(self, *args):
        appOpen = fileDir()
        appTFIDF = tfidf()
        appFormat = FormatFile()
        tupleTweetTrain = []
        tupleTweetTest = []
        listWords = []
        idfs = []

        vector_train = list()
        train_prediction = list()
        vector_test = list()
        
        tupleTweetTrain = appOpen.startTrain(self.file_train)
        print "Tweets Para Treinamento: Ok"
        tupleTweetTest = appOpen.startTest(self.file_test)
        print "Tweets Para Teste: Ok"     
        print "Preparando Dados..."
        idfs, listWords = appTFIDF.start(tupleTweetTrain)
        vector_train, train_prediction, vector_test = appFormat.formatFile(tupleTweetTrain, tupleTweetTest, listWords, idfs)

        #=====================================#
        print "Iniciando classicação..."
        appSVM = Model()
        appSVM.svm(vector_train, train_prediction, vector_test)
        print "Predição de arquivos finalizada!"

        for i in tupleTweetTest:
            self.list_tweets.append(i)
