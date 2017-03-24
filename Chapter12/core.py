from nltk.corpus import movie_reviews
import random
import cython_module as cm
import cytoolz

def label_docs():
    docs = [(list(movie_reviews.words(fid)), cat)
            for cat in movie_reviews.categories()
            for fid in movie_reviews.fileids(cat)]
    random.seed(42)
    random.shuffle(docs)

    return docs

def match(a, b):
    return set(a.keys()).intersection(b)

def filter_corpus():
    review_words = movie_reviews.words()
    print("# Review Words", len(review_words))
    res = cm.filter_sw(review_words)
    print("# After filter", len(res))

    return res

def select_word_features(corpus):
    words = cytoolz.frequencies(corpus)
    sorted_words = sorted(words, key=words.get)
    N = int(.02 * len(sorted_words))

    return sorted_words[-N:]

def split_data(sets):
    return sets[200:], sets[:200]
