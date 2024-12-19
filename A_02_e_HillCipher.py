# Author: Devashish Roy, Roll No: 2024PGCSIS08
# Assignment No: 02
# Implementation of Classical Substitution Ciphers 
# a) Additive (Ceasar) Cipher
# b) Multiplicative Cipher
# c) Affine Cipher
# d) Playfair Cipher 
# e) Hill Cipher

# Hill Cipher
def generateKeyMatrix(key, size):
    keyMatrix = [[0] * size for i in range(size)]
    k = 0
    for i in range(size):
        for j in range(size):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
    
    return keyMatrix

def generatePlaintextMatrix(plaintext, size):
    plaintextMatrix = [[0] * size for i in range(1)]
    for i in range(size):
        plaintextMatrix[0][i] = ord(plaintext[i]) % 97

    return plaintextMatrix

def generateCiphertextMatrix(ciphertext, size):
    ciphertextMatrix = [[0] * size for i in range(1)]
    for i in range(size):
        ciphertextMatrix[0][i] = ord(ciphertext[i]) % 65

    return ciphertextMatrix

def matrixMultiplication(textMatrix, keyMatrix, size):
    resultMatrix = [[0] * size for i in range(1)]
    for idxCol in range(size):
        for idxRow in range(size):
            resultMatrix[0][idxCol] += keyMatrix[idxRow][idxCol] * textMatrix[0][idxRow]
        resultMatrix[0][idxCol] %= 26

    return resultMatrix

def encryption(plaintext, key):
    size = len(plaintext)
    ciphertext = ""

    keyMatrix = generateKeyMatrix(key, size)
    plaintextMatrix = generatePlaintextMatrix(plaintext, size)
    ciphertextMatrix = matrixMultiplication(plaintextMatrix, keyMatrix, size)

    for i in range(size):
        ciphertext += chr(ciphertextMatrix[0][i] + 65)

    return ciphertext

def keyInverse(key) :
    inverseMatrix = [[8, 5, 10], [21, 8, 21], [21, 12, 8]]
    return inverseMatrix

def decryption(ciphertext, key):
    size = len(ciphertext)
    keyMatrix = keyInverse(key)
    ciphertextMatrix = generateCiphertextMatrix(ciphertext, size)
    plaintextMatrix = matrixMultiplication(ciphertextMatrix, keyMatrix, size)

    plaintext = ""
    for i in range(size):
        plaintext += chr(plaintextMatrix[0][i] + 97)

    return plaintext

def main():
    plaintext = "boy"
    key = "GYBNQKURP"

    ciphertext = encryption(plaintext, key)
    print(ciphertext)

    plaintext = decryption(ciphertext, key)
    print(plaintext)

if __name__ == "__main__" :
    main()
