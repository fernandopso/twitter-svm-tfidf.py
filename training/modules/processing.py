#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Stemmer

class Processing(object):
    def lower_case(self, tweet):
        return tweet.lower()

    def accented_letters(self, tweet):
    	dict = {
            '\u00e0': 'a', '\u00e1': 'a', '\u00e2': 'a', '\u00e3': 'a',
            '\u00e4': 'a', '\u00c0': 'a', '\u00c1': 'a', '\u00c2': 'a',
            '\u00c3': 'a', '\u00c4': 'a', '\u00c5': 'a', '\u00e7': 'c',
            '\u00c7': 'c', '\u00e8': 'e', '\u00e9': 'e', '\u00ea': 'e',
            '\u00eb': 'e', '\u00c8': 'e', '\u00c9': 'e', '\u00ca': 'e',
            '\u00cb': 'e', '\u00ec': 'i', '\u00ed': 'i', '\u00ee': 'i',
            '\u00ef': 'i', '\u00cd': 'i', '\u00cc': 'i', '\u00ce': 'i',
            '\u00cf': 'i', '\u00f2': 'o', '\u00f3': 'o', '\u00f4': 'o',
            '\u00f5': 'o', '\u00f6': 'o', '\u00d2':' o', '\u00d3': 'o',
            '\u00d4': 'o', '\u00d5': 'o', '\u00d6':' o', '\u00f1': 'n',
            '\u00d1': 'n', '\u00f9': 'u', '\u00fa': 'u', '\u00fb': 'u',
            '\u00fc': 'u', '\u00d9': 'u', '\u00da': 'u', '\u00db': 'u', 
            '\u00dc': 'u'
        }

    	keys = dict.keys()

    	for key in keys:
    		value = dict[key]
    		tweet = tweet.replace(key, value)

    	return tweet

    def loose_letters(self, tweet):
        dict = {
          'okk': 'ok', 'aa': 'a', 'ee': 'e', 'ii': 'i', 'oo': 'o', 'uu': 'u',
          'ddd': 'dd', 'ff': 'f', 'hh': 'h', 'zz': 'z', 'rsrs': 'rs',
          'rsr': 'rs', 'll': 'l', 'mm': 'm', 'nn': 'n', 'rrr': 'rr',
          'sss': 'ss', 'ttt': 't'
        }

        keys = dict.keys()
        wordList = tweet.split()

        for key in keys:
            while tweet.find(key) != -1:
                for word in wordList:
                    if word.find(key) != -1:
                        value = dict[key]
                        tweet = tweet.replace(key, value)

        return tweet

    def special_characters(self, tweet):
        dict = {
            '\u00ba': '', '\u00bb': '', '\u00ac': '', '\u2013': '',
            '\u2026': '', '\u2019': '', '\u200e': '', '\u200b': '',
            '\u00b4': '', '\u25bd': '', '\u201c': '', '\u201d': '',
            '\u266a': '', '\u2665': '', '\u267a': ''
        }

        keys = dict.keys()

        for key in keys:
            value = dict[key]
            tweet = tweet.replace(key, value)

        return tweet

    def similar_words(self, tweet):
        dict = {
            'axu': 'acho', 'achu': 'acho', 'agr': 'agora', 'aki': 'aqui',
            'aqi': 'aqui', 'aq': 'aqui', 'akela': 'aquela', 'axo': 'acho',
            'blz': 'beleza', 'ctz': 'certeza', 'cmg': 'comigo', 'gnt': 'gente',
            'dakele': 'daquele', 'daki': 'daqui', 'fikar': 'ficar', 'eh': 'e',
            'fika': 'ficar', 'dps': 'depois', 'hj': 'hoje', 'hje': 'hoje',
            'jah': 'ja', 'kd': 'cade', 'ki': 'que', 'mt': 'muito', 'soh': 'so',
            'mto': 'muito', 'msm': 'mesmo', 'memo': 'mesmo', 'mermo': 'mesmo',
            'neh':'ne', 'nois': 'nos', 'okay': 'ok', 'p': 'para', 'tah': 'ta',
            'pq': 'porque', 'prq': 'porque', 'pque': 'porque', 'vamo': 'vamos',
            'pqe': 'porque', 'poko': 'pouco', 'qe': 'que', 'qm': 'quem',
            'qnto': 'quanto', 'tamo': 'estamos', 'tb': 'tambem',
            'tbm': 'tambem', 'vc': 'voce', 'vcs': 'voce', 'v6': 'voce', 
        }

        keys = dict.keys()

        word_list = tweet.split()

        for word in word_list:
            for key in keys:
                if (len(key.strip()) == len(word.strip())) and (word == key):
                    value = dict[key]
                    tweet = self.near(tweet, key, value)

        return tweet

    def remove_stopwords(self, tweet):
        stopwords = [
            "rt", "a", "as", "ao", "aos", "ate", "abaixo", "aca", "acaso",
            "acola", "acula", "ademais", "adentro", "afora", "agorinha",
            "ah", "ainda", "alem", "algo", "alias", "aonde", "apesar",
            "ate", "atraves", "b", "c", "ca", "comigo", "conosco", "consigo",
            "contigo", "contudo", "convosco", "cuja", "cujas", "cujo",
            "cujos", "com", "como", "d", "de", "do", "dos", "da", "dai",
            "dali", "das", "dele", "deles", "dela", "delas", "depois",
            "daquela", "daquelas", "daquele", "daqueles", "daqui", "daquilo",
            "dessa", "dessas", "desse", "desses", "desta", "destas", "deste",
            "destes", "detras", "devera", "deveras", "diante", "disso",
            "disto", "donde", "duma", "dumas", "duns", "durante", "e", "eh",
            "eia", "eis", "em", "ele", "eles", "ela", "elas", "esta", "estas",
            "estou", "este", "estes", "eu", "entre", "era", "eram", "esse",
            "esses", "essa", "essas", "estao", "aquele", "aqueles", "aquela",
            "aquelas", "aquilo", "estamos", "estive", "esteve", "estivemos",
            "estiveram", "estava", "estavam", "estivera", "estiveramos",
            "esteja", "estejamos", "estejam", "estivesse", "estivessemos",
            "estivessem", "estiver", "estivermos", "estiverem", "enfim",
            "enquanto", "entanto", "entao", "entretanto", "exceto", "f",
            "foi", "foram", "fosse", "fossemos", "fossem", "for", "formos",
            "forem", "fui", "fomos", "foram", "fora", "foramos", "g", "h",
            "hem", "hum", "ha", "havia", "hei", "havemos", "hao", "houve",
            "houvemos", "houveram", "houvera", "houveramos", "haja",
            "hajamos", "hajam", "houvesse", "houvessemos", "houvessem",
            "houver", "houvermos", "houverem", "houverei", "houvera",
            "houveremos", "houverao", "houveram", "houveria", "houveriamos",
            "houveriam", "i", "idem", "inclusive", "isso", "isto", "j", "ja",
            "k", "ker", "l", "la", "las", "lhe", "lhes", "lha", "lhas", "lho",
            "lhos", "logo", "m", "mas", "mais", "mesma", "mesmas", "mesmo",
            "mesmos", "me", "meu", "meus", "minha", "minhas", "mim", "mui",
            "no", "nos", "na", "nas", "nas", "numa", "numas", "nem", "nosso",
            "nossa", "nossos", "nossas", "nalgum", "nalguma", "nalgumas",
            "nalguns", "naquela", "naquelas", "naquele", "naqueles",
            "naquilo", "nela", "nelas", "nele", "neles", "nessa", "nessas",
            "nesse", "nesses", "nesta", "nestas", "neste", "nestes",
            "ninguem", "nisso", "nisto", "noutra", "noutras", "noutro",
            "noutros", "nuns", "o", "os", "ou", "ola", "onde", "opa", "ora",
            "outra", "outras", "outrem", "outro", "outrora", "outros",
            "outrossim", "p",  "para", "por", "pelo", "pelos", "pela",
            "pelas", "per", "perante", "pero", "pois", "porem", "porque",
            "portanto", "porventura", "possivelmente", "posteriormente",
            "pra", "praquela", "praquelas", "praquele", "praqueles",
            "praquilo", "pras", "prela", "prelas", "prele", "preles",
            "preste", "prestes", "q", "que", "quando", "quem", "qual",
            "quais", "qualquer", "quaisquer", "r", "s", "se", "seu",
            "seus", "sua", "suas", "ser", "só", "so", "sem", "seja",
            "sejamos", "sejam", "serei", "sera", "seremos", "serao",
            "seria", "seriamos", "seriam", "sou", "somos", "sao", "saum",
            "sequer", "t", "ta", "tem", "tens", "tambem", "tenha", "tenhamos",
            "tenham", "tivesse", "tivessemos", "tivessem", "tiver", "tivermos",
            "tiverem", "terei", "tera", "teremos", "terao", "teria",
            "teriamos", "teriam", "tinha", "tenho", "tinhas", "tinham",
            "tive", "teve", "tivemos", "tiveram", "tivera", "teu", "tua",
            "teus", "tuas", "tenho", "temos", "tu", "te", "tal", "tais",
            "todavia", "u", "um", "uma", "umas", "uns", "voce", "voces", "vc",
            "vcs", "oce", "oces", "ces","vos", "vossa", "vossas", "vossos",
            "vulgo", "visto", "x", "z", "w", "y", "0", "1", "2", "3", "4", "5",
            "6", "7", "8", "9", "ascom", "noticia", "addthis", "via"
        ]

        for word in tweet.split():
            for stopword in stopwords:
                if (len(word.strip()) == len(stopword.strip())):
                    if (word == stopword):
                        tweet = self.remove_word(tweet, stopword)

        return tweet

    def remove_mentions(self, tweet):
        if tweet.find('@') != -1:
            tweet = self.remove(tweet, '@')

        return tweet

    def remove_links(self, tweet):
        if tweet.find('http') != -1:
            tweet = self.remove(tweet, 'http')

        return tweet

    def remove_alpha_numeric(self, tweet):
    	for word in tweet.split():
    		word = word.strip()
    		if word.isalpha() is False:
    			tweet = tweet.replace(word, ' ')
    	while tweet.isalnum():
    		remove_alpha_numeric(tweet)

    	dict = {
            '0': ' ', '1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ',
            '6': ' ', '7': ' ', '8': ' ', '9': ' '
        }

    	keys = dict.keys()

    	for key in keys:
    		if tweet.find(key) != -1:
    			value = dict[key]
    			tweet = tweet.replace(key, value)

    	return tweet

    def remove_solitary_letters(self, tweet):
    	dict = {
            'b': ' ', 'c': ' ', 'f': ' ', 'g': ' ', 'h': ' ', 'j': ' ',
            'k': ' ', 'l': ' ', 'm': ' ', 'r': ' ', 's': ' ', 't': ' ',
            'v': ' ', 'x': ' ', 'z': ' ', 'w': ' ', 'y': ' '
        }

    	keys = dict.keys()

    	for key in keys:
    		value = dict[key]
    		tweet = self.near(tweet, key, value)

    	return tweet

    def remove_spaces(self, tweet):
        if tweet.find('\n') != -1:
            tweet = self.remove(tweet, '\n')

        return tweet

    def stemmizator(self, tweet):
        stemmer = Stemmer.Stemmer('english')

        tweet_stemmer = ''
        for word in tweet.split():
            tweet_stemmer += stemmer.stemWord(word) + ' '

        return tweet_stemmer

    def remove_word(self, tweet, stopword):
        if tweet != None:
            t = ''

            for word in tweet.split():
                if word == stopword:
                    pass
                else:
                    t += word + ' '

            return t

        else:
            pass

    def remove(self, tweet, key):
        t = ''
        for word in tweet.split():
            if word.find(key) != -1:
                pass
            else:
                t += word + ' '

        return t

    def near(self, tweet, key, value):
        t = ''

        for word in tweet.split():
            if word == key:
                t += value + ' '
            else:
                t += word + ' '

        return t

    def word_accented(self, tweet):
        dict = {
            '\u00e0': 'à', '\u00e1': 'á', '\u00e2': 'â', '\u00e3': 'ã',
            '\u00e4': 'ä', '\u00c0': 'À', '\u00c1': 'Á', '\u00c2': 'Â',
            '\u00c3': 'Ã', '\u00c4': 'Ä', '\u00c5': 'A', '\u00e7': 'ç',
            '\u00c7': 'Ç', '\u00e8': 'è', '\u00e9': 'é', '\u00ea': 'ê',
            '\u00eb': 'ë', '\u00c8': 'È', '\u00c9': 'É', '\u00ca': 'Ê',
            '\u00cb': 'Ë', '\u00ec': 'ì', '\u00ed': 'í', '\u00ee': 'î',
            '\u00ef': 'ï', '\u00cd': 'Í', '\u00cc': 'Ì', '\u00ce': 'Î',
            '\u00cf': 'Ï', '\u00f2': 'ò', '\u00f3': 'ó', '\u00f4': 'ô',
            '\u00f5': 'õ', '\u00f6': 'ö', '\u00d2': 'Ò', '\u00d3': 'Ó',
            '\u00d4': 'Ô', '\u00d5': 'Õ', '\u00d6': 'Ö', '\u00f1': 'ñ',
            '\u00d1': 'ñ', '\u00f9': 'ù', '\u00fa': 'ú', '\u00fb': 'û',
            '\u00fc': 'ü', '\u00d9': 'Ù', '\u00da': 'Ú', '\u00db': 'Û',
            '\u00dc':'Ü'
        }

        for key in dict.keys():
            value = dict[key]
            tweet = tweet.replace(key, value)

        return tweet
