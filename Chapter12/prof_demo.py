import random
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk import FreqDist
from nltk import NaiveBayesClassifier
from nltk.classify import accuracy

import builtins

try:
    profile = builtins.profile
except AttributeError:
    def profile(func): 
        return func

@profile
def label_docs():
    docs = [(list(movie_reviews.words(fid)), cat)
            for cat in movie_reviews.categories()
            for fid in movie_reviews.fileids(cat)]
    random.seed(42)
    random.shuffle(docs)

    return docs

@profile
def isStopWord(word):
    return word in sw or len(word) == 1

@profile
def filter_corpus():
    review_words = movie_reviews.words()
    print("# Review Words", len(review_words))
    res = [w.lower() for w in review_words if not isStopWord(w.lower())]
    print("# After filter", len(res))

    return res
@profile
def select_word_features(corpus):
    words = FreqDist(corpus)
    N = int(.02 * len(words.keys()))
    return list(words.keys())[:N]

@profile
def doc_features(doc):
    doc_words = FreqDist(w for w in doc if not isStopWord(w))
    features = {}
    for word in word_features:
        features['count (%s)' % word] = (doc_words.get(word, 0))
    return features

@profile
def make_features(docs):
    return [(doc_features(d), c) for (d,c) in docs]

@profile
def split_data(sets):
    return sets[200:], sets[:200]

if __name__ == "__main__":
    labeled_docs = label_docs()

    sw = set(stopwords.words('english'))
    filtered = filter_corpus()
    word_features = select_word_features(filtered)
    featuresets = make_features(labeled_docs)
    train_set, test_set = split_data(featuresets)
    classifier = NaiveBayesClassifier.train(train_set)
    print("Accuracy", accuracy(classifier, test_set))
    print(classifier.show_most_informative_features())
