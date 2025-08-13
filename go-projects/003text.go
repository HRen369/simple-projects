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

/*Reverse a String - Enter a string and the program will reverse it and print it out.*/
func reverseString(word string) string {
	reverseStringArray := []rune{}

	for i := len(word) - 1; i >= 0; i-- {
		reverseStringArray = append(reverseStringArray, rune(word[i]))

	}
	return string(reverseStringArray)
}

/*Pig Latin - Pig Latin is a game of alterations played on the English language game. To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.

/*Count Vowels - Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.*/

func countVowels(word string) map[string]int {
	m := make(map[string]int)
	m["a"] = 0
	m["e"] = 0
	m["i"] = 0
	m["o"] = 0
	m["u"] = 0

	for _, charValue := range word {
		_, val := m[string(charValue)]

		if val {
			m[string(charValue)] += 1
		}
	}

	return m
}

/*Check if Palindrome - Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar”
 */

 func palindrome(word string)bool{
	i:=0
	j:=len(word)-1

	for i < j{
		if word[i] != word[j]{
			return false
		}
		i+=1
		j-=1

	}

	return true
	//return reverseString(word) == word
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
	// fizzBuzz(20)
	// fmt.Printf("%s\n", reverseString("hello"))
	// fmt.Printf("%s\n", countVowels("hello"))
	fmt.Printf("%s\n", palindrome("racecar"))
	fmt.Printf("%s\n", palindrome("hello"))

}
