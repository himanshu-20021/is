import numpy as np
import random
def encoding(msg,parity):
    I=np.identity(len(msg))
    G=np.concatenate((parity,I),axis=1).astype(int)
    print("G",G)
    codeWord=np.matmul(msg,G)%2
    return codeWord

def decoding(res,parity):
    I=np.identity(len(res)-parity.shape[0])
    H=np.concatenate((I,parity.T),axis=1).astype(int)
    print("H",H)
    s=np.matmul(res,H.T).astype(int)%2
    print("The syndrome for the codeWord is ",s)
    if (s==0).all(0):
        print("No Error the received codeWord")
    else:
        index=np.where((H.T==s).all(1))[0]
        e=np.zeros(len(res)).astype(int)
        e[index]=1
        correct=res^e
        print("Error vector is ",e)
        print("Corrected codeWord is ",correct)
def introduceError(codeWord):
    index=random.randrange(0,len(codeWord))
    codeWord[index]=1
    return codeWord

msg=np.array(input("Enter the message bits : ").split()).astype(int)
parity=np.array(input("Enter the parity bits : ").split()).astype(int).reshape((len(msg),-1))
codeWord=encoding(msg,parity)
print("CodeWord is ",codeWord)
res=introduceError(codeWord)
print("Recieved CodeWord is ",res)
decoding(res,parity)