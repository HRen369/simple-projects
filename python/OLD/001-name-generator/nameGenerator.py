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


# Full Name Generators
def getRandomFullMaleName():
    return f"{getRandomFirstMaleName()} {getRandomLastName()}"


def getRandomFullFemaleName():
    return f"{getRandomFirstFemaleName()} {getRandomLastName()}"


def getRandomFullName():
    return f"{getRandomFirstName()} {getRandomLastName()}"


## Testing Name Lists and Random Generators
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

def testRandomLastName():
    lastNameList = lastNames()
    randomName = getRandomLastName()

    if randomName in lastNameList:
        return True
    return False

def testRandomMaleFullName():
    fullName = getRandomFullMaleName().split()
    firstName = fullName[0]
    lastName = fullName[1]

    mFirstNameList = maleFirstNames()
    lastNameList = lastNames()

    if firstName in mFirstNameList and lastName in lastNameList:
        return True
    return False

def testRandomFemaleFullName():
    fullName = getRandomFullFemaleName().split()
    firstName = fullName[0]
    lastName = fullName[1]

    fFirstNameList = femaleFirstNames()
    lastNameList = lastNames()

    if  firstName in fFirstNameList and lastName in lastNameList:
        return True
    return False

def testRandomFullName():
    fullName = getRandomFullName().split()
    firstName = fullName[0]
    lastName = fullName[1]

    firstNameList = maleFirstNames() + femaleFirstNames()
    lastNameList = lastNames()

    if  firstName in firstNameList and lastName in lastNameList:
        return True
    return False


def test():
    print("Name Generator")
    print(f"Test Male First Name: {testMaleFirstName()}")
    print(f"Test Female First Name: {testFemaleFirstName()}")
    print(f"Test Last Names: {testRandomLastName()}")
    print(f"Test Male Full Name: {testRandomMaleFullName()}")
    print(f"Test Female Full Name: {testRandomFemaleFullName()}")
    print(f"Test Random Full Name: {testRandomFullName()}")


def main():
    test()
    #print(getFullRandomName())
    #print(getFullRandomFemaleName())
    #print(getFullRandomMaleName())

if __name__ == "__main__":
    main()
