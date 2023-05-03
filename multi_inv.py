def multi_inv(num, base):
    for i in range(1, base):
        if (num * i) % base == 1:
            return i
    
    return -1

num = int(input("Enter the number: "))
base = int(input("Enter the base: "))

inv = multi_inv(num, base)

if inv == -1:
    print("Multiplicative inverse for", num, "in base", base, "does not exist.")
else:
    print("Multiplicative inverse:", inv)