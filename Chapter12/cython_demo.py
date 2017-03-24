from nltk.corpus import movie_reviews
from nltk import NaiveBayesClassifier
from nltk.classify import accuracy
import cython_module as cm
import cytoolz
from core import label_docs
from core import filter_corpus
from core import split_data


def select_word_features(corpus):
    words = cytoolz.frequencies(filtered)
    sorted_words = sorted(words, key=words.get)
    N = int(.02 * len(sorted_words))

    return sorted_words[-N:]

def match(a, b):
    return set(a.keys()).intersection(b)

def doc_features(doc):
    doc_words = cytoolz.frequencies(cm.filter_sw(doc))

    # initialize to 0
    features = zero_features.copy()

    word_matches = match(doc_words, word_features)

    for word in word_matches:
        features[word] = (doc_words[word])

    return features

def make_features(docs):
    return [(doc_features(d), c) for (d,c) in docs]

if __name__ == "__main__":
    labeled_docs = label_docs()

    filtered = filter_corpus()
    word_features = select_word_features(filtered)
    zero_features = dict.fromkeys(word_features, 0)
    featuresets = make_features(labeled_docs)
    train_set, test_set = split_data(featuresets)
    classifier = NaiveBayesClassifier.train(train_set)
    print("Accuracy", accuracy(classifier, test_set))
    print(classifier.show_most_informative_features())
