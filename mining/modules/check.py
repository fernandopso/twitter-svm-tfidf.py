#!/usr/bin/env python
#-*- coding: utf-8 -*-
from subModules.Validate import Validate
from subModules.SaveTweet import SaveTweet

class Check:
	tupleTweets = []
	i = 0

	def __init__(self, tupleTweets):
		self.tupleTweets = tupleTweets
		super(Check, self).__init__()
		vb = gtk.VBox()
		sw = gtk.ScrolledWindow()
		tv = gtk.TextView()
		hb = gtk.HButtonBox()
		bt_correto = gtk.Button("Correto")
		bt_errado = gtk.Button("Errado")
		bq = gtk.Button("Sair")
		self.add(vb)
		vb.pack_start(sw)
		sw.add(tv)
		vb.pack_end(hb, expand = False)
		hb.pack_start(bt_correto)
		hb.pack_start(bt_errado)
		self.set_border_width(5)
		vb.set_spacing(5)
		hb.set_spacing(5)
		sw.set_shadow_type(gtk.SHADOW_IN)
		sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
		tv.set_editable(False)
		self.set_title('Verificação de Tweets')
		self.resize(500, 280)
		self.set_position(gtk.WIN_POS_CENTER)
		hb.pack_end(bq)
		self.connect('delete-event', self.sair)
		bt_errado.connect('clicked', self.validateTweet)
		bt_correto.connect('clicked', self.ao_clicar_num_botao, 0)
		bq.connect('clicked', self.sair)

		self.loop = None
		self.buf = tv.get_buffer()
		self.show_all()

	def wordAccented(self, tweet):
		dict = {'\u00e0':'à', '\u00e1':'á', '\u00e2':'â', '\u00e3':'ã', '\u00e4':'ä', '\u00c0':'À', '\u00c1':'Á', '\u00c2':'Â', '\u00c3':'Ã', '\u00c4':'Ä', '\u00c5':'A', '\u00e7':'ç', '\u00c7':'Ç', '\u00e8':'è', '\u00e9':'é', '\u00ea':'ê', '\u00eb':'ë', '\u00c8':'È', '\u00c9':'É', '\u00ca':'Ê', '\u00cb':'Ë', '\u00ec':'ì', '\u00ed':'í', '\u00ee':'î', '\u00ef':'ï', '\u00cd':'Í', '\u00cc':'Ì', '\u00ce':'Î', '\u00cf':'Ï', '\u00f2':'ò', '\u00f3':'ó', '\u00f4':'ô', '\u00f5':'õ', '\u00f6':'ö', '\u00d2':'Ò', '\u00d3':'Ó', '\u00d4':'Ô', '\u00d5':'Õ', '\u00d6':'Ö', '\u00f1':'ñ', '\u00d1':'ñ', '\u00f9':'ù', '\u00fa':'ú', '\u00fb':'û', '\u00fc':'ü', '\u00d9':'Ù', '\u00da':'Ú', '\u00db':'Û', '\u00dc':'Ü', '\u00bb':'-', '\u00ac':'¬', '\u00aa':'ª', '\u00ba':'º', '\u00a1':'' }

		keys = dict.keys()

		for key in keys:
			value = dict[key]
			tweet = tweet.replace(key, value)

		return tweet

	def convertTweet(self, tweet):
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

	def start(self, *args):
		tweet = self.tupleTweets[0]
		tweetOriginal = tweet['tweet_original']
		tweetOriginal = self.wordAccented(tweetOriginal)
		prediction = open('prediction', 'r').readlines()
		rotulo = prediction[0].replace('\r', '')
		rotulo = prediction[0].replace('\n', '')
		rotulo = int(float(rotulo))

		classification = ""
		if rotulo == 1:
			classification = "Tweet "+"Positivo: "+tweetOriginal
		if rotulo == 2:
			classification = "Tweet "+"Negativo: "+tweetOriginal
		if rotulo == 3:
			classification = "Tweet "+"Neutro: "+tweetOriginal

		classification = self.convertTweet(classification)

		self.buf.set_text('')
		self.buf.set_text(self.buf.get_text(*self.buf.get_bounds())+classification)

	def sair(self, *args):
		self.destroy()

	def ao_clicar_num_botao(self, botao, numero):
		self.buf.set_text('')
		self.i += 1
		self.buf.set_text(self.buf.get_text(*self.buf.get_bounds())+self.list_tweets[self.i])
		print 'Número:', numero
		if self.loop:
			self.escolha = numero
			self.loop.quit()

	def iniciar(self, *args):
		self.buf.set_text('')
		self.loop = glib.MainLoop()
		self.loop.run()
		self.loop = None
		self.buf.set_text(self.buf.get_text(*self.buf.get_bounds())+'%i\n' % self.escolha)
		self.buf.set_text(self.buf.get_text(*self.buf.get_bounds()) + 'Obrigado!')

	def validateTweet(self, *args):
		appValidate = Validate()