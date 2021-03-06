# !/usr/bin/env python
# -*- coding: utf-8 -*-
from os import listdir
from time import gmtime, strftime
from json import dump, loads

class Storage(object):
    FOLDERS = {
        'collected': './data/collected/',
        'trained': './data/trained/'
    }

    def __init__(self, output_type):
        self.output_type = Storage.FOLDERS[output_type]

    def save(self, files):
        """"
        Save file of json in file with name like 2015_09_30
        """

        # Create filename based in output type
        f = self.output_type + '/' + strftime("%Y_%m_%d", gmtime())

        outfile = open(f, 'a')

        for json in files:
            if type(json) is dict:
                dump(json, outfile)
            else:
                dump(json._json, outfile)

            # This is necessary beacause lib json cannot load many jsons
            # Save a file per line and this will work fine
            outfile.write("\n")

        outfile.close()

        return True

    def load(self):
        """
        Restore all files collected or trained and return a json of tweets
        """
        files = []

        folder = listdir(self.output_type)

        for file_name in folder:
            with open(self.output_type + file_name, 'r') as data:
                for tweet in data.readlines():
                    files.append(loads(tweet))

        return files
