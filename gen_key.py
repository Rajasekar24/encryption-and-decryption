import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = 'noonecanreadthisman'
password = password_provided.encode()

salt = b"\x98\\\xf4\x14dEr\r\x15_\x19\x90L+\xb8a"

kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend())

key = base64.urlsafe_b64encode(kdf.derive(password))
print(key)
file = open('key.key', 'wb') #wb = write bytes
file.write(key)
file.close()