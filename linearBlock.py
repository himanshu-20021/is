import numpy as np

n = int(input("Enter the number of code bits: "))
k = int(input("Enter the number of message bits: "))

parity = np.array(list(map(int, input("Enter the parity bits: ").strip().split()))).reshape((k, n-k))

gen = np.append(np.identity(k, dtype=int), parity, axis=1)
print(gen)

def encode(msg):
    sent = np.array(list(map(int, msg.zfill(n-k))))
    code = np.matmul(sent, gen) % 2
    return "".join(map(str, code))

    # print("Message\t Code")
    # for i in range(pow(2, n - k)):
    #     msg = np.array(list(map(int, bin(i)[2:].zfill(n - k))))
    #     code = np.matmul(msg, gen) % 2
    #     print("".join(map(str, msg)), "\t", "".join(map(str, code)))

def decode(msg):
    sent = np.array(list(map(int, msg)))

    rcvd = sent.copy()
    
    if np.random.randint(0, 2):
        # corrupt a random bit
        pos = np.random.randint(0, len(rcvd))
        print("Corrupting bit at position", pos)
        rcvd[pos] = (rcvd[pos] + 1) % 2
    
    print("Received: ", "".join(map(str, rcvd)))
    
    H = np.append(parity.T, np.identity(n - k, dtype=int), axis=1)
    syndrome = np.matmul(rcvd, H.T) % 2
    
    if np.all(syndrome == 0):
        print("No error")
    else:
        pos = np.where(np.all(H.T == syndrome, axis=1))[0][0]
        print("Error at position", pos)
        rcvd[pos] = (rcvd[pos] + 1) % 2

    return "".join(map(str, rcvd))

msg = input("Enter the message: ")

encoded = encode(msg)
print("Encoded: ", encoded)

decoded = decode(encoded)
print("Decoded: ", decoded)

original_msg = decoded[:k]
print("Original message: ", original_msg)