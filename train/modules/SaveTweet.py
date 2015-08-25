#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import Connection, ASCENDING

import pickle

class SaveTweet(object):
	def savePickle(self, tweet):
		#Salva uma versão em arquivo.
		file_treinado = open('file_treinado.pck', 'a')
		pickle.dump(tweet, file_treinado)
		file_treinado.close()

	def saveMongo(self, tweet, i):
		#Conecta com o servidor local.
		connection = Connection('localhost', 27017)
		
		#Cria um database com nome 'tweets'.
		db = connection['tweets']

		if i == 1:
			#Recebe coleção de tweets.
			positivo = db.positivo
			positivo.insert(tweet)

		elif i == 2:
			#Recebe coleção de tweets.
			negativo = db.negativo
			negativo.insert(tweet)

		elif i == 3:
			#Recebe coleção de tweets.
			neutro = db.neutro
			neutro.insert(tweet)
			