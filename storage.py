#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import gmtime, strftime
from json import dump

class Storage(object):
    """
    Classe for save and open files

    required params:
        @files is a list of json
        @output_type is a type for save in the correct folder
    """
    def __init__(self, files, output_type):
        self.files       = files
        self.output_type = output_type

    def save(self):
        """"
        Save file of json in file
        """

        # Create file path based in output type for current date
        f = './data/' +  self.output_type + '/' + strftime("%Y_%m_%d", gmtime())

        # Open file
        outfile = open(f, 'a')

        for json in self.files:
            dump(json._json, outfile)
            # This is necessary beacause lib json cannot load many jsons
            # Save a file per line and this will work fine
            outfile.write("\n")

        outfile.close()

        return True
