#-*- coding: utf-8 -*-

from re import UNICODE
import nltk
from nltk.tokenize import RegexpTokenizer
import math

stopwords = nltk.corpus.stopwords.words('portuguese')
tokenizer = RegexpTokenizer("[\w’]+", flags=UNICODE)

class TermFrequency(object):

    def __init__(self, tweets):
        self.tweets     = tweets
        self.vocabulary = []
        self.docs       = {}
        self.idfs       = []
        self.words      = []

    def freq(self, word, doc):
        """
        Calculates frequency of a word in the document
        """
        return doc.count(word)

    def vocabulary_appears(self, word):
        """
        Number of times a word appears in the vocabulary
        """
        count = 0
        for doc in self.vocabulary:
            if self.freq(word, doc):
                count += 1

        if count:
            return count

        else:
            return 1

    def idf(self, word):
        """
        Inverse document frequency calculets the log quantity of documents
        divided by quantity of word in all documents
        """
        frequency = len(self.vocabulary) / float(self.vocabulary_appears(word))

        return math.log(frequency)

    def tf(self, word, doc):
        """
        Term-frequency calcule the quantity of a word in the document
        divided by the number of words in a document
        """
        return (self.freq(word, doc) / float(len(doc)))

    def tf_idf(self, word, doc):
        """
        Term-frequency inverse document frequency
        """
        return (self.tf(word, doc) * self.idf(word))

    def tokenizator(self, text):
        """
        Text processor to generate token list
        """
        tokens = tokenizer.tokenize(text)
        tokens = [token.lower() for token in tokens if len(token) > 2]
        tokens = [token for token in tokens if token not in stopwords]

        return tokens

    def bag_of_words(self):
        """
        Create a bag wof words
        """
        for doc in self.docs:
            for token in self.docs[doc]['tf']:
                self.docs[doc]['idf'][token] = self.idf(token)
                self.docs[doc]['tf-idf'][token] = self.tf_idf(token, self.docs[doc]['tokens'])
                self.idfs.append({token: self.idf(token)})

        return self.idfs

    def word_list(self):
        """
        Create an array of tokens
        """
        for tupla in self.vocabulary:
            for tkn in tupla:
                if tkn not in self.words:
                    self.words.append(tkn)

        self.words.sort()

        return self.words

    def create_vocabulary(self):
        """
        Create vocabulary with all documents trained
        """
        for tweet in self.tweets:
            id = tweet['id']

            tokens = self.tokenizator(tweet['processed'])

            self.docs[id] = {
                'freq': {}, 'tf': {}, 'idf': {}, 'tf-idf': {}, 'tokens': [],
                'evaluation': tweet['evaluation']
            }

            for token in tokens:
                # Frequency computed for each tweet processed
                self.docs[id]['freq'][token] = self.freq(token, tokens)
                # Term-frequency (Normalized Frequency)
                self.docs[id]['tf'][token] = self.tf(token, tokens)
                # Set tokens
                self.docs[id]['tokens'] = tokens

            self.vocabulary.append(tokens)

        return self.bag_of_words(), self.word_list()
