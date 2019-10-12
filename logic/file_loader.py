class FileLoader:
    def __init__(self, path):
        self.path = path
    
    def load_file(self, clean_list=[]):
        loaded_file = open(self.path, encoding='utf8').read()
        for pair in clean_list:
            loaded_file = loaded_file.replace(pair[0], pair[1])
        return loaded_file