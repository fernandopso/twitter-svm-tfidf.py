# !/usr/bin/env python
# -*- coding: utf-8 -*-
from app.collect import Collect
from app.miner.mining import Mining
from app.storage import Storage
from app.trainer.training import Training
from app.cli import Cli

def start(cli):
    cli.clear_terminal()
    cli.dashboard()
    cli.waiting_input()

def display_help(cli):
    cli.clear_terminal()
    cli.help()

def collect(cli):
    if not cli.args:
        cli.error(cli.option)
    else:
        tweets = Collect(cli.args[0]).search()
        Storage('collected').save(tweets)
        cli.success(cli.option)

def training():
    data = Storage('collected').load()
    tweets = Training(data).evaluate()
    Storage('trained').save(tweets)

def prediction():
    collect_files = Storage('collected').load()
    trained_files = Storage('trained').load()
    trained_files = Training(trained_files).process_tweets()
    Mining(collect_files, trained_files).start()

if __name__ == '__main__':
    """
    Human-Machine Interface
    """
    cli = Cli()
    start(cli)

    if cli.option == 'x':
        cli.finished()
    else:
        if cli.option == 'h':
            display_help(cli)
        elif cli.option == 'c':
            collect(cli)
        elif cli.option == 't':
            training()
        elif cli.option == 'p':
            prediction()
        elif cli.option == 'tweets':
            data = Storage('collected').load()
            cli.tweets_colleted(data)
        elif cli.option == 'tweets trained':
            data = Storage('trained').load()
            cli.tweets_trained(data)
        elif cli.option == 'tweets metrics':
            collected = Storage('collected').load()
            trained   = Storage('trained').load()
            cli.tweets_metrics(collected, trained)

        cli.waiting_input()
