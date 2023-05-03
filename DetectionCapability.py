import numpy as np
def messageBit(k):
    message=[]
    for i in range(2**k):
        for x in list(np.binary_repr(i,k)):
            message.append((x))
    message=np.array(message).reshape((-1,k)).astype(int)
    return message

def generateCodeword(message,parity):
    I=np.identity(message.shape[1])
    G=np.concatenate((parity,I),axis=1).astype(int)
    codeWords=np.matmul(message,G)%2
    return codeWords

def DetectionAndCorrectionCapability(codeWords):
    weights=codeWords.sum(axis=1)
    dmin=weights[weights>0].min()
    correctionCapability=(dmin-1)/2
    detectionCapability=dmin-1
    print("The Linear Block Code is capable of detecting %d bit or fewer number of error."%(detectionCapability))
    print("The Linear Block Code is capable of correcting %d bit or fewer number of error"%(correctionCapability))


k=int(input("Enter the number of bits for message: "))
parity=np.array(input("Enter the parity bits rowise: ").split()).reshape((k,-1)).astype(int)
codeWords=generateCodeword(messageBit(k),parity)
DetectionAndCorrectionCapability(codeWords)
