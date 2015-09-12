# !/usr/bin/env python
# -*- coding: utf-8 -*-
from cli import Cli
from collect.collect import Collect
from training.training import Training
from mining.Mining import Mining

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
            t = Training()
            t.load_files()
            t.display_tweets()
        elif cli.option == "p":
            Mining()

        cli.dashboard()
        cli.waiting_input()

    cli.finished()
