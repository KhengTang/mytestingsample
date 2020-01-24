package main

import(
	"fmt"
	"time"
	"math/rand"
	"math"
	"math/cmplx"
)

var c, python, java = true, false, "no!"

var(
	ToBe    bool        = false
	MaxInt  uint64      = 1<<64-1
	z       complex128  = cmplx.Sqrt(-5 + 12i)
)

func main(){
	constant()
}

func sum(x, y int) int {
	return x + y
}

func swap(x, y string) (string, string){
	return y, x
}

func timeTour(){
	fmt.Println("Welcome to testing workspace")
	fmt.Println("The time now is : ", time.Now())
}

func split(sum int) (x, y int){
	x = sum * 4 / 9
	y = sum - x
	return
}

func randomTour(){
	x := 54
	y := 61

	strX := "World"
	strY := "Hello"

	second := time.Now().UnixNano()
	rand.Seed(int64(second))
	fmt.Println("My random favorite number is : ", rand.Intn(10))
	fmt.Printf("Now you have %g problems.\n", math.Sqrt(9))
	fmt.Println("The pi value is : ", math.Pi)
	fmt.Printf("Sum of %d + %d is %d.\n", x, y, sum(x, y))

	a, b := swap(strX,strY)
	fmt.Println("Swap ", strX, " & " , strY, " position : ", a, b)

	fmt.Println(split(51))

	var i, j = 1, 2
	k := 5
	e := "Hello"

	fmt.Println(i, j, k , e, c, python, java, "\n")

	fmt.Printf("Type: %T Value: %v\n", ToBe, ToBe)
	fmt.Printf("Type: %T Value: %v\n", MaxInt, MaxInt)
	fmt.Printf("Type: %T Value: %v\n", z, z)
}

func conversion(){
	//var x, y  = 3, 4
	//var f float64 = math.Sqrt(float64(x*x + y*y))
	//var z uint = uint(f)
	//fmt.Println(x, y, z)

	i := 42
	f := float64(i)
	u := uint(f)

	fmt.Println(i, f, u)
}

const Pi = 3.14

func constant(){
	const World = "世界"
	fmt.Println("Hello", World)
	fmt.Println("Happy", Pi, "Day")

	const Truth = true
	fmt.Println("Go rules?", Truth)
}