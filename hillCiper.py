import numpy as np
from math import gcd
def multiInv26(a):
    if gcd(a,26)!=1:
        return -1
    else:
        for i in range(1,26):
            if (a*i)%26==1:
                return i

def encryption(plainText,key):
    m=key.shape[0]
    print(key)
    output=''
    for i in range(0,len(plainText),m):
        block=np.array([ord(x)-97 for x in plainText[i:i+m]])
        print("Block")
        print(block)
        c=np.matmul(block,key)%26
        print("After multiplication")
        print(c)
        output=output+''.join([chr(x+65) for x in c])
        #print(c)
    return output
    
def decryption(ciperText,key):
    m=key.shape[0]
    det=multiInv26(int(np.linalg.det(key)%26))
    if det==-1:
        return -1
    adj=np.round((np.linalg.det(key))*(np.linalg.inv(key)))
    #print(adj)
    invKey=(((det*adj))).astype(int)%26
    print(invKey)
    output=''
    for i in range(0,len(ciperText),m):
        block=np.array([ord(x)-65 for x in ciperText[i:i+m]])
        c=np.matmul(block,invKey)%26
        output=output+''.join([chr(x+97) for x in c])
    return output



# main function
plainText=input("Enter the plain text: ")
plainText=''.join(plainText.split())
m=int(input("Enter number of row of key matrix: "))
n=int(input("Enter number of col of key matrix: "))
key=np.array(input("Enter the elements of key row-wise: ").split()).reshape(m,n).astype(int)
if(len(plainText)%m!=0):
    plainText=''.join([plainText,'x'*(m-(len(plainText)%m))])# to add trailing 'x' if length not multiple of row
ciperText=encryption(plainText,key)
print("Encrypted message: ")
print(ciperText)
original=decryption(ciperText,key)
print("Decrypted message: ")
print(original)
