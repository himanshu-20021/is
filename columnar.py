import numpy as np
from math import ceil
def encryption(plainText,key):
    row=ceil(len(plainText)/len(key))
    if(len(plainText)!=len(key)*row):
        plainText=''.join([plainText,'x'*((len(key)*row)-len(plainText))])
    msg=np.array(list(plainText)).reshape((row,-1))
    msg=msg[:,np.argsort(key)].T
    msg=msg.flatten()#row wise
    msg=''.join(msg)
    msg=msg.upper()
    return msg
def decryption(ciperText,key):
    row=ceil(len(plainText)/len(key))
    msg=np.array(list(ciperText)).reshape((row,-1),order='F')
    msg=msg[:,key-1]
    msg=msg.flatten()
    msg=''.join(msg)
    msg=msg.lower()
    return msg

plainText=input("Enter the plain text: ")
key=input("Enter the key: ")
plainText=''.join(plainText.split())
key=np.array(key.split()).astype(int)
ciperText=encryption(plainText,key)
#ciperText=encryption(ciperText,key)
original=decryption(ciperText,key)
#original=decryption(original,key)
print(ciperText)
print(original)