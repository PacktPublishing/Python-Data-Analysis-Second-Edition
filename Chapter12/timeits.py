import timeit
import numpy as np

setup = '''
import nltk
import cython_module as cm
import collections
from nltk.corpus import stopwords
from nltk.corpus import movie_reviews
from nltk.corpus import names
import string
import pandas as pd
import cytoolz

sw = set(stopwords.words('english'))
punctuation = set(string.punctuation)
all_names = set([name.lower() for name in names.words()])
txt = movie_reviews.words(movie_reviews.fileids()[0])

def isStopWord(w):
    return w in sw or w in punctuation

def isStopWord2(w):
    return w in sw or w in punctuation or not w.isalpha()

def isStopWord3(w):
    return w in sw or len(w) == 1 or not w.isalpha() or w in all_names

def isStopWord4(w):
    return w in sw or len(w) == 1

def freq_dict(words):
    dd = collections.defaultdict(int)

    for word in words:
        dd[word] += 1

    return dd

def zero_init():
    features = {}

    for word in set(txt):
        features['count (%s)' % word] = (0)

def zero_init2():
    features = {}
    for word in set(txt):
        features[word] = (0)

keys = list(set(txt))

def zero_init3():
    features = dict.fromkeys(keys, 0)

zero_dict = dict.fromkeys(keys, 0)

def dict_copy():
    features = zero_dict.copy()
'''

def time(code, n):
    times = min(timeit.Timer(code, setup=setup).repeat(3, n))

    return round(1000* np.array(times)/n, 3)

if __name__ == '__main__':
    print("Best of 3 times per loop in milliseconds")
    n = 10
    print("zero_init ", time("zero_init()", n))
    print("zero_init2", time("zero_init2()", n))
    print("zero_init3", time("zero_init3()", n))
    print("dict_copy ", time("dict_copy()", n))
    print("\n")

    n = 10**2
    print("isStopWord ", time('[w.lower() for w in txt if not isStopWord(w.lower())]', n))
    print("isStopWord2", time('[w.lower() for w in txt if not isStopWord2(w.lower())]', n))
    print("isStopWord3", time('[w.lower() for w in txt if not isStopWord3(w.lower())]', n))
    print("isStopWord4", time('[w.lower() for w in txt if not isStopWord4(w.lower())]', n))
    print("Cythonized isStopWord", time('[w.lower() for w in txt if not cm.isStopWord(w.lower())]', n))
    print("Cythonized filter_sw()", time('cm.filter_sw(txt)', n))
    print("\n")

    print("FreqDist", time("nltk.FreqDist(txt)", n))
    print("Default dict", time('freq_dict(txt)', n))
    print("Counter", time('collections.Counter(txt)', n))
    print("Series", time('pd.Series(txt).value_counts()', n))
    print("Cytoolz", time('cytoolz.frequencies(txt)', n))
    print("Cythonized freq_dict", time('cm.freq_dict(txt)', n))

