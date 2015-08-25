#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Stemmer

class Processing:
    #Metodos para aumentar a legibilidade.
    def lowerCased(self, tweet):
        #Transforma as letras do tweet que estão em maiusculas em minusculas.
        tweetMinuscula = tweet.lower()

        return tweetMinuscula

    def accentedLetters(self, tweet):
    	dict = {'\u00e0':'a', '\u00e1':'a', '\u00e2':'a', '\u00e3':'a', '\u00e4':'a', '\u00c0':'a', '\u00c1':'a', '\u00c2':'a', '\u00c3':'a', '\u00c4':'a', '\u00c5':'a', '\u00e7':'c', '\u00c7':'c', '\u00e8':'e', '\u00e9':'e', '\u00ea':'e', '\u00eb':'e', '\u00c8':'e', '\u00c9':'e', '\u00ca':'e', '\u00cb':'e', '\u00ec':'i', '\u00ed':'i', '\u00ee':'i', '\u00ef':'i', '\u00cd':'i', '\u00cc':'i', '\u00ce':'i', '\u00cf':'i', '\u00f2':'o', '\u00f3':'o', '\u00f4':'o', '\u00f5':'o', '\u00f6':'o', '\u00d2':'o', '\u00d3':'o', '\u00d4':'o', '\u00d5':'o', '\u00d6':'o', '\u00f1':'n', '\u00d1':'n', '\u00f9':'u', '\u00fa':'u', '\u00fb':'u', '\u00fc':'u', '\u00d9':'u', '\u00da':'u', '\u00db':'u', '\u00dc':'u'}

    	keys = dict.keys()

    	for key in keys:
    		value = dict[key]
    		tweet = tweet.replace(key, value)

    	return tweet

    def looseLetters(self, tweet):
        dict = {'kk':' ', 'okk':'ok', 'aa':'a', 'ee':'e', 'ii':'i', 'oo':'o', 'uu':'u', 'ddd':'dd', 'ff':'f', 'hh':'h', 'zz':'z', 'kaka':' ', 'hua':' ', 'uah':' ', 'uha':' ', 'hau':' ', 'rsrs':' ', 'rsr':' ', 'shua':' ', 'hehe':' ', 'haha':' ', 'll':'l', 'mm':'m', 'nn':'n', 'rrr':'rr', 'sss':'ss', 'ttt':'tt', 'ww':'w', 'pqp':' ', 'tc':' ', 'oh':' ', 'ih':' ', 'ah':' ', 'eh':' ', 'uh':' '}

        keys = dict.keys()
        wordList = tweet.split()

        for key in keys:
            while tweet.find(key) != -1:
                for word in wordList:
                    if word.find(key) != -1:
                        value = dict[key]
                        tweet = tweet.replace(key, value)

        return tweet

    def specialCharacters(self, tweet):
        dict = {'\u00ba':' ', '\u00bb':' ', '\u00ac':' ', '\u2013':' ', '\u00a':' ', '\u2026':' ', '\u2019':' ', '\u200e':' ', '\u200b':' ', '\u00b4':' ', '\u25bd':' ', '\u201c':' ', '\u201d':' ', '\u266a':' ', '\u2665':' ', '\u267a':' ', '!':' ', '?':' ', ',':' ', '.':' ', ':':' ', '"':' ', '!':' ', '#':' ', 'r$':' ', '$':' ', '%':' ', '"':' ', '&':' ', '*':' ', '(':' ', ')':' ', '[':' ', ']':' ', '{':' ', '}':' ', 'º':' ', ';':' ', '|':' ', "\\":' ', "/":' ', '°':' ', '^':' ', '~':' ', '`':' ', 'd+':'de mais', '+':' ', '=':' ', '-':' ', '_':' ', '\' ':' '}

        keys = dict.keys()

        for key in keys:
            value = dict[key]
            tweet = tweet.replace(key, value)

        return tweet

    def similarWords(self, tweet):
        dict = {'axu':'acho', 'achu':'acho', 'agr':'agora', 'aki':'aqui', 'aqi':'aqui', 'aq':'aqui', 'akela':'aquela', 'axo':'acho', 'blz':'beleza', 'ctz':'certeza', 'cmg':'comigo', 'cvs':'conversa', 'd':'de', 'dakele':'daquele', 'daki':'daqui', 'fikar':'ficar', 'fika':'ficar', 'dps':'depois', 'gnt':'gente', 'hj':'hoje', 'hje':'hoje', 'jah':'ja', 'kd':'cade', 'ki':'que', 'mt':'muito', 'mto':'muito', 'msm':'mesmo', 'memo':'mesmo', 'mermo':'mesmo', 'neh':'ne', 'nois':'nos', 'nus':'nos', 'okay':'ok', 'p':'para', 'pq':'porque', 'prq':'porque', 'pque':'porque', 'pqe':'porque', 'poko':'pouco', 'qe':'que', 'qm':'quem', 'qnto':'quanto', 'queue':'que', 'queuero':'quero', 'soh':'so', 'tah':'ta', 'tamo':'estamos', 'tb':'tambem', 'tbm':'tambem', 'vamo':'vamos', 'vc':'voce', 'vcs':'voce', 'v6':'voce', 'eh':' ', 'ow':' ', 'k':' ', 'rt':' ', 'rs':' '}

        keys = dict.keys()

        wordList = tweet.split()
        tweetRemoved = ''

        for word in wordList:
            for key in keys:
                if (len(key.strip()) == len(word.strip())) and (word == key):
                    value = dict[key]
                    tweet = self.changeSimilar(tweet, key, value)

        return tweet

    def removeStopWords(self, tweet):
        # Lista de stopWords da lingua portuguesa. Lista obtida e adaptada de http://snowball.tartarus.org/algorithms/portuguese/stop.txt
        listStopWords = ["rt", "a", "as", "ao", "aos", "ate", "abaixo", "aca", "acaso", "acola", "acula", "ademais", "adentro", "afora", "agorinha", "ah",  "ainda", "alem", "algo", "alias", "aonde", "apesar", "ate", "atraves", "b", "c", "ca", "comigo", "conosco", "consigo", "contigo", "contudo", "convosco", "cuja", "cujas", "cujo", "cujos", "com", "como", "d", "de", "do", "dos", "da", "dai", "dali", "das", "dele", "deles", "dela", "delas", "depois", "daquela", "daquelas", "daquele", "daqueles", "daqui", "daquilo", "dessa", "dessas", "desse", "desses", "desta", "destas", "deste", "destes", "detras", "devera", "deveras", "diante", "disso", "disto", "donde", "duma", "dumas", "duns", "durante", "e", "eh", "eia", "eis", "em", "ele", "eles", "ela", "elas", "esta", "estas", "estou", "este", "estes", "eu", "entre", "era", "eram", "esse", "esses", "essa", "essas", "estao", "aquele", "aqueles", "aquela", "aquelas", "aquilo", "estamos", "estive", "esteve", "estivemos", "estiveram", "estava", "estavam", "estivera", "estiveramos", "esteja", "estejamos", "estejam", "estivesse", "estivessemos", "estivessem", "estiver", "estivermos", "estiverem", "enfim", "enquanto", "entanto", "entao", "entretanto", "exceto", "f", "foi", "foram", "fosse", "fossemos", "fossem", "for", "formos", "forem", "fui", "fomos", "foram", "fora", "foramos", "g", "h", "hem", "hum", "ha", "havia", "hei", "havemos", "hao", "houve", "houvemos", "houveram", "houvera", "houveramos", "haja", "hajamos", "hajam", "houvesse", "houvessemos", "houvessem", "houver", "houvermos", "houverem", "houverei", "houvera", "houveremos", "houverao", "houveram", "houveria", "houveriamos", "houveriam", "i", "idem", "inclusive", "isso", "isto", "j", "ja", "k", "ker", "l", "la", "las", "lhe", "lhes", "lha", "lhas", "lho", "lhos", "logo", "m", "mas", "mais", "mesma", "mesmas", "mesmo", "mesmos", "me", "meu", "meus", "minha", "minhas", "mim", "mui", "no", "nos", "na", "nas", "nas", "numa", "numas", "nem", "nosso", "nossa", "nossos", "nossas", "nalgum", "nalguma", "nalgumas", "nalguns", "naquela", "naquelas", "naquele", "naqueles", "naquilo", "nela", "nelas", "nele", "neles", "nessa", "nessas", "nesse", "nesses", "nesta", "nestas", "neste", "nestes", "ninguem", "nisso", "nisto", "noutra", "noutras", "noutro", "noutros", "nuns", "o", "os", "ou", "ola", "onde", "opa", "ora", "outra", "outras", "outrem", "outro", "outrora", "outros", "outrossim", "p",  "para", "por", "pelo", "pelos", "pela", "pelas", "per", "perante", "pero", "pois", "porem", "porque",  "portanto", "porventura", "possivelmente", "posteriormente", "pra", "praquela", "praquelas", "praquele", "praqueles", "praquilo", "pras", "prela", "prelas", "prele", "preles", "preste", "prestes", "q", "que", "quando", "quem", "qual", "quais", "qualquer", "quaisquer", "r", "s", "se", "seu", "seus", "sua", "suas", "ser", "só", "so", "sem", "seja", "sejamos", "sejam", "serei", "sera", "seremos", "serao", "seria", "seriamos", "seriam", "sou", "somos", "sao", "saum", "sequer", "t", "ta", "tem", "tens", "tambem", "tenha", "tenhamos", "tenham", "tivesse", "tivessemos", "tivessem", "tiver", "tivermos", "tiverem", "terei", "tera", "teremos", "terao", "teria", "teriamos", "teriam", "tinha", "tenho", "tinhas", "tinham", "tive", "teve", "tivemos", "tiveram", "tivera", "teu", "tua", "teus", "tuas", "tenho", "temos", "tu", "te", "tal", "tais", "todavia", "u", "um", "uma", "umas", "uns", "v", "voce", "voces", "vc", "vcs", "oce", "oces", "ces","vos", "vossa", "vossas", "vossos", "vulgo", "visto", "x", "z", "w", "y", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "ascom", "noticia", "addthis", "via"]

        wordList = tweet.split()
        tweetRemoved = ''

        for word in wordList:
            for stopWord in listStopWords:
                if (len(word.strip()) == len(stopWord.strip())) and (word == stopWord):
                    tweet = self.removeWord(tweet, stopWord)

        return tweet

    #Metodos para redução textual.
    def removeMention(self, tweet):
        if tweet.find('@') != -1:
            tweet = self.remove(tweet, '@')

        return tweet

    def removeLinks(self, tweet):
        if tweet.find('http') != -1:
            tweet = self.remove(tweet, 'http')

        return tweet

    def alphaNumeric(self, tweet):
    	#Função para remover palavras que apresentão números.
    	listaPalavras = tweet.split()

    	for palavra in listaPalavras:
    		palavra = palavra.strip()
    		if palavra.isalpha() is False:
    			tweet = tweet.replace(palavra, ' ')
    	while tweet.isalnum():
    		alphaNumeric(tweet)

    	dict = {'0':' ', '1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ', '7':' ', '8':' ', '9':' '}

    	keys = dict.keys()

    	for key in keys:
    		if tweet.find(key) != -1:
    			value = dict[key]
    			tweet = tweet.replace(key, value)

    	return tweet

    def solitaryLatters(self, tweet):
    	dict = {'b':' ', 'c':' ', 'f':' ', 'g':' ', 'h':' ', 'j':' ', 'k':' ', 'l':' ', 'm':' ', 'r':' ', 's':' ', 't':' ', 'v':' ', 'x':' ', 'z':' ', 'w':' ', 'y':' '}

    	keys = dict.keys()

    	for key in keys:
    		value = dict[key]
    		tweet = self.changeSimilar(tweet, key, value)

    	return tweet

    def removeSpace(self, tweet):
        if tweet.find('\n') != -1:
            tweet = self.remove(tweet, '\n')

        return tweet

    def stemmizar(self, tweet):
        # Carrega as funcoes para stemmizar.
        stemmer = Stemmer.Stemmer('english')

        wordList = tweet.split()
        tweetStemmer = ''
        for word in wordList:
            tweetStemmer += stemmer.stemWord(word) + ' '

        return tweetStemmer

    #Metodos auxiliares aos metodos de redução textual.
    def removeWord(self, tweet, stopWord):
        if tweet != None:
            tweetRemoved = ''
            wordList = tweet.split()
            for word in wordList:
                if word == stopWord:
                    pass
                else:
                    tweetRemoved += word + ' '

            return tweetRemoved

        else:
            pass

    def remove(self, tweet, key):
        wordList = tweet.split()
        tweetRemoved = ''
        for word in wordList:
            if word.find(key) != -1:
                pass
            else:
                tweetRemoved += word + ' '

        return tweetRemoved

    def changeSimilar(self, tweet, key, value):
        wordList = tweet.split()
        tweetRemoved = ''

        for word in wordList:
            if word == key:
                tweetRemoved += value + ' '
            else:
                tweetRemoved += word + ' '

        return tweetRemoved

    #Metodo para acentuar as palavras corretamente.
    def wordAccented(self, tweet):
        dict = {'\u00e0':'à', '\u00e1':'á', '\u00e2':'â', '\u00e3':'ã', '\u00e4':'ä', '\u00c0':'À', '\u00c1':'Á', '\u00c2':'Â', '\u00c3':'Ã', '\u00c4':'Ä', '\u00c5':'A', '\u00e7':'ç', '\u00c7':'Ç', '\u00e8':'è', '\u00e9':'é', '\u00ea':'ê', '\u00eb':'ë', '\u00c8':'È', '\u00c9':'É', '\u00ca':'Ê', '\u00cb':'Ë', '\u00ec':'ì', '\u00ed':'í', '\u00ee':'î', '\u00ef':'ï', '\u00cd':'Í', '\u00cc':'Ì', '\u00ce':'Î', '\u00cf':'Ï', '\u00f2':'ò', '\u00f3':'ó', '\u00f4':'ô', '\u00f5':'õ', '\u00f6':'ö', '\u00d2':'Ò', '\u00d3':'Ó', '\u00d4':'Ô', '\u00d5':'Õ', '\u00d6':'Ö', '\u00f1':'ñ', '\u00d1':'ñ', '\u00f9':'ù', '\u00fa':'ú', '\u00fb':'û', '\u00fc':'ü', '\u00d9':'Ù', '\u00da':'Ú', '\u00db':'Û', '\u00dc':'Ü'}

        keys = dict.keys()

        for key in keys:
            value = dict[key]
            tweet = tweet.replace(key, value)

        return tweet
