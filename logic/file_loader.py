class FileLoader:
    def __init__(self, path):
        self.path = path
    
    def load_file(self, clean_list=[]):
        loaded_file = open(self.path, encoding='utf8').read()
        for pair in clean_list:
            loaded_file = loaded_file.replace(pair[0], pair[1])
            print("cleaned " + pair[0] + " from the file...")
        return loaded_file

    def write_dict_into_file(self, dictionary: dict):
        writing_file = open(self.path, "w+", encoding='utf8')
        for key in dictionary.keys():
            line = str(key) + "|;|" + str(str(dictionary.get(key))[1:-1])
            writing_file.write(line+"\n")
        writing_file.close()

    def load_file_into_dict(self):
        dictionary = {}
        loaded_file = self.load_file().split("\n")
        for line in loaded_file:
            split = line.split("|;|")
            if line != None and line != '' and line != "\n":
                temp_set = set()
                for word in split[1].split(", "):
                    word = word[1:-1]
                    temp_set.add(word)
                dictionary.update({split[0]: temp_set})
        return dictionary
