# Author: Devashish Roy, Roll No: 2024PGCSIS08
# Assignment No: 07
# Implementation of Standard Asymmetric Block Ciphers-Part I
# a) Rivest-Shamir-Adelman (RSA)
# b) Diffie-Hellman Key Exchange
# c) YAK authenticated key exchange protocol

# Rivest-Shamir-Adelman (RSA)
import random

def gcd(a, b):
    while(b != 0 or b > 0):
        r = a % b
        a = b
        b = r

    return a

def inverse(b, a) :
    r1 = a
    r2 = b
    t1 = 0 
    t2 = 1

    while r2 > 0 :
        q = (int)(r1/r2)
        r = r1 - q * r2
        t = t1 - q * t2

        r1 = r2
        r2 = r
        t1 = t2
        t2 = t

    if(r1 == 1) :
        return t1 % a
    else :
        return -1

def generateKey(p, q):
    n = p * q
    phin = (p-1) * (q-1)

    e_list = []
    for e in range(2, phin):
        if(gcd(e, phin) == 1):
            e_list.append(e)
            # break

    e = e_list[random.randint(0, len(e_list)-1)]
    d = inverse(e, phin)
    while e == d:
        e = e_list[random.randint(0, len(e_list)-1)]
        d = inverse(e, phin)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

def RSA(text, key):
    return pow(text, key[0]) % key[1]

if __name__ == "__main__":
    p = int(input("1st Prime No. : "))
    q = int(input("2nd Prime No. : "))
    
    public_key, private_key = generateKey(p, q)
    print("Public Key:", public_key, "\nPrivate Key:", private_key)
    
    plaintext = int(input("Input plaintext in numeric formate: "))


    ciphertext = RSA(plaintext, public_key)
    print("Encryption -> Ciphertext:", ciphertext)

    plaintext = RSA(ciphertext, private_key)
    print("Decryption -> Plaintext:", plaintext)