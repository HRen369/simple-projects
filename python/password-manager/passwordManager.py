import os, json

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

from argon2 import PasswordHasher, exceptions
from dotenv import load_dotenv

clear = lambda : os.system('cls') if os.name == "nt" else os.system('clear')
load_dotenv()

def validate():
    MASTER_PASSWORD = os.environ.get("MASTER_PASSWORD")
    clear()
    print("__________________________")
    print("*|Validate user")
    print("__________________________")
    print("Enter the master password >")
    ans = input("> ")

    ph = PasswordHasher()
    hash = ph.hash(ans)

    try:
        if ph.verify(hash,MASTER_PASSWORD) == True:
            clear()
            print("__________________________")
            print("*|Validate user")
            print("__________________________")
            print("Validation Successful")
            print("__________________________")
            input("Press Enter to continue >")
            return True
    except exceptions.VerifyMismatchError:        
        clear()
        print("__________________________")
        print("*|Validate user")
        print("__________________________")
        print("Validation Failed")
        print("__________________________")
        input("Press Enter to continue >")

        return False

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

# Viewing Accounts Functionality
def viewAccount():
    if validate() == False:
        return

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
    if validate() == False:
        return

    account =  addAccountDetails() #{ "websiteName":"github", "username":"Afv58", "password":"samplePassword"}

    clear()
    print("__________________________")
    print("*|Adding Account")
    print("*|-----------------------")    
    print(f"*|   Website Name: {account['websiteName']}")
    print(f"*|   Username: {account['username']}")
    print(f"*|   Password: {account['password']}")
    print("__________________________")
    ans = input("Are you sure you want to add this account (Y) > ")
    print("__________________________")

    if ans == "y" or ans == "Y":    
        encryptedMasterFile = readEncryptedMasterFile()
        decryptedMasterFile = decryptMasterFile(encryptedMasterFile)
        decryptedMasterFile.append(account)

        encryptedMasterFile = encryptMasterFile(decryptedMasterFile)
        writeEncryptedMasterFile(encryptedMasterFile)

        print("Account Successfully added!")
    else:
        print("Account NOT added!") 

    print("__________________________")
    input("Press Enter to continue >")   

# Deleting Accounts Functionality
def deleteAccount():    
    if validate() == False:
        return


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
        print("__________________________")


        if ans == "y" or ans == "Y":
            decryptedMasterFileAccounts.pop(accountIndex)

            if len(decryptedMasterFileAccounts) == 0:
                MASTER_FILE_NAME = os.environ.get("MASTER_FILE_NAME")
                os.remove(MASTER_FILE_NAME)
            else:
                encryptedMasterFile = encryptMasterFile(decryptedMasterFileAccounts)
                writeEncryptedMasterFile(encryptedMasterFile)

            print("Account Successfully deleted!")
        else:
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