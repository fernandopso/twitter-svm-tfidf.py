Twitter data mining in Python
==============

Using [Support Vector Machine](https://en.wikipedia.org/wiki/Support_vector_machine) and [Term Frequency–Inverse Document Frequency](https://en.wikipedia.org/wiki/Tf%E2%80%93idf).

The process of data mining can be realized in three steps after clone this repository, install OS dependencies and configure your credentials of Twitter:

  1. Collect tweets from Twitter
  2. Train some tweets
  3. Analyze other tweets and predict through pattern recognition

## Operating System dependencies

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


### Python Packages required

Install with [pip](https://pip.pypa.io/en/stable/)

```
pip install -r requirements.txt
```

after install Python Packages you need download the [Natural Language Toolkit](http://www.nltk.org/)

```
python -m nltk.downloader all
```

Or download from **Python Interpreter**

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

### Start the Human-Machine Interface

```
python hmi.py
```

### New features?

See [roadmap](https://github.com/fernandopso/twitter-svm-tfidf.py/wiki/Roadmap)
