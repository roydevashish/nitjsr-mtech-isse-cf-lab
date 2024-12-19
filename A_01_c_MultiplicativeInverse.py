# Author: Devashish Roy, Roll No: 2024PGCSIS08
# Assignment No: 01
# a) Implementation of Euclidean Algorithm.
# b) Implementation Extended Euclidean Algorithm.
# c) Using Extended Euclidean Algorithm to find the inverse of a number in GF(p).

# Inverse of a number n in GF(p)
def multiplicative_inverse(p, n) :
    r1 = p
    r2 = n
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
        return(t1 % p)
    else :
        raise Exception("Multiplicative Inverse does not exist.")

def main():
    n = int(input("Input the number n: "))
    p = int(input("Input p for GF(p): "))
    print(f"Multiplicative inverse of {n} in GF({p}) is {multiplicative_inverse(p, n)}.")

if __name__ == "__main__":
    main()