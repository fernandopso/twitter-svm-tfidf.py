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

## Finally

```
python main.py
```
