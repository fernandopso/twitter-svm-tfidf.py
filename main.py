# !/usr/bin/env python
# -*- coding: utf-8 -*-
from cli import Cli
from storage import Storage
from collect import Collect
from training import Training
from mining.mining import Mining

if __name__ == '__main__':
    cli = Cli()
    cli.clear_terminal()
    cli.dashboard()
    cli.waiting_input()

    while cli.option != "x":
        if cli.option == "h":
            cli.help()

        elif cli.option == "c":
            c = Collect()
            c.connect_with_twitter()
            tweets = c.search_tweets()
            storage = Storage(tweets, "collect")
            storage.save()

        elif cli.option == "t":
            # Load files
            data = Storage([], 'collect').load()

            # Training of tweets
            tweets = Training(data).evaluate()

            # Save tweets
            Storage(tweets, "trained").save()

        elif cli.option == "p":
            collect_files = Storage([], 'collect').load()
            trained_files = Storage([], 'trained').load()

            Mining(collect_files, trained_files).start()

        elif cli.option == "tweets":
            data = Storage([], 'collect').load()
            cli.tweets_colleted(data)

        elif cli.option == "tweets trained":
            data = Storage([], 'trained').load()
            cli.tweets_trained(data)

        cli.waiting_input()

    cli.finished()
