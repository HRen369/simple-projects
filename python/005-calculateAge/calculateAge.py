from datetime import datetime
import json,calendar


def getTodayDate():
    return {
    "day":datetime.now().day,
    "month":datetime.now().month,
    "year":datetime.now().year,
    "second":datetime.now().second,
    "minute": datetime.now().minute,
    "hour": datetime.now().hour,
}

#Helper Methods
def getMonthJson():
    return json.load(open("months.json","r"))


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
    currDate = getTodayDate()
    currYear = currDate['year']

    if currYear % 4 != 0:
        currYear -= currYear % 4
    elif currDate['month'] <= 2 and currDate['day'] < 29:
        leapYears -= 1

    while currYear >= year:
        if currYear % 100 != 0:
            leapYears += 1
            currYear -= 4
    return leapYears


def monthName(monthNum):
    if monthNum > 12:
        monthNum -= 12
    elif monthNum < 1:
        monthNum += 12
    
    return calendar.month_name[monthNum].upper()[0:3]


# Validation 
def validateDay(monthLimit, day):
    return day > 0 and day < monthLimit


def validateYear(year):
    return year > -1 and year < getTodayDate()["year"] + 1


def validateMonth(month):
    return month in getMonthJson().keys()

# Splitting the Birthday String
def validateSplitString(month,day,year):
    if validateMonth(month) == False:
        return {"day":0,"month":-1,"year":0}
    elif validateYear(year) == False:
        return {"day":0,"month":0,"year":-1}
    elif validateDay(getMonthJson()[month]['days'],day) == False:
        return {"day":-1,"month":0,"year":0}
    else:
        return {"day":day,"month":month,"year":year}  


# Calculate User Years in various units
def calculateAgeInYears(month,day,year):
    currDate = getTodayDate()
    monthNum = getMonthJson()[month]['num']

    if currDate["month"] <= monthNum and currDate['day'] < day:
        year += 1
    
    return currDate['year'] - year


def calculateAgeInMonths(month,day,year):
    currDate = getTodayDate()
    monthNum = getMonthJson()[month]['num']
    totalMonths = 12 - monthNum

    if day <= currDate['day']:
        totalMonths += currDate['month']
        year += 1
    return totalMonths + (calculateAgeInYears(month,day,year)*12)

def calculateAgeInDays(month,day,year):
    currDate = getTodayDate()

    if day < currDate['day']:
        pass
    elif day > currDate['day']:
        pass
    else:
        return calculateAgeInYears(month,day,year)*365 + calculateLeapYears(year)

def calculateAgeInHours(month,day,year):
    return calculateAgeInDays(month,day,year) * 24

def calculateAgeInMinutes(month,day,year):
    return calculateAgeInHours(month,day,year) * 60

def calculateAgeInSeconds(month,day,year):
    return calculateAgeInMinutes(month,day,year) * 60

def ageIn(funct, userInput):
    userInput = userInput 
    birthdateDict = splitBirthdateString(userInput)
    bMonth = birthdateDict['month']
    bDay = birthdateDict['day']
    bYear = birthdateDict['year']
    
    if bMonth == -1 or bDay == -1 or bYear == -1:
        return -1
    return funct(bMonth,bDay,bYear)


def ageInUserInput(funct,userInput):
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
    funct(bMonth,bDay,bYear)


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
    print("-----")


def testAgeInYears():
    age = 25
    today = getTodayDate()
    testYesterday = f'{today['day']}-{monthName(today['month'])}-{today['year']-age}'
    testToday = f'{today['day']-1}-{monthName(today['month'])}-{today['year']-age}'
    testTommarrow = f'{today['day']+1}-{monthName(today['month'])}-{today['year']-age}'

    expectedYesterday = age
    expectedToday = age
    expectedTommarrow = age - 1

    print("Test Age in Years")
    print(f"Testing Yesterday: {expectedYesterday == ageIn(calculateAgeInYears,testYesterday)}")
    print(f"Testing Today: {expectedToday == ageIn(calculateAgeInYears,testToday)}")
    print(f"Testing Tommarow: {expectedTommarrow == ageIn(calculateAgeInYears,testTommarrow)}")
    print("-----")


