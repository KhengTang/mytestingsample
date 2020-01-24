package main

import (
	"fmt"
)

type Vertex struct {
	X int
	Y int
}

var (
	v1 = Vertex{1, 2}
	v2 = Vertex{3}
	v3 = Vertex{}
	p  = &Vertex{3, 4}
)

func printSlice(s []int) {
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}

func main() {
	testSlice()
}

func testSlice() {
	names := [4]string{
		"John",
		"Paul",
		"George",
		"Ringo",
	}

	a := names[0:2]
	b := names[1:3]
	fmt.Println(a, b)
	b[0] = "XXX"
	fmt.Println(a, b)
	fmt.Println(names)

	s := []int{2, 3, 5, 7, 11, 13}
	printSlice(s)

	// Slice the slice to give it zero length.
	// But capacity remain
	s = s[:0]
	printSlice(s)

	// Extend its length.
	s = s[:4]
	printSlice(s)

	s = s[0:6]
	printSlice(s)

	// Drop its first two values.
	s = s[2:]
	printSlice(s)
}
