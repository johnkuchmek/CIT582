
def encrypt(key,plaintext):
    ciphertext=""
    #YOUR CODE HERE
    #Define Alphabet
    upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in plaintext:
        if letter in upperCase:
            letterPosition = upperCase.index(letter)
            cipherPosition = (letterPosition + key + ceil(key/26) * 26) % 26
            cipherLetter = upperCase[cipherPosition]
            ciphertext.append(cipherLetter)
        elif letter in lowerCase:
            letterPosition = lowerCase.index(letter)
            cipherPosition = (letterPosition + key + ceil(key/26) * 26) % 26
            cipherLetter = lowerCase[cipherPosition]
            ciphertext.append(cipherLetter)
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    #YOUR CODE HERE
    #Define Alphabet
    upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in ciphertext:
        if letter in upperCase:
            letterPosition = upperCase.index(letter)
            cipherPosition = (letterPosition - key + ceil(key/26) * 26) % 26
            plainLetter = upperCase[cipherPosition]
            plaintext.append(plainLetter)
        elif letter in lowerCase:
            letterPosition = lowerCase.index(letter)
            cipherPosition = (letterPosition - key + ceil(key/26) * 26) % 26
            plainLetter = lowerCase[cipherPosition]
            plaintext.append(plainLetter)
    return plaintext


