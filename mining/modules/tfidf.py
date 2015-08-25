#-*- coding: utf-8 -*-

import re
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk import bigrams, trigrams
import math
import pickle
import json
import simplejson as json

stopwords = nltk.corpus.stopwords.words('portuguese')
tokenizer = RegexpTokenizer("[\w’]+", flags=re.UNICODE)

class tfidf:
    def freq(self, word, doc):
        return doc.count(word)

    def word_count(self, doc):
        return len(doc)

    def tf(self, word, doc):
        return (self.freq(word, doc) / float(self.word_count(doc)))

    def num_docs_containing(self, word, list_of_docs):
        count = 0
        for document in list_of_docs:
            n = self.freq(word, document)
            if n > 0:
                count += 1
        return 1 + count

    def idf(self, word, list_of_docs):
        return math.log(len(list_of_docs) / float(self.num_docs_containing(word, list_of_docs)))

    def tf_idf(self, word, doc, list_of_docs):
        return (self.tf(word, doc) * self.idf(word, list_of_docs))

    def start(self, tupleTweet):

        vocabulary = []
        docs = {}
        idfs = []
        tupleTokens = []

        print "Criando Vocabulario..."
        for tupla in tupleTweet:
            tip = tupla["tweet_tratado"]
            rotulo = tupla["rotulo"] 
            if rotulo != 4:
                tokens = tokenizer.tokenize(tip)
                tokens = [token.lower() for token in tokens if len(token) > 2]
                tokens = [token for token in tokens if token not in stopwords]
                final_tokens = []
                final_tokens.extend(tokens)
                docs[tip] = {'freq': {}, 'tf': {}, 'idf': {},
                                    'tf-idf': {}, 'tokens': [], 'rotulo':rotulo}

                for token in final_tokens:
                    #The frequency computed for each tip
                    docs[tip]['freq'][token] = self.freq(token, final_tokens)
                    #The term-frequency (Normalized Frequency)
                    docs[tip]['tf'][token] = self.tf(token, final_tokens)
                    docs[tip]['tokens'] = final_tokens

                vocabulary.append(final_tokens)

                tupleTokens.append(final_tokens)

        print "Vocabulario: OK\nCriando Bag of Words..."

        for doc in docs:
            for token in docs[doc]['tf']:
                #The Inverse-Document-Frequency
                docs[doc]['idf'][token] = self.idf(token, vocabulary)
                idfs.append({token:docs[doc]['idf'][token]})
                #The tf-idf
                docs[doc]['tf-idf'][token] = self.tf_idf(token, docs[doc]['tokens'], vocabulary)

        listWords = []
        for tupla in tupleTokens:
            for tkn in tupla:
                if tkn not in listWords:
                    listWords.append(tkn)


        print "Bag of Words: OK"

        listWords.sort()
        return idfs, listWords
        