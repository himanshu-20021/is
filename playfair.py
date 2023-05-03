import numpy as np
key = str(input("Enter the key: ")).replace(" ", "").upper()
key.replace('J','I')
for i in range(65,91):
    if ord('J')==i:
        continue
    if chr(i) in key:
        continue
    else:
        key+=chr(i)
key=list(key)
print(key)
key=np.array(key).reshape(-1, 5)
print(key)

def encrypt(plainText):
    msg = list(plainText.replace(" ", "").upper())
    crypted = []

    if len(msg) % 2 != 0:
        msg.append('X')

    for i in range(0, len(msg), 2):
        
        a = np.where(msg[i]==key)
        b = np.where(msg[i+1]==key)
        
        rowA, rowB = a[0], b[0]
        ColA, ColB = a[1], b[1]

        if rowA == rowB:
            crypted.append(list(key[rowA,(ColA+1)%5]))
            crypted.append(list(key[rowB,(ColB+1)%5]))
        elif ColA == ColB:
            crypted.append(list(key[(rowA+1)%5,ColA]))
            crypted.append(list(key[(rowB+1)%5,ColB]))
        else:
            
            crypted.append(list(key[rowA,ColB]))
            crypted.append(list(key[rowB,ColA]))
    crypted=np.array(crypted).flatten()
    return "".join(crypted)

def decrypt(cipherText):
    msg = list(cipherText.replace(" ", "").upper())
    decrypted = []

    for i in range(0, len(msg), 2):
        a = np.where(msg[i]==key)
        b = np.where(msg[i+1]==key)
        
        rowA, rowB = a[0], b[0]
        ColA, ColB = a[1], b[1]

        if rowA==rowB:
            decrypted.append(list(key[rowA,(ColA-1)%5]))
            decrypted.append(list(key[rowB,(ColB-1)%5]))
        elif ColA==ColB:
            decrypted.append(list(key[(rowA-1)%5,ColA]))
            decrypted.append(list(key[(rowB-1)%5,ColB]))
        else:
            decrypted.append(list(key[rowA,ColB]))
            decrypted.append(list(key[rowB,ColA]))

    decrypted=np.array(decrypted).flatten()
    return "".join(decrypted)

plainText = str(input("Enter the secret: ")).upper()
msg=''
for i in range(26):
    double = chr(65 + i) * 2
    plainText = plainText.replace(double, double[0] + 'X' + double[1])

print(plainText)
encrypted = encrypt(plainText)
decrypted = decrypt(encrypted)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
