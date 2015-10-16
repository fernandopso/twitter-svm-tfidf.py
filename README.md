mining-svm-tfidf
================

Collecting, training and mining data from Twitter using Support Vector Machine and Term Frequency–Inverse Document Frequency.

## Tested with Operating System

The following operating system versions are supported:

```
$ lsb_release -a
Distributor ID:	elementary OS
Description:	elementary OS Freya
Release:	0.3.1
Codename:	freya

$ uname -mrs
Linux 3.19.0-30-generic x86_64
```

## Dependencies

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


### Python Packages

Install with [pip](https://pip.pypa.io/en/stable/)

```
pip install -r requirements.txt
```

### Natural Language Toolkit - http://www.nltk.org/

```
python -m nltk.downloader all
```

Or download from [Python Interpreter](https://docs.python.org/2/tutorial/interpreter.html)

```
import nltk
nltk.download()
```

A new window should open, showing the NLTK Downloader. Press d and type all

### Environment Variables

Set your twitter credentials from [Twitter Application Manager](https://apps.twitter.com/)

```
export CONSUMER_KEY="0000000000000000000"
export CONSUMER_SECRET="1111111111111111"
export ACCESS_TOKEN="2222222222222222222"
export ACCESS_TOKEN_SECRET="333333333333"
```

### Finally

```
python main.py
```
