import random


def flipCoin():
    if int(random.random() * 100) + 1 > 50:
        return True
    return False


def printResults(heads, tails):
    print("HEADS:",heads)
    print("TAILS:",tails)
    
    if heads > tails:
        print("More heads")
    elif heads < tails:
        print("More tails")
    else:
        print("Draw")


def playGame(games):
    heads = 0
    tails = 0
    for i in range(games):
        if flipCoin():
            heads += 1
        else:
            tails += 1

    printResults(heads,tails)


def main():
    game()

    
if __name__ == "__main__":
    main()