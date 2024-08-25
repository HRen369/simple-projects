# Celsius --> Other Temps
def convertCelsiusToFahrenheit(tempC):
    return (tempC * 9/5) + 32


def convertCelsiusToKelvin(tempC):
    return tempC + 273.15


# Fahrenheit --> Other Temps
def convertToFarenheightToCelsius(tempF):
    return (tempF - 32) * 5/9


def convertFahrenheitToKelvin(tempF):
    return convertToFarenheightToCelsius(tempF) + 273.15


# Kelvin --> Other Temps
def convertKelvinToFahrenheit(tempK):
    return convertCelsiusToFahrenheit(tempK - 273.15)


def convertKelvinToCelsius(tempK):
    return tempK - 273.15


def testCelsius():
    expectedFah = 104
    expectedKel = 313
    testTempC = 40

    testedFah = convertCelsiusToFahrenheit(testTempC)
    testedKel = convertCelsiusToKelvin(testTempC)
    print("Celsius Tests:")
    print("Tested Fahrenheit:",int(testedFah) == int(expectedFah))
    print("Tested Kelvin:",int(testedKel) == int(expectedKel))
    print("-----")


def testFarhrenheit():
    expectedCel = 40
    expectedKel = 313
    testTempF = 104

    testedCel = convertToFarenheightToCelsius(testTempF)
    testedKel = convertFahrenheitToKelvin(testTempF)
    print("Fahrenheit Tests:")
    print("Tested Celsius:",int(testedCel) == int(expectedCel))
    print("Tested Kelvin:",int(testedKel) == int(expectedKel))
    print("-----")


def testKelvin():
    expectedCel = 40
    expectedFah = 104
    testTempK = 313.15

    testedCel = convertKelvinToCelsius(testTempK)
    testedFah = convertKelvinToFahrenheit(testTempK)
    print("Kelvin Tests:")
    print("Tested Celsius:",int(testedCel) == int(expectedCel))
    print("Tested Fahrenheit:",int(testedFah) == int(expectedFah))
    print("-----")

def test():
    testCelsius()
    testFarhrenheit()
    testKelvin()


def main():
    test()


if __name__ == "__main__":
    main()