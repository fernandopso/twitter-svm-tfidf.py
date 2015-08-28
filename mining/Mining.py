#!/usr/bin/env python
# -*- coding: utf-8 -*-
from modules.Alert import Alert
from modules.tfidf import tfidf
from modules.fileDir import fileDir
from modules.formatFile import FormatFile
from modules.svm import Model
from modules.check import Check

class Mining:
    """docstring for Mining"""
    list_tweets = []
    def __init__(self):
        super(Mining, self).__init__()
        self.set_title("Mineração de Dados")
        self.set_size_request(500, 280)
        self.set_position(gtk.WIN_POS_CENTER)
        
        fixed = gtk.Fixed()

        #Label explanatory.
        self.label = gtk.Label("Uso:\n- Selecione um arquivo de treinamento: \n(Ex: file_trained.pck) \n\n- Selecione um arquivo de teste: \n(Ex: 2012_Dec_01_14_35_56)")
        fixed.put(self.label, 20, 20)

        #Button to open file train.
        self.bt_open = gtk.Button("Dados Treinados")
        self.bt_open.connect("clicked", self.on_openFile, 1)
        self.bt_open.set_size_request(130, 30)
        fixed.put(self.bt_open, 360, 20)

        #Button to open file test.
        self.bt_openPositivo = gtk.Button("Dados de Teste")
        self.bt_openPositivo.connect("clicked", self.on_openFile, 2)
        self.bt_openPositivo.set_size_request(130, 30)
        fixed.put(self.bt_openPositivo, 360, 60)

        #Button start.
        self.bt_start = gtk.Button("Iniciar")
        self.bt_start.connect("clicked", self.on_clickedStart)
        self.bt_start.set_size_request(130, 30)
        fixed.put(self.bt_start, 360, 100)

        #Button to ckeck datas.
        self.bt_check = gtk.Button("Verificar")
        self.bt_check.connect("clicked", self.on_clickedCheck)
        self.bt_check.set_size_request(130, 30)
        fixed.put(self.bt_check, 360, 140)

        #Button to close this window.
        self.bt_exit = gtk.Button("Voltar")
        self.bt_exit.connect("clicked", self.on_clickedExit)
        self.bt_exit.set_size_request(130, 30)
        fixed.put(self.bt_exit, 360, 220)

        self.add(fixed)
        self.show_all()       

    def on_clickedStart(self, *args):
        if self.file_train == None:
            print "Você não selecionou nenhum arquivo de treinamento."

        if self.file_test == None:
            print "Você não selecionou nenhum arquivo de teste."
    
        elif self.file_train != None and self.file_test != None:
            appOpen = fileDir()
            appTFIDF = tfidf()
            appFormat = FormatFile()
            tupleTweetTrain = []
            tupleTweetTest = []
            listWords = []
            idfs = []

            vector_train = list()
            train_prediction = list()
            vector_test = list()
            
            tupleTweetTrain = appOpen.startTrain(self.file_train)
            print "Tweets Para Treinamento: Ok"
            tupleTweetTest = appOpen.startTest(self.file_test)
            print "Tweets Para Teste: Ok"     
            print "Preparando Dados..."
            idfs, listWords = appTFIDF.start(tupleTweetTrain)
            vector_train, train_prediction, vector_test = appFormat.formatFile(tupleTweetTrain, tupleTweetTest, listWords, idfs)

            #=====================================#
            print "Iniciando classicação..."
            appSVM = Model()
            appSVM.svm(vector_train, train_prediction, vector_test)
            print "Predição de arquivos finalizada!"

            for i in tupleTweetTest:
                self.list_tweets.append(i)

    def on_clickedCheck(self, *args):
        appCheck = Check(self.list_tweets)
        appCheck.start()

    def on_clickedExit(self, *args):
        #Exit this page.
        self.destroy()

    def on_openFile(self, op, *args):
        if gtk.pygtk_version < (2,3,90):
            raise SystemExit

        dialog = gtk.FileChooserDialog("Selecione o Arquivo..",
                                     None,
                                     gtk.FILE_CHOOSER_ACTION_OPEN,
                                     (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                      gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)

        filter = gtk.FileFilter()
        filter.set_name("All files")
        filter.add_pattern("*")
        dialog.add_filter(filter)
        filter = gtk.FileFilter()
        filter.set_name("Images")
        filter.add_mime_type("image/png")
        filter.add_mime_type("image/jpeg")
        filter.add_mime_type("image/gif")
        filter.add_pattern("*.png")
        filter.add_pattern("*.jpg")
        filter.add_pattern("*.gif")
        filter.add_pattern("*.tif")
        filter.add_pattern("*.xpm")
        dialog.add_filter(filter)

        response = dialog.run()
        if response == gtk.RESPONSE_OK:        
            if op == 1:
                self.file_train = dialog.get_filename()
                #print self.file_train

            if op == 2:
                self.file_test = dialog.get_filename()
                #print self.file_test           

        elif response == gtk.RESPONSE_CANCEL:
            self.other_window = Alert()
            dialog.destroy()
        dialog.destroy()