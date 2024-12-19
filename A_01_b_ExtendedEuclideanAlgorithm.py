# Author: Devashish Roy, Roll No: 2024PGCSIS08
# Assignment No: 01
# a) Implementation of Euclidean Algorithm.
# b) Implementation Extended Euclidean Algorithm.
# c) Using Extended Euclidean Algorithm to find the inverse of a number in GF(p).

# Extended Euclidean Algorithm
def extended_euclidean(a, b) :
    if b > a:
        r1 = b
        r2 = a

    r1 = a
    r2 = b

    s1 = 1
    s2 = 0

    t1 = 0
    t2 = 1

    while r2 != 0 or r2 > 0:
        q = (int) (r1/r2)
        r = r1 - q * r2
        s = s1 - q * s2
        t = t1 - q * t2

        r1 = r2
        r2 = r

        s1 = s2
        s2 = s
        
        t1 = t2
        t2 = t
    
    return(r1, s1, t1)

def main():
    a = int(input("Input 1st Number: "))
    b = int(input("Input 2nd Number: "))
    print(f"(GCD, s, t) of {a} and {b} : {extended_euclidean(a, b)}.")

if __name__ == "__main__":
    main()