from cryptography.fernet import Fernet

# Get the key from the file
file = open('key.key', 'rb')
key = file.read()
file.close()
print(key)

#  Open the file to encrypt
with open('secret.rs', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
dencrypted = fernet.decrypt(data)
dencrypted = dencrypted.decode()
print(dencrypted)
# Write the dencrypted file
with open('secret.a', 'w') as f:
    f.write(dencrypted)

