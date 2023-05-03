import numpy as np
def encryption(plainText,depth):
    msg=np.array(list(plainText)).reshape((depth,-1),order='F')
    msg=msg.flatten()
    output=''.join(msg)
    output=output.upper()
    return output
def decryption(ciperText,depth):
    msg=np.array(list(ciperText)).reshape((depth,-1)).T
    msg=msg.flatten()
    output=''.join(msg)
    output=output.lower()
    return output


plainText=input("Enter the plain text: ")
plainText=''.join(plainText.split())
depth=2
if len(plainText)%depth!=0:
    plainText=''.join([plainText,'x'*(depth-(len(plainText)%depth))])
ciperText=encryption(plainText,depth)
print(ciperText)
original=decryption(ciperText,depth)
print(original)