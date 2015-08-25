# This Python file uses the following encoding: utf-8#
#!/usr/bin/python

import pickle
import json
import simplejson as json

from subModules.Processing import Processing

class fileDir:
	def startTrain(self, caminho):
		tupleTweetTrain = []
		file_addres = open(caminho, 'rb')
		try:
			try:
				while True:
					list = pickle.load(file_addres)
					tupleTweetTrain.append(list)
			except:
				pass
		except:
			pass
		file_addres.close()

		return tupleTweetTrain

	def startTest(self, caminho):
		tupleTweetTest = []
		data_file = open(caminho, 'rb')
		listTweets = data_file.readlines()
		for tweet in listTweets:
			valor = tweet.find("text")
			if valor > 0:
				try:
					decoded = json.loads(tweet)
					tweetOriginal = json.dumps(decoded["text"])
					tweetTratado = self.execute(tweetOriginal)
					idTweet = json.dumps(decoded["id"])
					nameUser = json.dumps(decoded["user"])
					decodedUser = json.loads(nameUser)
					nomeUsuario = json.dumps(decodedUser["screen_name"])
					tupla = {'id':idTweet, 'nome_usuario':nomeUsuario, 'tweet_original':tweetOriginal, 'tweet_tratado':tweetTratado, 'rotulo':0}
					tupleTweetTest.append(tupla)

				except:
					pass

		data_file.close()
		return tupleTweetTest

	def execute(self, tweet):
		#Método para tratar o texto do tweet.
		appProcessing = Processing()
		tweet = appProcessing.lowerCased(tweet)
		tweet = appProcessing.accentedLetters(tweet)
		tweet = appProcessing.looseLetters(tweet)
		tweet = appProcessing.specialCharacters(tweet)
		tweet = appProcessing.similarWords(tweet)
		tweet = appProcessing.removeStopWords(tweet)
		tweet = appProcessing.removeMention(tweet)
		tweet = appProcessing.removeLinks(tweet)
		tweet = appProcessing.alphaNumeric(tweet)
		tweet = appProcessing.solitaryLatters(tweet)
		tweet = appProcessing.removeSpace(tweet)
		tweet = appProcessing.stemmizar(tweet)
		return tweet