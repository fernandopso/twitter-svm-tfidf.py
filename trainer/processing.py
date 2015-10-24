# !/usr/bin/env python
# -*- coding: utf-8 -*-

import Stemmer

class Processing(object):
    """
    All methods has more sense for Portuguese-BR language
    """

    def __init__(self, tweet):
        self.tweet = tweet

    def execute(self):
        """
        Execute all processes to reduce ambiguities
        """
        self.lower_case()
        self.accented_letters()
        self.double_letters()
        self.special_characters()
        self.similar_words()
        self.remove_stopwords()
        self.remove_mentions()
        self.remove_links()
        self.remove_solitary_letters()

        return self.tweet

    def lower_case(self):
        """
        All words in case letters
        """
        self.tweet = self.tweet.lower()

        return self.tweet

    def accented_letters(self):
        """
        Change all accented letters for unaccented
        """
    	for key in Processing.UNICODE_ACCENTED_LETTERS.keys():
            value = Processing.UNICODE_ACCENTED_LETTERS[key]
            self.tweet = self.tweet.replace(key, value)

    	return self.tweet

    def double_letters(self):
        """
        Many words are written with double letters

        important!
            The double letters rr, ss and oo not considered in this case,
            this role has more sense for tweet portugues-br
        """
        wordList = self.tweet.split()

        for key in Processing.DOUBLE_LETTERS.keys():
            while self.tweet.find(key) != -1:
                for word in wordList:
                    if word.find(key) != -1:
                        value = Processing.DOUBLE_LETTERS[key]
                        self.tweet = self.tweet.replace(key, value)

        return self.tweet

    def special_characters(self):
        """
        Special characters are letters that make no sense to human readable
        """
        for key in Processing.SPECIAL_CHARACTERS.keys():
            value = Processing.SPECIAL_CHARACTERS[key]
            self.tweet = self.tweet.replace(key, value)

        return self.tweet

    def similar_words(self):
        """
        Many words are written the way they are pronounced or using analogies
        with other small words
        """
        word_list = self.tweet.split()

        for word in word_list:
            for key in Processing.SIMILAR_WORDS.keys():
                if (len(key.strip()) == len(word.strip())) and (word == key):
                    value = Processing.SIMILAR_WORDS[key]
                    self.tweet = self.near(self.tweet, key, value)

        return self.tweet

    def remove_stopwords(self):
        """
        Remove stopwords
        """
        for word in self.tweet.split():
            for stopword in Processing.STOPWORDS:
                if (len(word.strip()) == len(stopword.strip())):
                    if (word == stopword):
                        self.tweet = self.remove_word(self.tweet, stopword)

        return self.tweet

    def remove_mentions(self):
        """
        Remove mentions
        """
        if self.tweet.find('@') != -1:
            self.tweet = self.remove(self.tweet, '@')

        return self.tweet

    def remove_links(self):
        """
        Remove links
        """
        if self.tweet.find('http') != -1:
            self.tweet = self.remove(self.tweet, 'http')

        return self.tweet

    def remove_solitary_letters(self):
        """
        Solitary letters can be removed
        """
    	for key in Processing.SOLITARY_LETTERS:
    		self.tweet = self.near(self.tweet, key, '')

    	return self.tweet

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

    UNICODE_ACCENTED_LETTERS = {
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

    DOUBLE_LETTERS = {
        'aa': 'a', 'ee': 'e', 'ii': 'i', 'ooo': 'o', 'uu': 'u', 'ddd': 'dd',
        'ff': 'f', 'hh': 'h', 'zz': 'z', 'rsrs': 'rs', 'rsr': 'rs','ll': 'l',
        'mm': 'm', 'nn': 'n', 'rrr': 'rr', 'sss': 'ss', 'ttt': 't'
    }

    SPECIAL_CHARACTERS = {
        '\u00ba': '', '\u00bb': '', '\u00ac': '', '\u2013': '', '\u2026': '',
        '\u2019': '', '\u200e': '', '\u200b': '', '\u00b4': '', '\u25bd': '',
        '\u201c': '', '\u201d': '', '\u266a': '', '\u2665': '', '\u267a': ''
    }

    SIMILAR_WORDS = {
        'axu': 'acho', 'achu': 'acho', 'axo': 'acho', 'agr': 'agora',
        'aki': 'aqui', 'aqi': 'aqui', 'aq': 'aqui', 'akela': 'aquela',
        'blz': 'beleza', 'ctz': 'certeza', 'cmg': 'comigo', 'gnt': 'gente',
        'dakele': 'daquele', 'daki': 'daqui', 'fikar': 'ficar', 'eh': 'e',
        'fika': 'ficar', 'dps': 'depois', 'hj': 'hoje', 'hje': 'hoje',
        'jah': 'ja', 'kd': 'cade', 'ki': 'que', 'mt': 'muito', 'soh': 'so',
        'mto': 'muito', 'msm': 'mesmo', 'memo': 'mesmo', 'mermo': 'mesmo',
        'neh':'ne', 'nois': 'nos', 'okay': 'ok', 'p': 'para', 'tah': 'ta',
        'pq': 'porque', 'prq': 'porque', 'pque': 'porque', 'vamo': 'vamos',
        'pqe': 'porque', 'poko': 'pouco', 'qe': 'que', 'qm': 'quem',
        'qnto': 'quanto', 'tamo': 'estamos', 'tb': 'tambem', 'tbm': 'tambem',
        'vc': 'voce', 'vcs': 'voce', 'v6': 'voce'
    }

    STOPWORDS = [
        "rt", "a", "as", "ao", "aos", "ate", "abaixo", "aca", "acaso", "acola",
        "acula", "ademais", "adentro", "afora", "agorinha", "ah", "ainda",
        "alem", "algo", "alias", "aonde", "apesar", "ate", "atraves", "b", "c",
        "ca", "comigo", "conosco", "consigo", "contigo", "contudo", "convosco",
        "cuja", "cujas", "cujo", "cujos", "com", "como", "d", "de", "do", "dos",
        "da", "dai", "dali", "das", "dele", "deles", "dela", "delas", "depois",
        "daquela", "daquelas", "daquele", "daqueles", "daqui", "daquilo",
        "dessa", "dessas", "desse", "desses", "desta", "destas", "deste",
        "destes", "detras", "devera", "deveras", "diante", "disso", "disto",
        "donde", "duma", "dumas", "duns", "durante", "e", "eh", "eia", "eis",
        "em", "ele", "eles", "ela", "elas", "esta", "estas", "estou", "este",
        "estes", "eu", "entre", "era", "eram", "esse", "esses", "essa", "essas",
        "estao", "aquele", "aqueles", "aquela", "aquelas", "aquilo", "estamos",
        "estive", "esteve", "estivemos", "estiveram", "estava", "estavam",
        "estivera", "estiveramos", "esteja", "estejamos", "estejam",
        "estivesse", "estivessemos", "estivessem", "estiver", "estivermos",
        "estiverem", "enfim", "enquanto", "entanto", "entao", "entretanto",
        "exceto", "f", "foi", "foram", "fosse", "fossemos", "fossem", "for",
        "formos", "forem", "fui", "fomos", "foram", "fora", "foramos", "g", "h",
        "hem", "hum", "ha", "havia", "hei", "havemos", "hao", "houve",
        "houvemos", "houveram", "houvera", "houveramos", "haja", "hajamos",
        "hajam", "houvesse", "houvessemos", "houvessem", "houver", "houvermos",
        "houverem", "houverei", "houvera", "houveremos", "houverao", "houveram",
        "houveria", "houveriamos", "houveriam", "i", "idem", "inclusive",
        "isso", "isto", "j", "ja", "k", "ker", "l", "la", "las", "lhe", "lhes",
        "lha", "lhas", "lho", "lhos", "logo", "m", "mas", "mais", "mesma",
        "mesmas", "mesmo", "mesmos", "me", "meu", "meus", "minha", "minhas",
        "mim", "mui", "no", "nos", "na", "nas", "nas", "numa", "numas", "nem",
        "nosso", "nossa", "nossos", "nossas", "nalgum", "nalguma", "nalgumas",
        "nalguns", "naquela", "naquelas", "naquele", "naqueles", "naquilo",
        "nela", "nelas", "nele", "neles", "nessa", "nessas", "nesse", "nesses",
        "nesta", "nestas", "neste", "nestes", "ninguem", "nisso", "nisto",
        "noutra", "noutras", "noutro", "noutros", "nuns", "o", "os", "ou",
        "ola", "onde", "opa", "ora", "outra", "outras", "outrem", "outro",
        "outrora", "outros", "outrossim", "p",  "para", "por", "pelo", "pelos",
        "pela", "pelas", "per", "perante", "pero", "pois", "porem", "porque",
        "portanto", "porventura", "possivelmente", "posteriormente", "pra",
        "praquela", "praquelas", "praquele", "praqueles", "praquilo", "pras",
        "prela", "prelas", "prele", "preles", "preste", "prestes", "q", "que",
        "quando", "quem", "qual", "quais", "qualquer", "quaisquer", "r", "s",
        "se", "seu", "seus", "sua", "suas", "ser", "só", "so", "sem", "seja",
        "sejamos", "sejam", "serei", "sera", "seremos", "serao", "seria",
        "seriamos", "seriam", "sou", "somos", "sao", "saum", "sequer", "t",
        "ta", "tem", "tens", "tambem", "tenha", "tenhamos", "tenham", "tivesse",
        "tivessemos", "tivessem", "tiver", "tivermos", "tiverem", "terei",
        "tera", "teremos", "terao", "teria", "teriamos", "teriam", "tinha",
        "tenho", "tinhas", "tinham", "tive", "teve", "tivemos", "tiveram",
        "tivera", "teu", "tua", "teus", "tuas", "tenho", "temos", "tu", "te",
        "tal", "tais", "todavia", "u", "um", "uma", "umas", "uns", "voce",
        "voces", "vc", "vcs", "oce", "oces", "ces","vos", "vossa", "vossas",
        "vossos", "vulgo", "visto", "x", "z", "w", "y", "0", "1", "2", "3", "4",
        "5", "6", "7", "8", "9", "addthis", "via"
    ]

    SOLITARY_LETTERS = {
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z', 'w'
    }
