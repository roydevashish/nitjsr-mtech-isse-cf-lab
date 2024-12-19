# Author: Devashish Roy, Roll No: 2024PGCSIS08
# Assignment No: 02
# Implementation of Classical Substitution Ciphers 
# a) Additive (Ceasar) Cipher
# b) Multiplicative Cipher
# c) Affine Cipher
# d) Playfair Cipher 
# e) Hill Cipher

# Affine Cipher
def encryption(plaintext, keyA, keyB) :
    ciphertext = ""
    for x in plaintext:
        if(x == " "):
            cipherChar = " "
        else :
            cipherChar = chr((((ord(x) - 97) * keyA + keyB) % 26)+65)

        ciphertext += cipherChar

    return ciphertext

def decryption(ciphertext, keyA, keyB) :
    plaintext = ""
    for x in ciphertext:
        if(x == " "):
            plainChar = " "
        else:
            plainChar = chr((((ord(x) - 65 - keyB) * keyA) % 26)+97)
        plaintext += plainChar

    return plaintext

def main():
    keyA = 17
    keyAInv = 23
    keyB = 20
    sampletext = "hello world"

    cipher = encryption(sampletext, keyA, keyB)
    print("Cipher Text is: ")
    print(cipher)

    plain = decryption(cipher, keyAInv, keyB)
    print("Deciphered Text is: ")
    print(plain)

if __name__ == "__main__":
    main()