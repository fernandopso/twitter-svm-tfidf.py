#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-

from sklearn import svm

class Models(object):
    def __init__(self, trained, evaluations, classify):
        self.trained     = trained
        self.evaluations = evaluations
        self.classify    = classify
        self.result      = list()

    def svm_linear(self):
        """
        Classification tweets with linear Support Vector Machine
        """
        classification = svm.SVC(kernel='linear')
        classification.fit(self.trained, self.evaluations)

        prediction = classification.predict(self.classify)

        for p in prediction:
            self.result.append(p)

        print "\n##############################################################"
        print "The classification result of %d tweets is:\n" % len(self.result)

        print "Positive: %d tweets" % self.result.count(1)
        print "Negative: %d tweets" % self.result.count(2)
        print "Neutral: %d tweets" % self.result.count(3)
        print "Unknown: %d tweets" % self.result.count(4)

        return prediction
