# Original code was written by Ben Shaver in https://towardsdatascience.com/simulating-text-with-markov-chains-in-python-1a27e6d13fc6
# This code is slightly edited version

import numpy as np
import logic.file_loader as file_loader

class SenteceGenerator:
    def __init__(self, path, clean_list=[]):
        self.end_characters = [
            ".",
            "!",
            "?"
        ]
        self.initial_ends = [
            '"',
            "”"
        ]
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
        if word not in capitals and word[0].isupper() and word[len(word)-1] not in self.end_characters and word[len(word)-1] not in self.initial_ends:
            capitals.add(word)
    
    def _add_to_words(self, word_1, word_2):
        if word_1 in self.word_dict.keys():
            self.word_dict[word_1].append(word_2)
        else:
            self.word_dict[word_1] = [word_2]

    def make_pairs(self, corpus):
        for i in range(len(corpus)-1):
            yield(corpus[i], corpus[i+1])

    def generate_sentence(self, start_word=None, final_exceptions=[]):
        if(start_word==None):
            start_word = np.random.choice(self.capitals)
        first_word = start_word
        chain = [first_word]
        while True:
            word = np.random.choice(self.word_dict[chain[-1]])
            chain.append(word)
            if word[len(word)-1] in self.end_characters and word.lower() not in final_exceptions:
                break
        return ' '.join(chain)