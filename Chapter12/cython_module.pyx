from collections import defaultdict
from nltk.corpus import stopwords
from nltk.corpus import names
from libc.string cimport strlen

sw = set(stopwords.words('english'))
all_names = set([name.lower() for name in names.words()])

def isStopWord(w):
     py_byte_string = w.encode('UTF-8')
     cdef char* c_string = py_byte_string
     truth = (w in sw) or (w in all_names) or (not w.isalpha()) or (strlen(c_string) == 1)
     return truth

def filter_sw(words):
    return [w.lower() for w in words if not isStopWord(w.lower())]

def freq_dict(words):
    dd = defaultdict(int)

    for word in words:
        dd[word] += 1

    return dd