def testAgeInMonths():
    yearsDiff = 1
    today = getTodayDate()

    testYOneYearAgo = f"{today['day']-1}-{monthName(today['month'])}-{today['year']-yearsDiff}"
    testYOneMonthAgo = f"{today['day']-1}-{monthName(today['month']-1)}-{today['year']-yearsDiff}"
    testYFiveMonthAgo = f"{today['day']-1}-{monthName(today['month']-5)}-{today['year']-yearsDiff}"
    testYSevenMonthAgo = f"{today['day']-1}-{monthName(today['month']-7)}-{today['year']-yearsDiff}"
    testYTenMonthAgo = f"{today['day']-1}-{monthName(today['month']-10)}-{today['year']-yearsDiff}"

    testOneYearAgo = f"{today['day']}-{monthName(today['month'])}-{today['year']-yearsDiff}"
    testOneMonthAgo = f"{today['day']}-{monthName(today['month']-1)}-{today['year']-yearsDiff}"
    testFiveMonthAgo = f"{today['day']}-{monthName(today['month']-5)}-{today['year']-yearsDiff}"
    testSevenMonthAgo = f"{today['day']}-{monthName(today['month']-7)}-{today['year']-yearsDiff}"
    testTenMonthAgo = f"{today['day']}-{monthName(today['month']-10)}-{today['year']-yearsDiff}"

    testTOneYearAgo = f"{today['day']+1}-{monthName(today['month'])}-{today['year']-yearsDiff}"
    testTOneMonthAgo = f"{today['day']+1}-{monthName(today['month']-1)}-{today['year']-yearsDiff}"
    testTFiveMonthAgo = f"{today['day']+1}-{monthName(today['month']-5)}-{today['year']-yearsDiff}"
    testTSevenMonthAgo = f"{today['day']+1}-{monthName(today['month']-7)}-{today['year']-yearsDiff}"
    testTTenMonthAgo = f"{today['day']+1}-{monthName(today['month']-10)}-{today['year']-yearsDiff}"


    print("Testing Age In Months")
    print(f"Test Yesterday 1  Year   Ago: {12 == ageIn(calculateAgeInMonths,testYOneYearAgo)}")
    print(f"Test Yesterday 1  Months Ago: {1 == ageIn(calculateAgeInMonths,testYOneMonthAgo)}")
    print(f"Test Yesterday 5  Months Ago: {5 == ageIn(calculateAgeInMonths,testYFiveMonthAgo)}")
    print(f"Test Yesterday 7  Months Ago: {7 == ageIn(calculateAgeInMonths,testYSevenMonthAgo)}")
    print(f"Test Yesterday 10 Months Ago: {10 == ageIn(calculateAgeInMonths,testYTenMonthAgo)}")
    print("-")
    print(f"Test Today 1  Year   Ago: {12 == ageIn(calculateAgeInMonths,testOneYearAgo)}")
    print(f"Test Today 1  Months Ago: {1 == ageIn(calculateAgeInMonths,testOneMonthAgo)}")
    print(f"Test Today 5  Months Ago: {5 == ageIn(calculateAgeInMonths,testFiveMonthAgo)}")
    print(f"Test Today 7  Months Ago: {7 == ageIn(calculateAgeInMonths,testSevenMonthAgo)}")
    print(f"Test Today 10 Months Ago: {10 == ageIn(calculateAgeInMonths,testTenMonthAgo)}")
    print("-")
    print(f"Test Tomorrow 1  Year   Ago: {11 == ageIn(calculateAgeInMonths,testTOneYearAgo)}")
    print(f"Test Tomorrow 1  Months Ago: {0 == ageIn(calculateAgeInMonths,testTOneMonthAgo)}")
    print(f"Test Tomorrow 5  Months Ago: {4 == ageIn(calculateAgeInMonths,testTFiveMonthAgo)}")
    print(f"Test Tomorrow 7  Months Ago: {6 == ageIn(calculateAgeInMonths,testTSevenMonthAgo)}")
    print(f"Test Tomorrow 10 Months Ago: {9 == ageIn(calculateAgeInMonths,testTTenMonthAgo)}")
    

