#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-

from sklearn import svm
from sklearn import metrics
from sklearn import cross_validation

class Model():
   def svm(self, vector_train, train_prediction, vector_test, *args):
      #Definindo kernel e Produzindo um Modelo de Predição.
      
      clf = svm.SVC(kernel='linear')
      clf.fit(vector_train, train_prediction)


      prediction = clf.predict(vector_test)
      
      """ Para cálcular o índice de acerto, descomentar as três linhas abaixo e comentar a linha acima """
      #prediction_test = clf.predict(vector_train)
      #score = metrics.f1_score(train_prediction, prediction)
      #print score

      prdctn = open('prediction', 'w')
      for i in prediction:
          prdctn.write(str(i)+'\n')

      prdctn.close()


