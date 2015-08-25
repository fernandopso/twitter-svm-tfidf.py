#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-

import re
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk import bigrams, trigrams

stopwords = nltk.corpus.stopwords.words('portuguese')
tokenizer = RegexpTokenizer("[\w’]+", flags=re.UNICODE)

class FormatFile:
	def formatFile(self, tupleTweetTrain, tupleTweetTest, listWords, idfs, *args):
		vector_train = list()
		train_prediction = list()
		vector_test = list()

		print "Processando dados de treinamento..."
		for tupla in tupleTweetTrain:
			rotulo = tupla["rotulo"]
			tweet = tupla["tweet_tratado"]
			line = self.formatLine(tweet, listWords, idfs)
			train_prediction.append(int(rotulo))
			vector_train.append(line)
		print "Dados de Treinamento Processado.\nProcessando dados de teste..."

		for tupla in tupleTweetTest:
			tweet = tupla["tweet_tratado"]
			line = self.formatLine(tweet, listWords, idfs)
			vector_test.append(line)
		print "Dados de Teste Processado"

		return vector_train, train_prediction, vector_test		

	def formatLine(self, tweet, listWords, idfs, *args):
		tkns = tokenizer.tokenize(tweet)
		tkns = [tkn.lower() for tkn in tkns if len(tkn) > 2]
		tkns = [tkn for tkn in tkns if tkn not in stopwords]
		tokens = []
		tokens.extend(tkns)
		tokens.sort()

		line = list()
		for word in listWords:
			if word not in tokens:
				line.append(int(0))
			else:
				idf = self.pesoIdfs(word, idfs)
				line.append(float(idf))
				
		return line

	def pesoIdfs(self, word, idfs, *args):
		for idf in idfs:
			try:
				peso = idf[word]
				return peso
			except:
				pass