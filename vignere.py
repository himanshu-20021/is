import numpy as np
def encrypt(plainText,key):
    plainText=[ord(x)-65 for x in plainText]
    key=[ord(x)-65 for x in key]
    plainText=np.array(plainText)
    key=np.array(key)
    cipherText= (plainText+key)%26
    cipherText=[chr(x+65) for x in cipherText]
    return ''.join(cipherText)
def decrpytion(cipherText,key):
    cipherText=[ord(x)-65 for x in cipherText]
    key=[ord(x)-65 for x in key]
    cipherText=np.array(cipherText)
    key=np.array(key)
    plainText= (cipherText-key)%26
    plainText=[chr(x+65) for x in plainText]
    return ''.join(plainText)
plainText=input("Enter the plain text: ")
key=input("Enter the key: ")
if(len(key)!=len(plainText)):
    key+=plainText[0:abs(len(key)-len(plainText))]
cipherText=encrypt(plainText,key)
print(cipherText)
original=decrpytion(cipherText,key)
print(original)