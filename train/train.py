#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import listdir
from json import loads

from modules.Alert import Alert
from modules.Processing import Processing
from modules.SaveTweet import SaveTweet
from modules.LangDetect import LangDetect 

class Train(object):

    COLLECTION_FOLDER = './data/collect/'
    OPTIONS = ["Positive", "Negative", "Neutral"]

    n = 0

    def __init__(self):
        self.files = listdir(Train.COLLECTION_FOLDER)
        self.tweets = []
        self.tuples = []

    def load_files(self):
        """
        Open all files in directoy data/collect/ and restore json dump
        """
        for json_file in self.files:
            with open(Train.COLLECTION_FOLDER + json_file, 'r') as f:
                dump = loads(f.read())
                self.process(dump)


    def process(self, tweets):
        import ipdb; ipdb.set_trace()
        for tweet in tweets:
            #obtem dados do Tweet.
            tweetOriginal = json.dumps(decoded["text"])
            tweetTratado = ""
            idTweet = json.dumps(decoded["id"])
            nameUser = json.dumps(decoded["user"])
            decodedUser = json.loads(nameUser)
            lang = str(json.dumps(decodedUser["lang"]))
            nomeUsuario = json.dumps(decodedUser["screen_name"])

            #Adiciona \n no tweet para melhor visualização na TextView.
            tweetOriginal = self.wordAccented(tweetOriginal)
            tweetOriginal = self.convertTweet(tweetOriginal)

            #Cria uma tupla de infos do tweet.
            tupla = {'id':idTweet, 'nome_usuario':nomeUsuario, 'tweet_original':tweetOriginal, 'tweet_tratado':tweetTratado}

            if lang.find('pt') > -1:
                #Salva uma lista de tuplas e uma lista de tweet_text.
                self.tuples.append(tupla)
                self.tweets.append(tweetOriginal)

        arquive.close()
        
        ## Inicializa na tela com o primeiro tweet.
        tweet = self.tuples[self.n]
        tweetOriginal = tweet['tweet_original']
        self.buf.set_text('')
        self.buf.set_text(self.buf.get_text(*self.buf.get_bounds())+tweetOriginal)

    def ao_clicar_num_botao(self, botao, i):
        tweet = self.tuples[self.n]
        tweetOriginal = tweet['tweet_original']
        tweetTratado = self.execute(tweetOriginal)
        userName = tweet['nome_usuario']
        idTweet = tweet['id']
        tupla = {'tweet_original':tweetOriginal, 'tweet_tratado':tweetTratado, 'nome_usuario':userName, 'id':idTweet, 'rotulo':i}
        self.recordTuples(tupla, i)

        #Imprime próximo tweet na tela.
        self.n += 1
        self.buf.set_text('')
        tweet = self.tuples[self.n]
        tweetOriginal = tweet['tweet_original']
        self.buf.set_text(self.buf.get_text(*self.buf.get_bounds())+tweetOriginal)

        ## Loop ##
        if self.loop:
            self.escolha = number
            self.loop.quit()

    def recordTuples(self, tweet, i):
        appSave = SaveTweet()
        appSave.savePickle(tweet)
        #appSave.saveMongo(tweet, i)

    def execute(self, tweet):
        # Método para tratar o texto do tweet.
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
