# Author: Devashish Roy, Roll No: 2024PGCSIS08
# Assignment No: 08
# Implementation of Standard Asymmetric Block Ciphers-Part II
# c) Elgamal Cryptosystems
# d) Elliptic Curve Cryptography

# Elliptic Curve Cryptography - Encryption and Decryption
print("ECC Encryption and Decryption: \n")

import tinyec.ec as ec
import warnings
warnings.simplefilter("error", UserWarning)

def is_prime(n):
    if n <= 1:
        return False
    
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def printKey(privateKey):
    return (privateKey.x, privateKey.y)

flag = True
while(flag):
    p = int(input("Enter Prime No: "))
    if(is_prime(p)):
        flag = False
    else:
        print("Error: Not a valid Prime No, enter a Prime No.")

flag = True
while(flag):
    a = int(input("Enter a for E(a, b): "))
    b = int(input("Enter b for E(a, b): "))

    condition = 4 * pow(a, 3) + 27 * pow(b, 2)

    if(condition != 0):
        flag = False
    else:
        print("Error: Not valid E(a, b), enter valid E(a, b).")

flag = True
while(flag):
    x = int(input("Enter x for G(x, y): "))
    y = int(input("Enter y for G(x, y): "))
    g = (x, y)
    n = 5
    h = 1

    field = ec.SubGroup(p, g, n, h)
    try:
        curve = ec.Curve(a, b, field, "field")
        flag = False
    except UserWarning:
        print("Error: x and y point is not in the curve.")

Bob_PrivateKey = int(input("Enter Bob Private Key: "))
Bob_PublicKey = Bob_PrivateKey * curve.g
print("Bob Private Key:", Bob_PrivateKey)
print("Bob Public Key:", printKey(Bob_PublicKey))
print()

flag = True
while(flag):
    Mx = int(input("Message Coordinate x: "))
    My = int(input("Message Coordinate y: "))

    try:
        M = ec.Point(curve, Mx, My)
        flag = False
    except UserWarning:
        print("Error: Message coordinate is not on curve.")

k = int(input("Random integer k: "))

print("Encryption:")
kG = k * curve.g
C1 = (kG.x, kG.y)

kPb = k * Bob_PublicKey
MaddkPb = M + kPb
C2 = (MaddkPb.x, MaddkPb.y)

print((C1, C2))

print("Decryption")
C1 = kG
C2 = MaddkPb
plaintext = C2 - Bob_PrivateKey * C1

print((plaintext.x, plaintext.y))