ROTATE = 6

LOWER_ALPHABET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
UPPER_ALPHABET = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
SPECIAL_ALPHABET = ["!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}","\\","|","'","\"",";",":","/","?",".",">",",","<","`","~","*"]
TOTAL_ALPHA_LEN = 26 + len(SPECIAL_ALPHABET) 

def findSpecialCharInd(char):
    found = False
    i = -1

    while i < len(SPECIAL_ALPHABET) and found == False:
        if SPECIAL_ALPHABET[i] == char:
            found = True
        i += 1

    return i

def rotateForward(char):
    if char.isupper():
        num = ord(char) - 65
    elif char.islower():
        num = ord(char) - 97
    elif char in SPECIAL_ALPHABET:
        pass
    else:
        return -1
    
    return (num + ROTATE) % 26 

def rotateBackward(char):
    return

def encrypt(string):
    pass

def decrypt(string):
    pass

def testEncrypt():
    pass

def testDecrypt():
    pass

def main():
    print(ord("a"))

if __name__ == "__main__":
    main()