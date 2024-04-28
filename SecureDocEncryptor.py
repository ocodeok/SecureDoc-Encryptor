class SecureDocEncryptor:
    def __init__(self, data, cryptographer):
        self.data = data
        self.cryptographer = cryptographer()

    def get_data(self):
        return self.data

    def encrypt_data(self):
        self.data = self.cryptographer.encrypt(self.data)

    def decrypt_data(self):
        self.data = self.cryptographer.decrypt(self.data)