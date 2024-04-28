class SecureDocEncryptor:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

        self.data = self.read_data()

    def read_data(self):
        file = open(self.path_to_file, 'r', encoding='utf8')
        return file.read()

    def get_data(self):
        return self.data
