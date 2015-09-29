#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import listdir
from time import gmtime, strftime
from json import dump, loads

class Storage(object):
    """
    Classe for save and open files

    required params:
        @files is a list of json
        @output_type is a type for save in the correct folder
    """

    COLLECT_FOLDER = './data/collect/'
    TRAINED_FOLDER = './data/trained/'

    def __init__(self, files, output_type):
        self.files = files

        if output_type == 'collect':
            self.output_type = Storage.COLLECT_FOLDER
        elif output_type == 'trained':
            self.output_type = Storage.TRAINED_FOLDER

    def save(self):
        """"
        Save file of json in file
        """

        # Create file path based in output type for current date
        f = self.output_type + '/' + strftime("%Y_%m_%d", gmtime())

        # Open file
        outfile = open(f, 'a')

        for json in self.files:
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
        Open all files in directoy data/collect/ and restore json dump
        """

        folder = listdir(self.output_type)

        for file_name in folder:
            with open(self.output_type + file_name, 'r') as data:
                for tweet in data.readlines():
                    self.files.append(loads(tweet))

        return self.files