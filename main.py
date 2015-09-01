# !/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import sys
from collect.collect import Collect
from mining.Mining import Mining
from train.Train import Train

class Cli(object):
    """Command-line Application"""

    file_path = './locale/en.yaml'

    def __init__(self):
        self.text = yaml.load(open(self.file_path).read())
        self.option = False

    def dashboard(self):
        print self.text['dashboard']

    def waiting_input(self):
        self.option = raw_input("Select an option: ")
        return self.option

    def clear_terminal(self):
        sys.stderr.write("\x1b[2J\x1b[H")

    def finished(self):
        print 'Finished'

if __name__ == '__main__':
    cli = Cli()
    cli.dashboard()
    cli.waiting_input()

    while cli.option != "x":
        cli.clear_terminal()

        if cli.option == "c":
            c = Collect()
            c.connect_with_twitter()
            c.search_tweets()
            c.save()
        elif cli.option == "t":
            Train()
        elif cli.option == "p":
            Mining()

        cli.dashboard()
        cli.waiting_input()

    cli.finished()
