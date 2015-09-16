# !/usr/bin/env python
# -*- coding: utf-8 -*-
from cli import Cli
from storage import Storage
from collect.collect import Collect
from training.training import Training
from mining.mining import Mining

if __name__ == '__main__':
    cli = Cli()
    cli.dashboard()
    cli.waiting_input()

    while cli.option != "x":
        cli.clear_terminal()

        if cli.option == "c":
            c = Collect()
            c.connect_with_twitter()
            tweets = c.search_tweets()
            storage = Storage(tweets, "collect")
            storage.save()
        elif cli.option == "t":
            # Load files
            datas = Storage([], 'load').files_collect()

            # Training of tweets
            tweets = Training(datas).evaluate()

            # Save tweets
            Storage(tweets, "trained").save()
        elif cli.option == "p":
            Mining()

        cli.dashboard()
        cli.waiting_input()

    cli.finished()
