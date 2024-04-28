# SecureDoc Encryptor

from SecureDocEncryptor import SecureDocEncryptor
from LatinEncryption import LatinEncryption

sec_doc = SecureDocEncryptor("abracadabra.txt")
lat_enc = LatinEncryption()


print(sec_doc.get_data())
print(lat_enc.base_dict)
print(lat_enc.reverse_base_dict)





