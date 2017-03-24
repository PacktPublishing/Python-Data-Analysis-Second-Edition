import jug.mapreduce
from jug.compound import CompoundTask
import cython_module as cm
import cytoolz
import pickle

def get_txts():
    return [(1, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'), (2, 'Donec a elit pharetra, malesuada massa vitae, elementum dolor.'), (3, 'Integer a tortor ac mi vehicula tempor at a nunc.')]

def freq_dict(file_words):
    filtered = cm.filter_sw(file_words[1].split())

    fd = cytoolz.frequencies(filtered)

    return fd

def merge(left, right):
    return cytoolz.merge_with(sum, left, right)

merged_counts = CompoundTask(jug.mapreduce.mapreduce, merge, freq_dict, get_txts(), map_step=1)
