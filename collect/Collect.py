#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import psutil

#Libraries for get time
from time import gmtime, strftime

#Libraries for threads.
import thread
import threading

class Collect(object):
    """Collect tweet from Twitter"""

    def __init__(self, term, username, password):
        self.term = term
        self.username = username
        self.password = password

    def start(self):
        tmp = "curl -d track='"+self.term+"' https://stream.twitter.com/1/statuses/filter.json -u "+self.username+":"+self.password+" -o "
        now = strftime("%Y_%b_%d_%H.%M.%S", gmtime())
        cmd = tmp + now

        os.system(cmd)
  
