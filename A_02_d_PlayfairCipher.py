# Author: Devashish Roy, Roll No: 2024PGCSIS08
# Assignment No: 02
# Implementation of Classical Substitution Ciphers 
# a) Additive (Ceasar) Cipher
# b) Multiplicative Cipher
# c) Affine Cipher
# d) Playfair Cipher 
# e) Hill Cipher

# Playfair Cipher
def generateKeySquare(key):
    size = 5
    keySquare = [[0] * size for i in range(size)]

    alphaSet = set(())

    row = 0
    col = 0

    for alpha in key:
        if(alpha not in alphaSet):
            if(alpha == 'J'):
                continue

            alphaSet.add(alpha)
            # Add to the matrix
            if(col >= size):
                row += 1
                col = 0
            
            keySquare[row][col] = alpha
            col += 1

    for i in range(65, 91):
        if(chr(i) not in alphaSet):
            if(i == 74):
                continue

            alphaSet.add(chr(i))

            if(col >= size):
                row += 1
                col = 0
            
            keySquare[row][col] = chr(i)
            col += 1

    return keySquare

def generateDigraph(sampletext):
    digraphArray = []
    i = 0
    while i < len(sampletext):
        if(i+1 >= len(sampletext)):
            digraphArray.append([sampletext[i], 'z'])
            i += 1
        elif(sampletext[i] == sampletext[i+1]):
            digraphArray.append([sampletext[i], 'x'])
            i += 1
        else:
            digraphArray.append([sampletext[i], sampletext[i+1]])
            i += 2
    return digraphArray

def search(keySquare, element):
    for i in range(5):
        for j in range(5):
            if(keySquare[i][j] == element.upper()):
                return i, j

def encryptionMethod(digraph, keySquare):
    row_1, col_1 = search(keySquare, digraph[0])
    row_2, col_2 = search(keySquare, digraph[1])

    if(col_1 == col_2):
        row_1 += 1
        row_2 += 1

        if(row_1 == 5):
            row_1 = 0
        
        if(row_2 == 5):
            row_2 = 0
    elif(row_1 == row_2):
        col_1 += 1
        col_2 += 1
        
        if(col_1 == 5):
            col_1 = 0

        if(col_2 == 5):
            col_2 = 0
    else:
        temp = col_1 
        col_1 = col_2
        col_2 = temp
    
    return keySquare[row_1][col_1], keySquare[row_2][col_2]

def decryptionMethod(digraph, keySquare):
    row_1, col_1 = search(keySquare, digraph[0])
    row_2, col_2 = search(keySquare, digraph[1])

    if(col_1 == col_2):
        row_1 -= 1
        row_2 -= 1

        if(row_1 == -1):
            row_1 = 4
        
        if(row_2 == -1):
            row_2 = 4
    elif(row_1 == row_2):
        col_1 -= 1
        col_2 -= 1
        
        if(col_1 == -1):
            col_1 = 4

        if(col_2 == -1):
            col_2 = 4
    else:
        temp = col_1 
        col_1 = col_2
        col_2 = temp
    
    return keySquare[row_1][col_1], keySquare[row_2][col_2]

# def encryption(plaintext, key):
#     ciphertext = ""
#     keySquare = generateKeySquare(key)
#     digraphArray = generateDigraph(plaintext)

#     for eachDigraph in digraphArray:
#         x, y = encryptionMethod(eachDigraph, keySquare)
#         ciphertext = ciphertext + x + y

#     return ciphertext

# def decryption(ciphertext, key):
#     plaintext = ""
#     keySquare = generateKeySquare(key)
#     digraphArray = generateDigraph(ciphertext)

#     for eachDigraph in digraphArray:
#         x, y = decryptionMethod(eachDigraph, keySquare)
#         plaintext = plaintext + x + y

#     return plaintext.lower()

def encryptNdecrypt(inputtext, key, method):
    outputtext = ""
    keySquare = generateKeySquare(key)
    digraphArray = generateDigraph(inputtext)

    for eachDigraph in digraphArray:
        if(method == "encryption"):
            x, y = encryptionMethod(eachDigraph, keySquare)
        elif(method == "decryption"):
            x, y = decryptionMethod(eachDigraph, keySquare)
        
        outputtext = outputtext + x + y

    if(method == "encryption"):
        return outputtext.upper()
    elif(method == "decryption"):
        return outputtext.lower()

def main():
    sampletext = "instruments"
    key = "MONARCHY"
    
    ciphertext = encryptNdecrypt(sampletext, key, "encryption")
    print(ciphertext)
    
    plaintext = encryptNdecrypt(ciphertext, key, "decryption")
    print(plaintext)

if __name__ == "__main__":
    main()