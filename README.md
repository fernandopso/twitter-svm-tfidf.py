mining-svm-tfidf
================

Course project for collecting, training and mining data collected from Twitter using Support Vector Machine and Term Frequency–Inverse Document Frequency.

## Dependencies

```
sudo apt-get install build-essential python-dev python-setuptools \
                     python-numpy python-scipy libblas-dev gfortran \
                     libatlas-dev libatlas3gf-base
```

## Dependencies for Python 3

```
sudo apt-get install python3-minimal
```


### Libs

```
pip install -r requirements.txt
```

### Natural Language Toolkit - http://www.nltk.org/

```
python -m nltk.downloader all
```

or

```
import nltk
nltk.download()

# A new window should open, showing the NLTK Downloader. Press d and type all
```

## Run

```
python main.py
```
