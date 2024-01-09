import json,random

NAME_FILE = 'names.json'


# Getting Name Lists
def maleFirstNames():
    nameFile = open(NAME_FILE)
    nameList = json.load(nameFile)
    return nameList['names']['usTopMaleFirstNames']

def femaleFirstNames():
    nameFile = open(NAME_FILE)
    nameList = json.load(nameFile)
    return nameList['names']['usTopFemaleFirstNames']

def lastNames():
    nameFile = open(NAME_FILE)
    nameList = json.load(nameFile)
    return nameList['names']['usTopLastNames']


# Getting Random Name from Lists
def getRandomFirstName():
    return random.choice(femaleFirstNames() + maleFirstNames())

def getRandomFirstMaleName():
    return random.choice(maleFirstNames())

def getRandomFirstFemaleName():
    return random.choice(femaleFirstNames())

def getRandomLastName():
    return random.choice(lastNames())


## Testing Generators

def testMaleFirstName():
    mFirstNameList = maleFirstNames()
    randomName = getRandomFirstMaleName()

    if randomName in mFirstNameList:
        return True
    return False

def testFemaleFirstName():
    fFirstNameList = femaleFirstNames()
    randomName = getRandomFirstFemaleName()

    if randomName in fFirstNameList:
        return True
    return False

def testLastName():
    lastNameList = lastNames()
    randomName = getRandomLastName()

    if randomName in lastNameList:
        return True
    return False

def test():
    print("Name Generator")
    print(f"Test Male First Name: {testMaleFirstName()}")
    print(f"Test Female First Name: {testFemaleFirstName()}")
    print(f"Test Last Names: {testLastName()}")


# Full Name Generators

def getFullRandomMaleName():
    return f"{getFullRandomMaleName()} {getRandomLastName()}"


def getFullRandomFemaleName():
    return f"{getFullRandomFemaleName()} {getRandomLastName()}"


def getFullRandomName():
    return f"{getRandomFirstName()} {getRandomLastName()}"

def main():
    test()
    #print(getFullRandomName())
    #print(getFullRandomFemaleName())
    #print(getFullRandomMaleName())

if __name__ == "__main__":
    main()
