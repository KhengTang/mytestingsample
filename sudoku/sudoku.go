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

func partFill() {
	fullBoard[0].cell[0] = 1
	fullBoard[0].cell[1] = 2
	fullBoard[0].cell[2] = 3

	fullBoard[1].cell[0] = 4
	fullBoard[1].cell[1] = 5
	fullBoard[1].cell[2] = 6

	fullBoard[2].cell[0] = 7
	fullBoard[2].cell[1] = 8
	fullBoard[2].cell[2] = 9
}

func main() {
	choice := 0

	for {
		if choice == 0 {
			// Menu page
			choice = option()
		}
		// Manual play
		if choice == 1 {
			board()
			input := userInput()
			if input == 0 {
				// Exit game
				choice = input
			}
			clearScreen()
		}
		// Backtrack solving
		if choice == 2 {
			board()

			// Sudoku solved
			if backtrack() {
				fmt.Printf("Sudoku solved\n")
				choice = 0
				clearScreen()
			} else {
				fmt.Printf("No valid solution\n")
				choice = 0
				clearScreen()
			}
		}
		if choice == -1 {
			// Quit program
			fmt.Printf("Quitting sudoku\n")
			clearScreen()
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
		return checkValidInput(row, err)
	}

	fmt.Printf("Enter col (-1 to quit): ")
	_, err = fmt.Scanf("%d\n", &col)
	if err != nil || col < 1 || col > 9 {
		return checkValidInput(col, err)
	}

	fmt.Printf("Enter value (0 to clear cell) (-1 to quit): ")
	_, err = fmt.Scanf("%d\n", &val)
	if val != 0 {
		if err != nil || val < 1 || val > 9 {
			return checkValidInput(val, err)
		}
	}

	fmt.Printf("Row : %d, Col : %d, Value : %d\n", row, col, val)

	fillBoard(row-1, col-1, val)
	return 1
}

func checkValidInput(input int, err error) int {
	if input == -1 {
		fmt.Printf("Exiting game\n")
	} else {
		fmt.Println("Value must be between 1 - 9\n Value enter : ", input, err)
	}
	return checkExit(input)

}

func option() int {
	userInput := 0
	for {
		fmt.Printf("Enter a number :\n")
		fmt.Printf("(1)Play sudoku\n")
		fmt.Printf("(2)Solved sudoku\n")
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

func emptyCell(row, col *int) bool {
	// Loop row
	for *row = 0; *row < 9; *row++ {
		// Row column
		for *col = 0; *col < 9; *col++ {
			if fullBoard[*row].cell[*col] == 0 {
				// There is empty cell
				return true
			}
		}
	}
	// Board is full
	return false
}

func backtrack() bool {

	row, col := 0, 0

	// All cell all fill up
	if !emptyCell(&row, &col) {
		return true
	}

	// Try all value
	for k := 1; k <= 9; k++ {
		if validMove(row, col, k) == 0 {
			fullBoard[row].cell[col] = k
			board()
			cmd := exec.Command("cmd", "/c", "cls")
			cmd.Stdout = os.Stdout
			cmd.Run()
			// Solved sudoku
			if backtrack() {
				return true
			}

			// Reset cell value
			fullBoard[row].cell[col] = 0
		}
	}
	return false
}

func validMove(row, col, val int) int {
	for i := 0; i < 9; i++ {
		// Check row
		if fullBoard[row].cell[i] == val {
			//fmt.Printf("\nRow %d col %d contain duplicate value : %d\n", row+1, i+1, val)
			return -1
		}
		// Check col
		if fullBoard[i].cell[col] == val {
			//fmt.Printf("\nRow %d col %d contain duplicate value : %d\n", i+1, col+1, val)
			return -1
		}
	}

	return checkSquareRow((row)/3, col/3, val)
}

func checkSquareRow(row, col, val int) int {
	ret := 0
	for i := row * 3; i < (row+1)*3; i++ {
		ret = checkSquareCol(i, col, val)
		if ret == -1 {
			return ret
		}
	}
	return ret
}

func checkSquareCol(row, col, val int) int {
	for i := col * 3; i < (col+1)*3; i++ {
		if fullBoard[row].cell[i] == val {
			//var box int
			//box = ((row+1)/3)*3 - 3 + col
			//fmt.Printf("\nBox %d contain duplicate value : %d\n", box, val)
			return -1
		}
	}
	return 0
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
