# SecureDoc Encryptor

from SecureDocEncryptor import SecureDocEncryptor
from LatinEncryption import LatinEncryption

key_phrase = "Иван Рыженков"

sec_doc = SecureDocEncryptor(key_phrase, LatinEncryption)
sec_doc.encrypt_data()

print(sec_doc.get_data())

sec_doc.decrypt_data()
print(sec_doc.get_data())