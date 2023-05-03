def encryption(plainText,key):
    msg=''
    for x in plainText:
        if ord(x)>=97 and ord(x)<=122:
            msg+=chr((((ord(x)-97)+key)%26)+65)
        else:
            msg+=x
    return msg
def decryption(cipherText,key):
    msg=''
    for x in cipherText:
        if ord(x)>=65 and ord(x)<=90:
            msg+=chr((((ord(x)-65)-key)%26)+97)
        else:
            msg+=x
    return msg

plainText=input("Enter the plain text: ")
key=int(input('Enter the key number: '))
cipherText=encryption(plainText,key)
original=decryption(cipherText,key)
print('The cipher text is ',cipherText)
print('Plain text after decryption is ',original)