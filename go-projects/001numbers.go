package main

import (
	"fmt"
	"math"
	"strconv"
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

func main() {
	// fmt.Printf("%v\n", strconv.FormatFloat(piToNthDigit(3), 'f', 3, 64))
	// eToNthDigit() --- NOT FINISHED -- I'M SO CONFUSED ON HOW TO GET THIS
	// fmt.Printf("%v\n",fibonacci(0))
	// fmt.Printf("%v\n",primeFactorization(10))
	// fmt.Printf("%v\n",nextPrimeNumber(1))
	// fmt.Printf("%v\n",isPrimeNumber(11))
	// fmt.Printf("%v\n",findTileCost(5,5,2.50))
	fmt.Printf("")
}
