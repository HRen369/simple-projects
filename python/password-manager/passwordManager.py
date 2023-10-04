import os, json

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

from argon2 import PasswordHasher
from dotenv import load_dotenv

clear = lambda : os.system('cls') if os.name == "nt" else os.system('clear')
load_dotenv()

def readEncryptedMasterFile():
    MASTER_FILE = os.environ("MASTER_FILE")
    if os.path.isfile(MASTER_FILE):
        with open(MASTER_FILE,"r") as file:
            return file.read()
    return ""

def decryptMasterFile(encryptedMasterFile):
    if encryptedMasterFile == "":
        return []
    else:
        key = os.environ.get('KEY')
        iv = os.environ.get("IV")

        keyBytes = bytes.fromhex(key)
        ivBytes = bytes.fromhex(iv)

        cipher = AES.new(keyBytes, AES.MODE_CBC, ivBytes)
        decryptedMasterFile = cipher.decrypt(bytes.fromhex(encryptedMasterFile))
        unpaddedDMF = decryptedMasterFile[:-decryptedMasterFile[-1]]
        
        json_string = unpaddedDMF.decode('utf-8')

        return json.loads(json_string)

def encryptMasterFile(decryptedMasterFile):
    key = os.environ.get('KEY')
    iv = os.environ.get("IV")

    keyBytes = bytes.fromhex(key)
    ivBytes = bytes.fromhex(iv)

    jsonString = json.dumps(decryptedMasterFile)
    bytesDMF = jsonString.encode('utf-8')

    cipher = AES.new(keyBytes, AES.MODE_CBC, ivBytes)

    blockSize = 32
    padded_bytesDMF = bytesDMF + bytes([blockSize - len(bytesDMF) % blockSize] * (blockSize - len(bytesDMF) % blockSize))
    return cipher.encrypt(padded_bytesDMF)

def writeEncryptedMasterFile(encryptedMasterFile):
    MASTER_FILE = os.environ("MASTER_FILE")
    with open(MASTER_FILE, "w") as file:
        file.write(str(encryptedMasterFile.hex()))

def viewAccount():
    pass


# Adding Accounts functionality
def addAccountDetailsScreen():
    clear()
    print("__________________________")
    print("*|Add Account")
    print("*|-----------------------")
    print("*|[Q] Quit")
    print("__________________________")

def addAccountDetails():
    addAccountDetailsScreen()
    print("*|Website Name: ")
    websiteName = input("> ")
    
    addAccountDetailsScreen()
    print("*|Username: ")
    username = input("> ")
    
    addAccountDetailsScreen()
    print("*|Password: ")
    password = input("> ")

    return {
        "websiteName":websiteName,
        "username":username, 
        "password":password,
    }

def addAccount():
    account = {
        "websiteName":"github",
        "username":"Afv58", 
        "password":"samplePassword",
    }

    encryptedMasterFile = readEncryptedMasterFile()
    decryptedMasterFile = decryptMasterFile(encryptedMasterFile)
    decryptedMasterFile.append(account)
    print(decryptedMasterFile)
    
    encryptedMasterFile = encryptMasterFile(decryptedMasterFile)
    print(encryptedMasterFile)

    writeEncryptedMasterFile(encryptedMasterFile)
    
    input("> ")
    # # Need function that encryots and decrypts string

def deleteAccount():
    pass

def mainMenuScreen():
    clear()
    print("__________________________")
    print("*|Python Password Manager")
    print("*|-----------------------")
    print("*|[1] View Accounts")
    print("*|[2] Add Account")
    print("*|[3] Delete Account")
    print("*|-----")
    print("*|[Q] Quit")
    print("__________________________")

def mainMenu():
    
    running = True
    while running:
        mainMenuScreen()
        ans = input("> ")
        
        if ans == 1:
            viewAccount()
        elif ans == "2":
            addAccount()
        elif ans == 3:
            deleteAccount()
        elif ans == "q" or ans == "Q":
            running = False

def main():
    mainMenu()



if __name__ == "__main__":
    main()