# Author: Devashish Roy, Roll No: 2024PGCSIS08
# Assignment No: 02
# Implementation of Classical Substitution Ciphers 
# a) Additive (Ceasar) Cipher
# b) Multiplicative Cipher
# c) Affine Cipher
# d) Playfair Cipher 
# e) Hill Cipher

# Additive (Ceasar) Cipher
def encryption(plaintext, key) :
    ciphertext = ""
    for x in plaintext:
        if(x == " "):
            cipherChar = " "
        else :
            cipherChar = chr(((ord(x) - 97 + key) % 26)+65)

        ciphertext += cipherChar

    return ciphertext

def decryption(ciphertext, key) :
    plaintext = ""
    for x in ciphertext:
        if(x == " "):
            plainChar = " "
        else:
            plainChar = chr(((ord(x) - 65 - key) % 26) + 97)
        plaintext += plainChar

    return plaintext

def main():
    key = 81
    sampletext = input()

    cipher = encryption(sampletext, key)
    print("Cipher Text is: ")
    print(cipher)

    plain = decryption(cipher, key)
    print("Deciphered Text is: ")
    print(plain)

if __name__ == "__main__":
    main()