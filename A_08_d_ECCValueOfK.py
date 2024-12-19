# Author: Devashish Roy, Roll No: 2024PGCSIS08
# Assignment No: 08
# Implementation of Standard Asymmetric Block Ciphers-Part II
# c) Elgamal Cryptosystems
# d) Elliptic Curve Cryptography

# Elliptic Curve Cryptography - Value of k
import tinyec.ec as ec
import warnings
warnings.simplefilter("error", UserWarning)

def xTimesMultiplication(x):
    return curve.g * x

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

flag = True
while(flag):
    p = int(input("Enter Prime No: \t"))
    if(is_prime(p)):
        flag = False
    else:
        print("Error: Not a valid Prime No, enter a Prime No.")

flag = True
while(flag):
    a = int(input("Enter a for E(a, b): \t"))
    b = int(input("Enter b for E(a, b): \t"))

    condition = 4 * pow(a, 3) + 27 * pow(b, 2)

    if(condition != 0):
        flag = False
    else:
        print("Error: Not valid E(a, b), enter valid E(a, b).")

flag = True
while(flag):
    Px = int(input("Enter x for P(x, y): \t"))
    Py = int(input("Enter y for P(x, y): \t"))
    g = (Px, Py)
    n = 5
    h = 1

    field = ec.SubGroup(p, g, n, h)
    try:
        curve = ec.Curve(a, b, field, "field")
        flag = False
    except UserWarning:
        print("Error: x and y point is not in the curve.")
    
Qx = int(input("Enter x for Q(x, y): \t"))
Qy = int(input("Enter y for Q(x, y): \t"))
Q = (Qx, Qy)

R = (Px, Py)

i = 0
while(Q != R):
    i = i+1
    R = xTimesMultiplication(i)
    Rx = R.x
    Ry = R.y
    R = (Rx, Ry)

print("The value of k: \t", i)