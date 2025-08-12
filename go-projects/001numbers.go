package main

import (
	"math"
	"strconv"
	"strings"
)

/*
Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.
*/
func piToNthDigit(k int) float64 {
	sum := 0.0
	i := 0

	for i <= k {
		var iFloat float64 = float64(i)

		var a float64 = 1 / (math.Pow(16, float64(iFloat)))
		var b float64 = ((4.0 / (8.0*iFloat + 1.0)) - (2.0 / (8.0*iFloat + 4.0)) - (1.0 / (8.0*iFloat + 5.0)) - (1.0 / (8.0*iFloat + 6.0)))
		sum += (a * b)

		i += 1.0
	}
	return sum
}

/*
Find e to the Nth Digit - Just like the previous problem, but with e instead of PI. Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.
*/

func factorial(num int) int {
	// factorial 5 = 5 * 4 *3 * 2 * 1
	if num <= 1 {
		return 1
	}
	return num * factorial(num-1)
}

func factorialLoop(num int) int {
	if num < 0 {
		panic("Not a valid number")
	}

	sum := 1
	for i := 1; i <= num; i++ {
		sum *= i
	}

	return sum
}

/*func eToNthDigit()float64 {
	i := 0
	// k := 3
	sum := 2.0

	for i <= k {
		a := 1.0 / float64(factorial(i))
		sum += a

		i += 1

	}
}*/

/*
Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
F0 = 0, F1 = 1, Fn = Fn-1 + Fn-2 for n > 1
*/

func fibonacci(num int) int {
	if num < 0 {
		panic("Invalid Number. Number needs to greater than 0")
	}

	if num == 0 || num == 1 {
		return num
	}

	return fibonacci(num-1) + fibonacci(num-2)
}

func fibonacciLoop(num int) int {
	if num < 0 {
		panic("Invalid Number. Number needs to greater than 0")
	}

	if num == 0 || num == 1 {
		return num
	}

	var n1 int = 0
	var n2 int = 1

	var switchToOther bool = true
	for i := 3; i <= num; i++ {
		if switchToOther == true {
			n1 += n2
			switchToOther = false
		} else {
			n2 += n1
			switchToOther = true
		}
	}

	return n1 + n2
}

/*
Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
*/

func primeFactorization(num int) map[string]int {
	m := make(map[string]int)

	for i := 2; i <= num; i++ {
		tempNum := num
		for tempNum%i == 0 {
			numStr := strconv.Itoa(i)
			_, val := m[numStr]

			if val {
				m[numStr] += 1
			} else {
				m[numStr] = 1
			}

			tempNum = tempNum / 2
		}
	}
	return m
}

/*
Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.
  - Prime Number: A whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1 (e.g. 2, 3, 5, 7, 11)
*/
func isPrimeNumber(num int) bool {
	if num == 1 {
		return false
	}

	for i := 2; i < num; i++ {
		if num%i == 0 {
			return false
		}
	}
	return true
}

// TODO: add function program to prompt
// func nextPrimeNumber(num int) int{}

/*
Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.
*/

func findTileCost(width float64, height float64, tileCost float64) float64 {
	return (width * height) * tileCost
}

/*
Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. Also figure out how long it will take the user to pay back the loan. For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).
*/

/*
Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. Also figure out how long it will take the user to pay back the loan. For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).
*/

func mortgageCalculator(num int) float64 {
	principal := 300000.0
	rate := .05 / 12
	n := 30.0 * 12

	p1 := math.Pow((1 + rate), n)

	return (principal * rate * p1) / (p1 - 1)
}

/*
Change Return Program - The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.
*/
func changeReturn(cost float64, amountGiven float64) map[string]int {
	var change float64 = amountGiven - cost
	m := make(map[string]int)

	if change < 0.0 {
		panic("Did not cover the cost of item.")
	}

	var denominations = [10]float64{100.00, 50.00, 20.00, 10.00, 5.00, 1.00, 0.25, 0.10, 0.05, 0.01}

	for _, denomination := range denominations {
		for (change > 0.0 && change-denomination >= denomination) || change-denomination >= 0.0 {
			change = change - denomination

			numStr := strconv.FormatFloat(denomination, 'f', 2, 64)
			_, val := m[numStr]

			if val {
				m[numStr] += 1
			} else {
				m[numStr] = 1
			}
		}
	}
	return m
}

/*
Binary to Decimal and Back Converter - Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.
(0 * 2^3) + (1 * 2^2) + (1 * 2^1) + (1 * 2^0) = 0 + 4 + 2 + 1 = 7
*/

func binaryToDecimal(binaryString string) int {
	sum := 0
	currentPow := float64(len(binaryString)) - 1

	for _, charValue := range binaryString {
		sum += (int(charValue) - 48) * int(math.Pow(2, currentPow))
		currentPow -= 1

	}
	return sum
}

func decimalToBinary(num int) string {
	binaryString := []string{}

	for num > 0 {
		binaryString = append(binaryString, strconv.Itoa(num%2))
		num /= 2
	}

	i := 0
	j := len(binaryString) - 1
	for i < j {
		temp := binaryString[i]
		binaryString[i] = binaryString[j]
		binaryString[j] = temp

		i += 1
		j -= 1
	}

	return strings.Join(binaryString[:], "")
}

/*Calculator - A simple calculator to do basic operators. Make it a scientific calculator for added complexity.*/

/*Alarm Clock - A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.*/

/*Distance Between Two Cities - Calculates the distance between two cities and allows the user to specify a unit of distance. This program may require finding coordinates for the cities like latitude and longitude.*/

/*Credit Card Validator - Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer) and validates it to make sure that it is a valid number (look into how credit cards use a checksum).*/

/*Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.*/

func collatzConjecture(num int) int {
	if num <= 1 {
		panic("Number is less than 1")
	}
	steps := 0

	for num > 2 {
		if num%2 == 0 {
			num = num / 2
		} else {
			num = (num * 3) + 1
		}
		steps += 1
	}

	return steps + 1
}
