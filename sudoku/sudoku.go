package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
)

type oneBoard struct {
	cell [9]int
}

var fullBoard [9]oneBoard

func main() {
	choice := 0

	for {
		if choice == 0 {
			choice = option()
		}
		if choice == 1 {
			board()
			input := userInput()
			if input == 0 {
				choice = input
			}
			clearScreen()
		}
		if choice == 2 {
			fmt.Printf("Quitting sudoku")
			break
		}

	}
}

func board() {
	fmt.Printf("SUDOKU BOARD:\n")
	fmt.Printf("  1 2 3   4 5 6   7 8 9 COL\n")
	fmt.Printf(" ________________________\n")
	for i := 1; i <= 9; i++ {
		fmt.Printf("| ")
		for idx, pos := range fullBoard[i-1].cell {
			fmt.Printf("%d ", pos)
			if (idx+1)%3 == 0 {
				fmt.Printf("| ")
			}
		}

		if i%3 == 0 {
			fmt.Printf(" %d\n ________________________\n", i)
		} else {
			fmt.Printf(" %d\n", i)
		}
	}
}

func userInput() int {
	row, col, val := 0, 0, 0
	fmt.Printf("Enter row (-1 to quit): ")
	_, err := fmt.Scanf("%d\n", &row)
	if err != nil || row < 1 || row > 9 {
		fmt.Println("Value must be between 1 - 9\n Value enter : ", row, err)
		return checkExit(row)
	}

	fmt.Printf("Enter col (-1 to quit): ")
	_, err = fmt.Scanf("%d\n", &col)
	if err != nil || col < 1 || col > 9 {
		fmt.Println("Value must be between 1 - 9\n Value enter : ", col, err)
		return checkExit(col)
	}

	fmt.Printf("Enter value (-1 to quit): ")
	_, err = fmt.Scanf("%d\n", &val)
	if err != nil || val < 0 || val > 9 {
		fmt.Println("Value must be between 1 - 9\n Value enter : ", val, err)
		return checkExit(val)
	}
	fmt.Printf("Row : %d, Col : %d, Value : %d\n", row, col, val)

	fillBoard(row-1, col-1, val)
	return 1
}

func option() int {
	userInput := 0
	for {
		fmt.Printf("Enter a number :\n")
		fmt.Printf("Play sudoku - 1\n")
		fmt.Printf("Quit        - 2\n")

		fmt.Scanf("%d\n", &userInput)

		if userInput == 1 || userInput == 2 {
			break
		}

		fmt.Printf("Enter a vaild number\n")
		clearScreen()
	}

	return userInput
}

func fillBoard(row, col, val int) {
	if val == 0 {
		fullBoard[row].cell[col] = val
		return
	}
	valid := validMove(row, col, val)
	if valid == -1 {
		return
	}
	fullBoard[row].cell[col] = val
}

func validMove(row, col, val int) int {
	for i := 0; i < 9; i++ {
		// Check row
		if fullBoard[row].cell[i] == val {
			fmt.Printf("\n%d row contain duplicate value : %d\n", row+1, val)
			return -1
		}
		// Check col
		if fullBoard[i].cell[col] == val {
			fmt.Printf("\n%d col contain duplicate value : %d\n", col+1, val)
			return -1
		}
	}
	if row <= 3 {
		// Row 1 - 3
		if col <= 3 {
			// Column 1 - 3
		} else if col <= 6 {
			// Column 4 - 6
		} else {
			// Column 7 - 9
		}
	} else if row <= 6 {
		// Row 4 - 6

	} else {
		// Row 7 - 9
	}
	return 0
}

func checkSquareRow(row int) {

}

func checkSquareCol(col int) {

}

func clearScreen() {
	fmt.Print("Press 'Enter' to continue...")
	bufio.NewReader(os.Stdin).ReadBytes('\n')
	cmd := exec.Command("cmd", "/c", "cls")
	cmd.Stdout = os.Stdout
	cmd.Run()
}

func checkExit(input int) int {
	if input == -1 {
		return 0
	} else {
		return 1
	}
}
