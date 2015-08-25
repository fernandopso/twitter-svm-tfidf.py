mining-svm-tfidf
================

Course conclusion project for collecting, training, and mining data collected from Twitter using Support Vector Machine and term frequency–inverse document frequency.

## Dependencies

### scikit-learn

Simple and efficient tools for data mining and data analysis http://scikit-learn.org/stable/install.html

```
sudo apt-get install build-essential python-dev python-setuptools \
                     python-numpy python-scipy \
                     libatlas-dev libatlas3gf-base
```

And

```
pip install -U scikit-learn
```

### pymongo

https://api.mongodb.org/python/2.0/tutorial.html

```
pip install pymongo==2
```

### nltk

Natural Language Toolkit - http://www.nltk.org/

```
pip install -U nltk

# After install you need download corpus from nltk
import nltk
nltk.download()

# A new window should open, showing the NLTK Downloader. Press d and type all
```

For Python 2 run the command

```
python -m nltk.downloader all
```

### psutil

https://pypi.python.org/pypi/psutil

```
pip install psutil
```

### PyStemmer

Snowball stemming algorithms, for information retrieval - https://pypi.python.org/pypi/PyStemmer/1.0.1

```
pip install PyStemmer
```

## Run

```
python main.py
```