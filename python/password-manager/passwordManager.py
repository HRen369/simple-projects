import os, json

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

from argon2 import PasswordHasher
from dotenv import load_dotenv

clear = lambda : os.system('cls') if os.name == "nt" else os.system('clear')
load_dotenv()

def readEncryptedMasterFile():
    MASTER_FILE_NAME = os.environ.get("MASTER_FILE_NAME")
    if os.path.isfile(MASTER_FILE_NAME):
        with open(MASTER_FILE_NAME,"r") as file:
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
    MASTER_FILE_NAME = os.environ.get("MASTER_FILE_NAME")
    with open(MASTER_FILE_NAME, "w") as file:
        file.write(str(encryptedMasterFile.hex()))

# Viewing Accounts Functionality

def choosingAccountIndex(accounts):
    haveChoice = False
    while haveChoice == False:
        ans = input(">")
        try:
            intAns = int(ans) - 1
            if intAns < 0 or intAns > len(accounts)-1:
                print("-- Invalid Input --")
            else:   
                return intAns
        except ValueError:
            if ans == "q" or ans == "Q":
                return -1
            else:
                print("-- Invalid input --")

def viewAccount():

    encryptedMasterFile = readEncryptedMasterFile()
    decryptedMasterFileAccounts = decryptMasterFile(encryptedMasterFile)

    clear()
    print("__________________________")
    print("*|View Accounts")
    print("*|-----------------------")    
    print("*|[Q] Quit")
    print("__________________________")

    if len(decryptedMasterFileAccounts) == 0:
        print("No Accounts to View")
        print("__________________________")
        input("Press Enter to continue >")
    else:
        for i in range(len(decryptedMasterFileAccounts)):
            websiteName = decryptedMasterFileAccounts[i]["websiteName"]
            print(f"*|   [{i+1}] {websiteName}")

        print("__________________________")
        accountIndex = choosingAccountIndex(decryptedMasterFileAccounts)

        if accountIndex == -1:
            return

        pickedAccount = decryptedMasterFileAccounts[accountIndex]

        clear()
        print("__________________________")
        print("*|Viewing Account")
        print("*|-----------------------")    
        print(f"*|   Website Name: {pickedAccount['websiteName']}")
        print(f"*|   Username: {pickedAccount['username']}")
        print(f"*|   Password: {pickedAccount['password']}")
        print("__________________________")
        input("Press Enter to continue >")        



# Adding Accounts Functionality
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
    account =  addAccountDetails() #{ "websiteName":"github", "username":"Afv58", "password":"samplePassword"}

    encryptedMasterFile = readEncryptedMasterFile()
    decryptedMasterFile = decryptMasterFile(encryptedMasterFile)
    decryptedMasterFile.append(account)
    
    encryptedMasterFile = encryptMasterFile(decryptedMasterFile)
    writeEncryptedMasterFile(encryptedMasterFile)
    
    print("__________________________")
    input("Press Enter to continue >")   

# Deleting Accounts Functionality
def deleteAccount():
    encryptedMasterFile = readEncryptedMasterFile()
    decryptedMasterFileAccounts = decryptMasterFile(encryptedMasterFile)

    clear()
    print("__________________________")
    print("*|Deleting Accounts")
    print("*|-----------------------")    
    print("*|[Q] Quit")
    print("__________________________")

    if len(decryptedMasterFileAccounts) == 0:
        print("No Accounts to Delete")
        print("__________________________")
        input("Press Enter to continue >")
    else:
        for i in range(len(decryptedMasterFileAccounts)):
            websiteName = decryptedMasterFileAccounts[i]["websiteName"]
            print(f"*|   [{i+1}] {websiteName}")

        print("__________________________")
        
        accountIndex = choosingAccountIndex(decryptedMasterFileAccounts)
        if accountIndex == -1:
            return

        pickedAccount = decryptedMasterFileAccounts[accountIndex]

        clear()
        print("__________________________")
        print("*|Deleting Account")
        print("*|-----------------------")    
        print(f"*|   Website Name: {pickedAccount['websiteName']}")
        print(f"*|   Username: {pickedAccount['username']}")
        print(f"*|   Password: {pickedAccount['password']}")
        print("__________________________")

        ans = input("Are you sure you want to delete (Y) > ")


        if ans == "y" or ans == "Y":
            decryptedMasterFileAccounts.pop(accountIndex)

            encryptedMasterFile = encryptMasterFile(decryptedMasterFileAccounts)
            writeEncryptedMasterFile(encryptedMasterFile)

            print("__________________________")
            print("Account Successfully deleted!")
            print("__________________________")
            input("Press Enter to continue >")      
        else:
            print("__________________________")
            print("Account NOT deleted!")
            print("__________________________")
            input("Press Enter to continue >")     


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
        
        if ans == "1":
            viewAccount()
        elif ans == "2":
            addAccount()
        elif ans == "3":
            deleteAccount()
        elif ans == "q" or ans == "Q":
            running = False

def main():
    mainMenu()

if __name__ == "__main__":
    main()