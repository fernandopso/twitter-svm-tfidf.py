Twitter data mining with Python
==============

[![Build Status](https://travis-ci.org/fernandopso/twitter-svm-tfidf.py.svg?branch=master)](https://travis-ci.org/fernandopso/twitter-svm-tfidf.py)

Using [Support Vector Machine](https://en.wikipedia.org/wiki/Support_vector_machine) and [Term Frequency–Inverse Document Frequency](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) in three steps:

  1. Collect many tweets from Twitter
  2. Classify some tweets with **positive**, **negative** or **neutral**
  3. Predict others tweets

### System dependencies

```
sudo apt-get install build-essential python-dev python-setuptools \
                     python-numpy python-scipy libblas-dev gfortran \
                     libatlas-dev libatlas3gf-base liblapack-dev \
                     libatlas-base-dev
```

If you use Python 3

```
sudo apt-get install python3-minimal
```


### Install Packages

Use [pip](https://pip.pypa.io/en/stable/) with [virtualenv](https://virtualenv.readthedocs.org/en/latest/)

```
pip install -r requirements.txt
```

### Configuration

The [Natural Language Toolkit](http://www.nltk.org/) provide human language data (over 50 corpora and lexical resources) in different languages and formats as **twitter samples**, **RSLP Stemmer** (*Removedor de Sufixos da Lingua Portuguesa*), complete work of Machado de Assis for Brazilian Portuguese language and much more.

For download all corpora

```
python -m nltk.downloader all
```

Or download the corpora of your choice from **Python Interpreter**

```
>>> import nltk
>>> nltk.download()
```

A new window should open, showing the NLTK Downloader.

### Credentials

Set your Twitter credentials from [Twitter Application Manager](https://apps.twitter.com/) for variables: *CONSUMER_KEY*, *CONSUMER_SECRET*, *ACCESS_TOKEN* and *ACCESS_TOKEN_SECRET*.

### Run tests

```
python -m unittest discover
```

### Start

Run the Human-Machine Interface

```
python hmi.py
```

### Example

#### Collect

![collect](https://cloud.githubusercontent.com/assets/3316732/14270116/470048a4-fac1-11e5-8817-69e49744de0a.png)

#### Listing collected tweets

![tweets](https://cloud.githubusercontent.com/assets/3316732/14270159/b5ede956-fac1-11e5-80ea-00aeb78b9e9d.png)

#### Classification

![training](https://cloud.githubusercontent.com/assets/3316732/14270117/47030012-fac1-11e5-86f8-583865ea0c9a.png)

#### Predication

![prediction](https://cloud.githubusercontent.com/assets/3316732/14270118/47060460-fac1-11e5-8a1c-134fa4b65a1f.png)

[Roadmap](https://github.com/fernandopso/twitter-svm-tfidf.py/wiki/Roadmap)
