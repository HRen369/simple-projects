from argon2 import PasswordHasher


def mainMenu():
    print("__________________________")
    print("*|Python Password Manager")
    print("*|-----------------------")
    print("*|[1] View Accounts")
    print("*|[2] Add Account")
    print("*|[3] Delete Account")
    print("*|-----")
    print("*|[Q] Quit")
    print("__________________________")


    running = True
    while running:
        ans = input("> ")
        
        if ans == 1:
            viewAccount()
        elif ans == 2:
            addAccount()
        elif ans == 3:
            deleteAccount()
        elif ans == "q" or ans == "Q":
            running = False

def main():
    mainMenu()
    ph = PasswordHasher()
    hash = ph.hash("myPassword")
    print(hash)


if __name__ == "__main__":
    main()