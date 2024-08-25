import json, random

# File JSON constants
NAME_FILE = 'names.json'
US_MALE_FIRST_NAMES = 'usTopMaleFirstNames'
US_FEMALE_FIRST_NAMES = 'usTopFemaleFirstNames'
US_LAST_NAMES = 'usTopLastNames'


def openNameFile(name_type):
    name_file = open(NAME_FILE)
    name_list = json.load(name_file)
    return name_list['names'][name_type]


# Getters for Name Lists
def maleFirstNames():
    return openNameFile(US_MALE_FIRST_NAMES)


def femaleFirstNames():
    return openNameFile(US_FEMALE_FIRST_NAMES)


def lastNames():
    return openNameFile(US_LAST_NAMES)


# Getting Random Name from Lists
def randomFirstMaleName():
    return random.choice(maleFirstNames())

def randomFirstFemaleName():
    return random.choice(femaleFirstNames())

def randomLastName():
    return random.choice(lastNames())

# Get Random Full Name
def fullMaleName():
    return f"{randomFirstMaleName()} {randomLastName()}"

def fullFemaleName():
    return f"{randomFirstFemaleName()} {randomLastName()}"

def fullRandomName():
    firstNames = femaleFirstNames()
    firstNames.append(maleFirstNames())
    random.shuffle(firstNames)

    return f"{random.choice(firstNames)} {randomLastName()}" 


# TESTS
def testMaleName():
    return randomFirstMaleName() in maleFirstNames()


def testFemaleName():
    return randomFirstFemaleName() in femaleFirstNames()


def testLastName():
    return randomLastName() in lastNames()


def testMaleFullName():
    fullName = fullMaleName().split(' ')
    return fullName[0] in maleFirstNames() and fullName[1] in lastNames()

def testFemaleFullName():
    fullName = fullFemaleName().split(' ')
    return fullName[0] in femaleFirstNames() and fullName[1] in lastNames()

def testRandomFullName():
    fullName = fullRandomName().split(' ')
    return (fullName[0] in femaleFirstNames() or fullName[0] in maleFirstNames()) and fullName[1] in lastNames()


def test():
    print("--- Testing Name Generator ---")
    print(f"Male First Name Test: {testMaleName()}")
    print(f"Female First Name Test:{testFemaleName()}")
    print(f"Last Name Test: {testLastName()}")
    print(f"Full Male Name: {testMaleFullName()}")
    print(f"Full Female Name: {testFemaleName()}")
    print(f"Full Random Name: {testRandomFullName()}")


def main():
    test()

if __name__ == "__main__":
    main()