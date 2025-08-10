package main

import "fmt"

/*99 Bottles

Create a program that prints out every line to the song "99 bottles of beer on the wall."

    Do not use a list for all of the numbers, and do not manually type them all in. Use a built in function instead.
    Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
    Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
*/

func _99bottles() {
	for i := 5; i > 2; i-- {
		fmt.Printf("%v bottles of beer on the wall, %v bottles of beer.\nTake one down and pass it around, %v bottles of beer on the wall.\n\n", i, i, i-1)
	}

	for i := 2; i > 2; i-- {
		fmt.Printf("2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.")
		fmt.Printf("1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.")
	}

	fmt.Printf("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")

}

func main() {
	_99bottles()
}

/*
Magic 8 Ball

Simulate a magic 8-ball.

    Allow the user to enter their question.
    Display an in progress message(i.e. "thinking").
    Create 20 responses, and show a random response.
    Allow the user to ask another question or quit.

Bonus:

    Add a gui.
    It must have box for users to enter the question.
    It must have at least 4 buttons:
        ask
        clear (the text box)
        play again
        quit (this must close the window)

Pythagorean Triples Checker

If you do not know how basic right triangles work, read this article on Wikipedia.

    Allows the user to input the sides of any triangle in any order.
    Return whether the triangle is a Pythagorean Triple or not.
    Loop the program so the user can use it more than once without having to restart the program.

Rock Paper Scissors Game

Create a rock-paper-scissors game.

    Ask the player to pick rock, paper or scissors.
    Have the computer chose its move.
    Compare the choices and decide who wins.
    Print the results.

Subgoals:

    Give the player the option to play again.
    Keep a record of the score (e.g. Player: 3 / Computer: 6).

Coin Estimator By Weight

When some people receive change after shopping, they put it into a container and let it add up over time. Once they fill up the container, they'll roll them up in coin wrappers which can then be traded in at a bank for what they are worth.

    Allow the user to input the total weight of each type of coin they have (pennies, nickels, dimes, and quarters).
    Print out how many of each type of coin wrapper they would need, how many coins they have, and the estimated total value of all their money.

Subgoals:

    Round all numbers printed out to the nearest whole number.
    Allow the user to select whether they want to submit the weight in either grams or pounds.
*/
