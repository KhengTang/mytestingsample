package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
)

var board [9]int

func main() {
	choice := 0
	for {
		if choice == 0{
			choice = option()
		}
		if choice == 1 {
			printBoard()

			if !userInput() {
				break
			}
			clearScreen()
		}
	}
}

func printBoard() {
	for i := 0; i < 9; i++ {
		if board[i] == 0 {
			fmt.Printf("%d", i)
		} else if board[i] == 1 {
			fmt.Printf("X")
		} else if board[i] == 2 {
			fmt.Printf("O")
		}
		if ((i + 1) % 3) != 0 {
			fmt.Printf("|")
		}else if i == 8 {
			fmt.Printf("\n")
		} else {
			fmt.Printf("\n-----\n")
		}
	}
}

func option() int {
	userInput := 0
	for {
		fmt.Printf("Enter a number :\n")
		fmt.Printf("(1)Play TicTacToe\n")
		fmt.Printf("(-1)Quit\n")

		fmt.Scanf("%d\n", &userInput)

		if userInput == 2 || userInput == 1 || userInput == -1 {
			break
		}

		fmt.Printf("Enter a vaild number\n")
		clearScreen()
	}

	return userInput
}

func userInput() bool {
	cell := 0
	var str string
	fmt.Printf("Select space to fill :")
	_, err := fmt.Scanf("%d\n", &cell)
	if err != nil || cell < 1 || cell > 9 {
		if cell == -1 {
			return false
		}
		fmt.Printf("Please enter a valid number")
		return true
	}
	fmt.Printf("Enter X | O :")
	_, err = fmt.Scanf("%d\n", &str)
	if err != nil || str == "x" || str == "X" || str == "o" ||str == "O" {
		fmt.Printf("Please enter a valid choice")
		return true
	}

	if str == "x" || str == "X" {
		board[cell] = 1
	} else {
		board[cell] = 2
	}
	return true
}

func clearScreen() {
	fmt.Print("Press 'Enter' to continue...")
	bufio.NewReader(os.Stdin).ReadBytes('\n')
	cmd := exec.Command("cmd", "/c", "cls")
	cmd.Stdout = os.Stdout
	cmd.Run()
}
