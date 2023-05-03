import numpy as np

letters = [chr(i) for i in range(65, 65+26)]

print("".join(letters))
np.random.shuffle(letters)
print("".join(letters))

def encrypt(secret):
    msg = []

    for letter in secret:
        msg.append(letters[ord(letter) - 65])

    return "".join(msg)

def decrypt(secret):
    msg = []

    for letter in secret:
        msg.append(chr(letters.index(letter) + 65))

    return "".join(msg)


secret = str(input("Enter the secret to encrypt: ")).replace(" ", "").upper()

encrypted = encrypt(secret)
decrypted = decrypt(encrypted)

print("Encrypted: ", encrypted)
print("Decrypted: ", decrypted)
