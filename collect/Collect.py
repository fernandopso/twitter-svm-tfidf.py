#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import psutil

#Libraries for Interface Grafics
import gtk, gobject, glib
import pygtk
pygtk.require('2.0')

#Libraries for get time
import time
from time import sleep
from time import gmtime, strftime

#Libraries for threads.
import thread
import threading
import gobject
gtk.gdk.threads_init()
gobject.threads_init()

class Collect(gtk.Window, threading.Thread):
    """docstring for Coletar"""
    stopthread = threading.Event()
    def __init__(self):
        super(Collect, self).__init__()

        self.set_title("Coletar Dados")
        self.set_size_request(500, 280)
        self.set_position(gtk.WIN_POS_CENTER)

        fixed = gtk.Fixed()

        #Label of indentification of the search term
        self.label_termo = gtk.Label("Termo:")
        fixed.put(self.label_termo, 10, 25)
        
        #Label of identification name of user
        self.label_termo = gtk.Label("Usuário:")
        fixed.put(self.label_termo, 10, 65)        

        #Label of indentification password
        self.label_termo = gtk.Label("Senha:")
        fixed.put(self.label_termo, 10, 105) 

        #Text box to enter the search tokken
        self.boxtext_term = gtk.Entry()
        self.boxtext_term.set_max_length(50)
        self.boxtext_term.set_text()
        self.boxtext_term.set_size_request(250, 30)
        fixed.put(self.boxtext_term, 70, 20)

        #Text box to enter the username of twitter.
        self.boxtext_user = gtk.Entry()
        self.boxtext_user.set_max_length(50)
        self.boxtext_user.set_text()
        self.boxtext_user.set_size_request(200, 30)
        fixed.put(self.boxtext_user, 70, 60)

        #Text box to enter the password user
        self.boxtext_pass = gtk.Entry()
        self.boxtext_pass.set_max_length(50)
        self.boxtext_pass.set_text()
        self.boxtext_pass.set_visibility(False)
        self.boxtext_pass.set_size_request(200, 30)
        fixed.put(self.boxtext_pass, 70, 100)

        #Label explanatory
        self.label_inst = gtk.Label("Preencha os campos acima com o termo (Ex: UFLA),\nnome do usuário cadastrado no Twitter (Ex: fulano)\ne senha do usuário para iniciar o processo de coleta \nde documentos de textos.\n\n\nImportante: Nome de usuário e senha não serão guardado.")
        fixed.put(self.label_inst, 10, 145)

        #Button Collect Data
        self.bt_collectData = gtk.Button("Inicar Coleta")
        self.bt_collectData.connect("button-press-event", self.on_clickedCollect)
        self.bt_collectData.set_size_request(120, 30)
        fixed.put(self.bt_collectData, 360, 20)

        #Button Stop Collect Data
        self.bt_stopCollect = gtk.Button("Parar Coleta")
        self.bt_stopCollect.connect("button-press-event", self.on_clickedStopCollect)
        self.bt_stopCollect.set_size_request(120, 30)
        fixed.put(self.bt_stopCollect, 360, 60)

        #Button to exit of the windows 'Coletar Dados'.
        self.bt_exit = gtk.Button("Voltar")
        self.bt_exit.connect("clicked", self.on_clickedExit)
        self.bt_exit.set_size_request(120, 30)
        fixed.put(self.bt_exit, 360, 210)

        self.add(fixed)
        self.show_all()

    def collectData(self, *args):
        search = self.boxtext_term.get_text()
        user = self.boxtext_user.get_text()
        password = self.boxtext_pass.get_text()

        tmp = "curl -d track='"+search+"' https://stream.twitter.com/1/statuses/filter.json -u "+user+":"+password+" -o "
        now = strftime("%Y_%b_%d_%H.%M.%S", gmtime())
        cmd = tmp + now

        os.system(cmd)

    def on_clickedStopCollect(self, *args):
        for proc in psutil.process_iter():
            if proc.name == 'curl':
                proc.kill()

    def on_clickedCollect(self, widget, data=None):
        #Call the function collectData.
        self.thread_collect = threading.Thread(target=self.collectData, args=(widget, data)).start()
          
    def on_clickedExit(self, *args):
        self.destroy()
