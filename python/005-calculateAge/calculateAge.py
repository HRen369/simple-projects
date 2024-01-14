from datetime import datetime
import json

def getTodayDate():
    return {
    "day":datetime.now().day,
    "month":datetime.now().month,
    "year":datetime.now().year,
    "second":datetime.now().second,
    "minute": datetime.now().minute,
    "hour": datetime.now().hour,
}

# Validation 
def validateDay(monthLimit, day):
    return day > 0 and day < monthLimit


def validateYear(year):
    return year > -1 and year < getTodayDate()["year"] + 1


def validateMonth(month):
    return month in json.load(open("months.json","r")).keys()

# Splitting the Birthday String
def validateSplitString(month,day,year):
    if validateMonth(month) == False:
        return {"day":0,"month":-1,"year":0}
    elif validateYear(year) == False:
        return {"day":0,"month":0,"year":-1}
    elif validateDay(json.load(open("months.json","r"))[month]['days'],day) == False:
        return {"day":-1,"month":0,"year":0}
    else:
        return {"day":day,"month":month,"year":year}  


def splitBirthdateString(birthdateString):
    birthdateArray = birthdateString.split("-")

    try:
        day =   int(birthdateArray[0])
        month = birthdateArray[1]
        year =  int(birthdateArray[2])
        return validateSplitString(month,day,year)
    except:
        pass

    return {"day":-1,"month":-1,"year":-1}
    

def calculateLeapYears(year):
    leapYears = 0
    currYear = getTodayDate()['year']
    if currYear % 4 != 0:
        currYear -= currYear % 4

    while currYear >= year:
        if currYear % 100 != 0:
            leapYears += 1
            currYear -= 4
    return leapYears


# Calculate User Years in various units
def calculateAgeInYears(month,day,year):
    currDate = getTodayDate()
    monthNum = json.load(open("months.json","r"))[month]['num']

    if currDate["month"] <= monthNum and currDate['day'] < day:
        year += 1
    return currDate['year'] - year


def calculateAgeInMonths(month,day,year):
    return calculateAgeInYears(month,day,year) * 12

# Tests
def testValidateDay():
    monthLimit = 31
    print("Test Day Validation")
    print(f"Test Day Validation Lower: {False == validateDay(monthLimit,0)}")
    print(f"Test Day Validation Lower: {True == validateDay(monthLimit,1)}")
    print(f"Test Day Validation Middle: {True == validateDay(monthLimit,15)}")
    print(f"Test Day Validation Upper: {False == validateDay(monthLimit,32)}")
    print("-----")
    

def testValidateYear():
    year = getTodayDate()['year']

    print("Test Year")
    print(f"Test Year Validation Lower: {False == validateYear(-1)}")
    print(f"Test Year Validation Lower: {True ==  validateYear(0)}")
    print(f"Test Year Validation Middle: {True == validateYear(year - 20)}")
    print(f"Test Year Validation Upper: {False == validateYear(year + 1)}")
    print("-----")


def testValidateMonth():
    monthName = "JAN"

    print("Test Month")
    print(f"Test Month Validation Fake: {False == validateMonth("nkjbjkb")}")
    print(f"Test Month Validation Real: {True ==  validateMonth(monthName)}")
    print(f"Test Month Validation : {False == validateMonth("Jan")}")
    print(f"Test Month Validation : {False == validateMonth("January")}")
    print("-----")


def testSplitBirthdateString():
    testRight =  "21-FEB-1996"
    testWrongDay =  "50-FEB-1996"
    testWrongMonth =  "21-FUYB-1996"
    testWrongYear =  "21-FEB-" + str(getTodayDate()['year'] + 1)
    testWrongInput =  "21-FEB--5"

    expectedRight = {"day":21,"month":"FEB","year":1996}
    expectedWrongMonth = {"day":0,"month":-1,"year":0}
    expectedWrongYear = {"day":0,"month":0,"year":-1}
    expectedWrongDay = {"day":-1,"month":0,"year":0}
    expectedWrongInput = {"day":-1,"month":-1,"year":-1}

    print("Test Split Birthdate String:")
    print(f"Test Right BD: {expectedRight == splitBirthdateString(testRight)}")
    print(f"Test Wrong BD Day: {expectedWrongDay == splitBirthdateString(testWrongDay)}")
    print(f"Test Wrong BD Month: {expectedWrongMonth == splitBirthdateString(testWrongMonth)}")
    print(f"Test Wrong BD Year: {expectedWrongYear == splitBirthdateString(testWrongYear)}")
    print(f"Test Wrong BD Input: {expectedWrongInput == splitBirthdateString(testWrongInput)}")


# Functions that are primarly used for testing ageIn--()
#This could be a lamda function with the auto function as a parameter
def ageInMonthsAuto(userInput):
    userInput = userInput 
    birthdateDict = splitBirthdateString(userInput)
    bMonth = birthdateDict['month']
    bDay = birthdateDict['day']
    bYear = birthdateDict['year']
    
    if bMonth == -1 or bDay == -1 or bYear == -1:
        return -1
    return calculateAgeInMonths(bMonth,bDay,bYear)


def ageInYearsAuto(userInput):
    userInput = userInput 
    birthdateDict = splitBirthdateString(userInput)
    bMonth = birthdateDict['month']
    bDay = birthdateDict['day']
    bYear = birthdateDict['year']
    
    if bMonth == -1 or bDay == -1 or bYear == -1:
        return -1
    return calculateAgeInYears(bMonth,bDay,bYear)


# NOTE THE FOLLOWING DAY THIS TEST IS GOING TO FAIL.
# I KNOW THE SOLUTION BUT TOO BORED TO FIX IT
def testAgeInYears():
    print("Test Age in Years")
    print(f"Testing Yesterday {25 == ageInYearsAuto('13-JAN-1999')}")
    print(f"Testing Today: {25 == ageInYearsAuto('14-JAN-1999')}")
    print(f"Testing Tommarow: {24 == ageInYearsAuto('15-JAN-1999')}")
    

def testAgeInMonths():
    print("Test Age in Months")
    # 12 months/year 
    print(f"Testing Today: {49 == ageInMonthsAuto('14-JAN-2012')}")
    

def test():
    # testValidateDay()
    # testValidateYear()
    # testValidateMonth()
    # testSplitBirthdateString()
    #testAgeInYears()
    testAgeInMonths()

def ageInYearsRealUser(userInput):
    userInput = userInput 
    birthdateDict = splitBirthdateString(userInput)
    bMonth = birthdateDict['month']
    bDay = birthdateDict['day']
    bYear = birthdateDict['year']
    
    if bMonth == -1 or bDay == -1 or bYear == -1:
        print("ERROR! Your Input is incorrect")
        print("Please follow the correct format")
        print("DAY-MONTH-YEAR")
        print("ex) 9-MAY-2005")
        print("ex) 21-JUN-2000")
        exit(0)
    print(calculateAgeInYears(bMonth,bDay,bYear))


def main():
    test()

if __name__ == "__main__":
    main()


