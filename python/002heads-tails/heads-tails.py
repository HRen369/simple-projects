import random

GAMES = 5

def printResults(heads, tails):
    print("HEADS:",heads)
    print("TAILS:",tails)
    
    if heads > tails:
        print("Heads Win!")
    elif heads < tails:
        print("Tails Win!")
    else:
        print("Draw!")


def playGames(gameTotals):
    heads = 0
    tails = 0

    for i in range(gameTotals):
        if random.uniform(0,1) > 0.5:
            heads += 1
        else: 
            tails += 1
    
    printResults(heads,tails)


if __name__ == "__main__":
    playGames(GAMES)