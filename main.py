# !/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import sys
from collect.Collect import Collect
from mining.Mining import Mining
from train.Train import Train

if __name__ == '__main__':
    sys.stderr.write("\x1b[2J\x1b[H")

    # Load locale for a text interface
    text = open('./locale/en.yaml')
    text = yaml.load(text.read())

    # Display dashboad
    print text['dashboard']

    option = raw_input("Select an option: ")

    while option != "x":
        option = raw_input("Select an option: ")

        if option == "c":
            Collect()
        elif option == "t":
            Train()
        elif option == "p":
            Mining()
        elif option == "x":
            print "Finished"
