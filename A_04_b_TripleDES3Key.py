# Author: Devashish Roy, Roll No: 2024PGCSIS08
# Assignment No: 04
# Implementation of Standard Symmetric Block Ciphers 
# a) Data Encryption Standard (DES)
# b) Triple DES
# c) Advance Encryption Standard (AES)

# Triple DES with 3 Keys
import A_04_a_DES as DES

def tripleDESEncryption(plaintext, key1, key2, key3):
    return DES.desEncryption(DES.desDecryption(DES.desEncryption(plaintext, key1), key2), key3)

def tripleDESDecryption(ciphertext, key1, key2, key3):
    return DES.desDecryption(DES.desEncryption(DES.desDecryption(ciphertext, key3), key2), key1)

if __name__ == "__main__":
    plaintext = "ABCD132536654321"
    plaintext = DES.hexToBin(plaintext)

    key1 = "4133957999BDCCF9"
    key1 = DES.hexToBin(key1)

    key2 = "4133957999BDCCF2"
    key2 = DES.hexToBin(key2)

    key3 = "4133957999BDCCF1"
    key3 = DES.hexToBin(key3)

    print("Plaintext:", DES.binToHex(plaintext), "\nKey1:", DES.binToHex(key1), "\nKey2:", DES.binToHex(key2), "\nKey3:", DES.binToHex(key3))
    print()

    ciphertext = tripleDESEncryption(plaintext, key1, key2, key3)

    print("Encryption:")
    print("Ciphertext:", DES.binToHex(ciphertext))
    print()
    print("Decryption: ")
    print("Plaintext:", DES.binToHex(tripleDESDecryption(ciphertext, key1, key2, key3)), "\n")
