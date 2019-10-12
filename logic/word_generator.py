# Original code was written by Ben Shaver in https://towardsdatascience.com/simulating-text-with-markov-chains-in-python-1a27e6d13fc6
# This code is slightly edited version

import numpy as np
import logic.file_loader as file_loader

class WordGenerator:
    def __init__(self, path, clean_list=[]):
        origin_file = file_loader.FileLoader(path).load_file(clean_list=clean_list)
        self.corpus = origin_file.split()
        pairs = self.make_pairs(self.corpus)
        self.word_dict = {}
        capitals = set()
        for word_1, word_2 in pairs:
            self._add_to_words(word_1, word_2)
            self._add_to_capitals(word_1, capitals)
        self.capitals = list(capitals)

    def _add_to_capitals(self, word, capitals):
        if word not in capitals and word[0].isupper():
            capitals.add(word)
    
    def _add_to_words(self, word_1, word_2):
        if word_1 in self.word_dict.keys():
            self.word_dict[word_1].append(word_2)
        else:
            self.word_dict[word_1] = [word_2]

    def make_pairs(self, corpus):
        for i in range(len(corpus)-1):
            yield(corpus[i], corpus[i+1])

    def generate_text(self, length, start_word=None):
        if(start_word==None):
            start_word = np.random.choice(self.capitals)
        first_word = start_word
        chain = [first_word]
        n_words = length
        for _ in range(n_words):
            chain.append(np.random.choice(self.word_dict[chain[-1]]))
        return ' '.join(chain)