package main

import (
	"fmt"
	"strings"
)

/*Fizz Buzz - Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.*/

func fizzBuzz(num int) {

	for i := 1; i <= num; i++ {
		phraseString := []string{}

		if i%3 == 0 {
			phraseString = append(phraseString, "fizz")
		}
		if i%5 == 0 {
			phraseString = append(phraseString, "buzz")
		}

		phraseJoined := strings.Join(phraseString[:], "")
		if phraseJoined == "" {
			fmt.Printf("%v\n", i)
		} else {
			fmt.Printf("%s\n", phraseJoined)
		}
	}
}

func main() {
	// a := 3
	// fmt.Printf("%v\n", strconv.FormatFloat(piToNthDigit(3), 'f', 3, 64))
	// eToNthDigit() --- NOT FINISHED -- I'M SO CONFUSED ON HOW TO GET THIS
	// fmt.Printf("%v\n",fibonacci(a))
	// fmt.Printf("%v\n",fibonacciLoop(a))
	// fmt.Printf("%v\n",primeFactorization(10))
	// fmt.Printf("%v\n",nextPrimeNumber(1))
	// fmt.Printf("%v\n",isPrimeNumber(11))
	// fmt.Printf("%v\n",findTileCost(5,5,2.50))
	// fmt.Printf("%v\n", mortgageCalculator(a))
	// fmt.Printf("%v\n", changeReturn(5.20, 191.58))
	// fmt.Printf("%v\n", changeReturn(180.50, 400.30))
	// fmt.Printf("%v\n", binaryToDecimal(a))
	// fmt.Printf("%v\n", decimalToBinary(a))
	// fmt.Printf("%v\n", factorialLoop(a))
	fizzBuzz(20)

}
