package main

import "fmt"

func calculate(a, b int, sign string) int {
	switch sign {
	case "+":
		return a + b
	case "-":
		return a - b
	case "*":
		return a * b
	case "/":
		return a / b
	}
	return 0
}

func main() {
	valueA, valueB := 0, 0
	sign := ""
	fmt.Printf("Enter 2 value : ")
	fmt.Scanf("%d %v %d", &valueA, &sign, &valueB)
	fmt.Printf("The value you enter are %v and %v\n", valueA, valueB)
	fmt.Printf("%d %v %d = %d", valueA, sign, valueB, calculate(valueA, valueB, sign))
}