def testAgeInDays():
    yearsDiff = 1
    today = getTodayDate()

    testYOneYearAgo = f"{today['day']-1}-{monthName(today['month'])}-{today['year']-yearsDiff}"
    testYOneMonthAgo = f"{today['day']-1}-{monthName(today['month']-1)}-{today['year']-yearsDiff}"
    testYFiveMonthAgo = f"{today['day']-1}-{monthName(today['month']-5)}-{today['year']-yearsDiff}"
    testYSevenMonthAgo = f"{today['day']-1}-{monthName(today['month']-7)}-{today['year']-yearsDiff}"
    testYTenMonthAgo = f"{today['day']-1}-{monthName(today['month']-10)}-{today['year']-yearsDiff}"

    testOneYearAgo = f"{today['day']}-{monthName(today['month'])}-{today['year']-yearsDiff}"
    testOneMonthAgo = f"{today['day']}-{monthName(today['month']-1)}-{today['year']-yearsDiff}"
    testFiveMonthAgo = f"{today['day']}-{monthName(today['month']-5)}-{today['year']-yearsDiff}"
    testSevenMonthAgo = f"{today['day']}-{monthName(today['month']-7)}-{today['year']-yearsDiff}"
    testTenMonthAgo = f"{today['day']}-{monthName(today['month']-10)}-{today['year']-yearsDiff}"

    testTOneYearAgo = f"{today['day']+1}-{monthName(today['month'])}-{today['year']-yearsDiff}"
    testTOneMonthAgo = f"{today['day']+1}-{monthName(today['month']-1)}-{today['year']-yearsDiff}"
    testTFiveMonthAgo = f"{today['day']+1}-{monthName(today['month']-5)}-{today['year']-yearsDiff}"
    testTSevenMonthAgo = f"{today['day']+1}-{monthName(today['month']-7)}-{today['year']-yearsDiff}"
    testTTenMonthAgo = f"{today['day']+1}-{monthName(today['month']-10)}-{today['year']-yearsDiff}"


    # print("Testing Age In Months")
    print(f"Test Yesterday 1  Year   Ago: {15 == ageIn(calculateAgeInDays,testYOneYearAgo)}")
    print(f"Test Yesterday 1  Months Ago: {1 ==  ageIn(calculateAgeInDays,testYOneMonthAgo)}")
    print(f"Test Yesterday 5  Months Ago: {5 ==  ageIn(calculateAgeInDays,testYFiveMonthAgo)}")
    print(f"Test Yesterday 7  Months Ago: {7 ==  ageIn(calculateAgeInDays,testYSevenMonthAgo)}")
    print(f"Test Yesterday 10 Months Ago: {10 == ageIn(calculateAgeInDays,testYTenMonthAgo)}")
    # print("-")
    # print(f"Test Today 1  Year   Ago: {365 == ageIn(calculateAgeInMonths,testOneYearAgo)}")
    # print(f"Test Today 1  Months Ago: {1 == ageIn(calculateAgeInMonths,testOneMonthAgo)}")
    # print(f"Test Today 5  Months Ago: {5 == ageIn(calculateAgeInMonths,testFiveMonthAgo)}")
    # print(f"Test Today 7  Months Ago: {7 == ageIn(calculateAgeInMonths,testSevenMonthAgo)}")
    # print(f"Test Today 10 Months Ago: {10 == ageIn(calculateAgeInMonths,testTenMonthAgo)}")
    # print("-")
    # print(f"Test Tomorrow 1  Year   Ago: {11 == ageIn(calculateAgeInMonths,testTOneYearAgo)}")
    # print(f"Test Tomorrow 1  Months Ago: {0 == ageIn(calculateAgeInMonths,testTOneMonthAgo)}")
    # print(f"Test Tomorrow 5  Months Ago: {4 == ageIn(calculateAgeInMonths,testTFiveMonthAgo)}")
    # print(f"Test Tomorrow 7  Months Ago: {6 == ageIn(calculateAgeInMonths,testTSevenMonthAgo)}")
    # print(f"Test Tomorrow 10 Months Ago: {9 == ageIn(calculateAgeInMonths,testTTenMonthAgo)}")

def test():
    # testValidateDay()
    # testValidateYear()
    # testValidateMonth()
    # testSplitBirthdateString()
    # testAgeInYears()
    # testAgeInMonths()
    testAgeInDays()


def main():
    test()


if __name__ == "__main__":
    main()