# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# Libraries for Interface Grafics
import gtk

# Classes implemented.
from collect.Collect import Collect
from mining.Mining import Mining
from train.Train import Train

class MainWindows(gtk.Window):
    def __init__(self):
        super(MainWindows, self).__init__()
        # Creat the main window.
        self.set_title("Data Mining - UFLA")
        self.set_size_request(500, 280)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", self.on_destroy)
        
        fixed = gtk.Fixed()

        #TextView com os procedimentos.
        label = gtk.Label()
        label.set_markup("""Bem-vindo,\nEsta ferramenta é dívida em três etapas para o \nprocesso de mineração de textos:\n\n\n1ª Etapa: Coleta de dados.\n\n2ª Etapa: Treinamento de uma parte dos dados\n                      coletados.\n\n3ª Etapa: Classificação dos dados coletados.""")
        label.set_line_wrap(True)
        fixed.put(label, 10, 20)

        #Button Data Collect.
        bt_collect = gtk.Button("Coletar Dados")
        bt_collect.connect("clicked", self.on_clickedCollect)
        bt_collect.set_size_request(130, 30)
        fixed.put(bt_collect, 360, 20)

        #Button Data Train.
        bt_train = gtk.Button("Treinar Dados")
        bt_train.connect("clicked", self.on_clickedTrain)
        bt_train.set_size_request(130, 30)
        fixed.put(bt_train, 360, 70)

        #Button Data Mining.
        bt_mining = gtk.Button("Classificar Dados")
        bt_mining.connect("clicked", self.on_clickedMining)
        bt_mining.set_size_request(130, 30)
        fixed.put(bt_mining, 360, 120)

		#Button Exit.
        bt_exit = gtk.Button("Sair")
        bt_exit.connect("clicked", self.on_clickedExit)
        bt_exit.set_size_request(130, 30)
        fixed.put(bt_exit, 360, 210)   

        self.add(fixed)
        self.show_all()

    def on_clickedCollect(self, *args):
        appCollect = Collect()
        
    def on_clickedTrain(self, *args):
        appTrain = Train()

    def on_clickedMining(self, *args):
        appMining = Mining()

    def on_destroy(windows, *args):
        gtk.main_quit()       

    def on_clickedExit(windows, *args):
        d = gtk.MessageDialog(parent = windows, flags = 0,
                              type = gtk.MESSAGE_QUESTION,
                              buttons = gtk.BUTTONS_YES_NO,
                              message_format = "Deseja realmente sair?")
        resposta = d.run()
        d.destroy()
        if resposta == gtk.RESPONSE_YES:
            gtk.main_quit()

if __name__ == '__main__':
    print "=================================================================================="
    print "=== Suport Vector Machine for tweet data mining - UFLA                        ===="
    print "=================================================================================="
    print """\nWelcome, this tool is divided into three steps to the tweets mining process """
    print """\nSelect an option:\n"""
    print """ (c) 1ª step: Collect tweets from Twitter """
    print """ (t) 2ª step: Training some tweets """
    print """ (p) 3ª step: Predication others tweets """

    #app = MainWindows()
    #gtk.main()
