#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygtk
pygtk.require("2.0")
import gtk
import glib
import json
import simplejson as json

#Classes implemented.
from modules.Alert import Alert
from modules.Processing import Processing
from modules.SaveTweet import SaveTweet
from modules.LangDetect import LangDetect 

class Train(gtk.Window):
    listMsgTweet = []
    tupleTweets = []
    n = 0
    def __init__(self):
        super(Train, self).__init__()
        vb = gtk.VBox()
        sw = gtk.ScrolledWindow()
        tv = gtk.TextView()
        hb = gtk.HButtonBox()
        bp = gtk.Button("Abrir Arquivo")
        bq = gtk.Button("Sair")
        self.add(vb)
        vb.pack_start(sw)
        sw.add(tv)
        vb.pack_end(hb, expand = False)
        hb.pack_start(bp)
        self.set_border_width(5)
        vb.set_spacing(5)
        hb.set_spacing(5)
        sw.set_shadow_type(gtk.SHADOW_IN)
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        tv.set_editable(False)
        self.set_title('Treinamento de Tweets')
        self.resize(500, 280)
        self.set_position(gtk.WIN_POS_CENTER)
        listaNames = [None, "Positivo", "Negativo", "Neutro"]
        for i in range(1, 4):
            b = gtk.Button(listaNames[i])
            hb.pack_start(b)
            b.connect('clicked', self.ao_clicar_num_botao, i)
        hb.pack_end(bq)
        self.connect('delete-event', self.sair)
        bp.connect('clicked', self.openFile)
        bq.connect('clicked', self.sair)
        self.loop = None
        self.buf = tv.get_buffer()
        self.show_all()

    def sair(self, *args):
        self.destroy()

    def openFile(self, *args):
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
            self.carregaArquivos(dialog.get_filename())

        elif response == gtk.RESPONSE_CANCEL:
            self.other_window = Alert()
            dialog.destroy()
        dialog.destroy()        

    def convertTweet(self, tweet):
        #Metodo para quebra de linha dentro da textview.
        appProcessing = Processing()
        tweet = appProcessing.wordAccented(tweet)
        
        phrase = ""
        sizeTextView = 0
        
        wordList = tweet.split()
        for word in wordList:
            size = len(word)
            sizeTextView += size
            if sizeTextView <= 55:
                phrase += word+" "
            else:
                phrase += '\n'+word
                sizeTextView = 0 + size

        tweet = phrase        
        return tweet

    def carregaArquivos(self, file_dir, *args):
        arquive = open(file_dir, 'r')
        listTweets = arquive.readlines()
        for tweet in listTweets:
            valor = tweet.find("text")
            if valor > 0:
                try:
                    #Decodifica o texto.
                    decoded = json.loads(tweet)

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
                        self.tupleTweets.append(tupla)
                        self.listMsgTweet.append(tweetOriginal)
                    
                except:
                    pass

        arquive.close() 
        
        ## Inicializa na tela com o primeiro tweet.
        tweet = self.tupleTweets[self.n]
        tweetOriginal = tweet['tweet_original']
        self.buf.set_text('')
        self.buf.set_text(self.buf.get_text(*self.buf.get_bounds())+tweetOriginal)

    def iniciar(self, *args):
        self.buf.set_text('')
        self.loop = glib.MainLoop()
        self.loop.run()
        self.loop = None

    def ao_clicar_num_botao(self, botao, i):
        tweet = self.tupleTweets[self.n]
        tweetOriginal = tweet['tweet_original']
        tweetTratado = self.execute(tweetOriginal)
        userName = tweet['nome_usuario']
        idTweet = tweet['id']
        tupla = {'tweet_original':tweetOriginal, 'tweet_tratado':tweetTratado, 'nome_usuario':userName, 'id':idTweet, 'rotulo':i}
        self.recordTuples(tupla, i)

        #Imprime próximo tweet na tela.
        self.n += 1
        self.buf.set_text('')
        tweet = self.tupleTweets[self.n]
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
