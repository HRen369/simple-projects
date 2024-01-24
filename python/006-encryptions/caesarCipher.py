ROTATE = 1


ALPHABET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", 
"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
"!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}","\\","|","'","\"",";",":","/","?",".",">",",","<","`","~","*"]


def findCharInd(char):
    if char.isupper():
        return ord(char) - 65 + 26
    elif char.islower():
        return ord(char) - 97
    elif char in SPECIAL_ALPHABET:
        return findSpecialCharInd(char)
    else:
        return -1


def findSpecialCharInd(char):
    found = False
    i = 52

    while i < len(ALPHABET) and found == False:
        if ALPHABET[i] == char:
            found = True
        i += 1

    if i == 52:
        return -1
    return i


def encrypt(string):
    encryptString = []

    for char in string:
        encryptedCharInd = (findCharInd(char) + ROTATE) % len(ALPHABET)
        encryptString.append(ALPHABET[encryptedCharInd])

    return "".join(encryptString)


def decrypt(string):
    decryptString = []

    for char in string:
        decryptedCharInd = (findCharInd(char) - ROTATE) % len(ALPHABET)
        decryptString.append(ALPHABET[decryptedCharInd])

    return "".join(decryptString)


def testEncrypt():
    arg1 = "azyx"
    result = "bAzy"

    functResult = encrypt(arg1)
    print(functResult == result)


def testDecrypt():
    arg1 = "bAzy"
    result = "azyx"

    functResult = decrypt(arg1)
    print(functResult == result)


def main():
    testEncrypt()
    testDecrypt()


if __name__ == "__main__":
    main()