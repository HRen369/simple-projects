import json, random

def getRandomFish():
    file = open("items.json")
    data = json.load(file)
    
    return random.choice(data)


def main():
    print(getRandomFish())



if __name__ == '__main__':
    main()