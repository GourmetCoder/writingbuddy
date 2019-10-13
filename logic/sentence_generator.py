import numpy as np
import logic.file_loader as file_loader
import collections
import random

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
        links = self._make_links(self.corpus)
        self.single_word_dict = {}
        self.double_word_dict = {}
        self.triple_word_dict = {}
        self.quad_word_dict = {}
        self.similarity_helper = set()
        self.used_names = set()
        capitals = set()
        names = set()
        loading_amount = 0
        amount = 0
        generation_text = "Generating links"
        for word_1, word_2, word_3, word_4, word_5 in links:
            loading_amount += 1
            amount += 1
            if loading_amount == 100000:
                loading_amount = 0
                print (generation_text)
                generation_text = generation_text + "."
            self._add_to_single_words(word_1, word_2)
            self._add_to_double_words(word_1, word_2, word_3)
            self._add_to_triple_words(word_1, word_2, word_3, word_4)
            self._add_to_quad_words(word_1, word_2, word_3, word_4, word_5)
            self._add_to_capitals(word_1, capitals)
            self._add_to_names(word_1, word_2, names)
        self.capitals = list(capitals)
        self.names = list(names)
        print("Data generated from " + str(amount) + " words.")
        print("\n")

    def _clean_word(self, word):
        word = word.replace(".", '').replace(",", '').replace("!", '').replace("?", '').replace("(", '').replace(")", '').replace("'", '').replace('"', '').replace(";", "")
        return word.lower()

    def _add_to_capitals(self, word, capitals):
        if word not in capitals and (word[0].isupper() or (len(word) > 1 and word[1].isupper())) and word[-1] not in self.end_characters and word[-1] not in self.initial_ends:
            capitals.add(word)

    def _add_to_names(self, word_1, word_2, names):
        if word_1[-1] not in self.end_characters:
            if len(word_1) > 2 and word_1[-2] not in self.end_characters:
                if self._add_to_sets_checker(word_2):
                    names.add(word_2)
    
    def _add_to_sets_checker(self, word):
        if word[0].isupper() and word.isupper() != True and word[:-1].isupper() != True:
            return "'" not in word and '.' not in word and ',' not in word and '…' not in word and '?' not in word and '!' not in word and '"' not in word and ':' not in word and '-' not in word and '/' not in word and '(' not in word and ')' not in word
        else:
            return False

    def _add_to_single_words(self, word_1, word_2):
        if word_1 in self.single_word_dict.keys():
            self.single_word_dict[word_1].append(word_2)
        else:
            self.single_word_dict[word_1] = [word_2]

    def _add_to_double_words(self, word_1, word_2, word_3):
        if (word_1, word_2) in self.double_word_dict.keys():
            self.double_word_dict[(word_1, word_2)].append(word_3)
        else:
            self.double_word_dict[(word_1, word_2)] = [word_3]

    def _add_to_triple_words(self, word_1, word_2, word_3, word_4):
        if (word_1, word_2, word_3) in self.triple_word_dict.keys():
            self.triple_word_dict[(word_1, word_2, word_3)].append(word_4)
        else:
            self.triple_word_dict[(word_1, word_2, word_3)] = [word_4]

    def _add_to_quad_words(self, word_1, word_2, word_3, word_4, word_5):
        if (word_1, word_2, word_3, word_4) in self.quad_word_dict.keys():
            self.quad_word_dict[(word_1, word_2, word_3, word_4)].append(word_5)
        else:
            self.quad_word_dict[(word_1, word_2, word_3, word_4)] = [word_5]

    def _make_links(self, corpus):
        for i in range(len(corpus)-4):
            yield(corpus[i], corpus[i+1], corpus[i+2], corpus[i+3], corpus[i+4])

    def generate_sentence(self, start_word=None, final_exceptions=[]):
        rand = random.Random()
        if(start_word==None):
            first_word = np.random.choice(self.capitals)
        else:
            first_word = start_word
        chain = [first_word]
        attempt = 0
        while True:
            attempt += 1
            sentence_count = collections.Counter(' '.join(chain))
            word = self._get_next_word(chain, rand)
            if sentence_count['"'] % 2 == 0:
                if len(word) >= 1:
                    if word[-1] != '"' or (word[0] == '"' and word[-1] == '"'):
                        chain.append(word)
                    elif attempt >= 5000:
                        chain.append(word.replace('"', ''))
                        attempt = 0
                else:
                    word = "."
                    chain.append(".")
            else:
                if len(word) >= 1 and word[0] != '"':
                    chain.append(word)
                elif len(word) >= 1 and  attempt >= 5000:
                    chain.append(word.replace('"', ''))
                    attempt = 0
                else:
                    word = "."
                    chain.append(word)
            sentence_count = collections.Counter(' '.join(chain))
            if word[-1] in self.end_characters and word.lower() not in final_exceptions:
                if sentence_count['"'] % 2 == 0:
                    break
        if start_word != None:
            return ' '.join(chain[1:len(chain)])
        return ' '.join(chain)
    
    def _get_next_word(self, chain, rand):
        if len(chain) == 1:
            word = self._chain_length_1(chain)
        elif len(chain) == 2:
            word = self._chain_length_2(chain, rand)
        elif len(chain) == 3:
            word = self._chain_length_3(chain, rand)
        else:
            word = self._chain_length_4(chain, rand)
        if word in self.names:
            if len(self.used_names) > 0:
                if word not in self.used_names:
                    if rand.randrange(10) < min(8,len(self.used_names)):
                        word = list(self.used_names)[rand.randrange(len(self.used_names))]
        return word

    def _chain_length_1(self, chain):
        singles = self.single_word_dict.get(chain[-1])
        if singles != None and singles != []:
            return np.random.choice(self.single_word_dict[chain[-1]])
        else:
            return ""

    def record_names_from_sentence(self, sentence):
        for word in sentence.split(" "):
            if word in self.names:
                if word not in self.used_names:
                    self.used_names.add(word)

    def _chain_length_2(self, chain, rand):
        if rand.randrange(10) < 1:
            return self._chain_length_1(chain)
        doubles = self.double_word_dict.get( (chain[-2], chain[-1]) )
        if doubles == None or doubles == []:
            return self._chain_length_1(chain)
        else:
            return np.random.choice(self.double_word_dict[ (chain[-2], chain[-1]) ])

    def _chain_length_3(self, chain, rand):
        if rand.randrange(10) < 1:
            return self._chain_length_2(chain, rand)
        triples = self.triple_word_dict.get( (chain[-3], chain[-2], chain[-1]) )
        if triples == None or triples == []:
            return self._chain_length_2(chain, rand)
        else:
            return np.random.choice(self.triple_word_dict[ (chain[-3], chain[-2], chain[-1]) ])

    def _chain_length_4(self, chain, rand):
        if rand.randrange(10) < 2:
            return self._chain_length_2(chain, rand)
        quads = self.quad_word_dict.get( (chain[-4], chain[-3], chain[-2], chain[-1]) )
        if quads == None or quads == []:
            return self._chain_length_3(chain, rand)
        else:
            return np.random.choice(self.quad_word_dict[ (chain[-4], chain[-3], chain[-2], chain[-1]) ])

