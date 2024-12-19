# Author: Devashish Roy, Roll No: 2024PGCSIS08
# Assignment No: 01
# a) Implementation of Euclidean Algorithm.
# b) Implementation Extended Euclidean Algorithm.
# c) Using Extended Euclidean Algorithm to find the inverse of a number in GF(p).

# Basic Euclidean Algorithm
def euclidean_algorithm(a, b):
    while(b != 0 or b > 0):
        r = a % b
        a = b
        b = r

    return a
 
def main():
    a = int(input("Input 1st Number: "))
    b = int(input("Input 2nd Number: "))
    print(f"GCD of {a} and {b} is {euclidean_algorithm(a, b)}.")

if __name__ == "__main__":
    main()