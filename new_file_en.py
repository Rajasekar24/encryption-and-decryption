import base64
import os
from cryptography.fernet import Fernet

# Get the key from the file
file = open('key.key', 'rb')
key = file.read()
file.close()
print(key)

#  Open the file to encrypt
with open('new_ms.txt', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)
print(encrypted)
# Write the encrypted file
with open('secret.rs', 'wb') as f:
    f.write(encrypted)
