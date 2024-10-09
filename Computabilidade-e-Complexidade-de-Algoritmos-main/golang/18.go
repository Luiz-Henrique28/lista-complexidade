package main
import "fmt"

func imparZerosUns(s string) bool {
    count0, count1 := 0, 0
    for _, char := range s {
        if char == '0' {
            count0++
        } else if char == '1' {
            count1++
        }
    }
    return count0 % 2 != 0 && count1 % 2 != 0
}

func main() {
    fmt.Println(imparZerosUns("101"))   // True
    fmt.Println(imparZerosUns("1100"))  // False
}
