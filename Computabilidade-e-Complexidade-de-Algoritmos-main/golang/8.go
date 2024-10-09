package main
import "fmt"

func divisivelPor3Zeros(s string) bool {
    countZeros := 0
    for _, char := range s {
        if char == '0' {
            countZeros++
        }
    }
    return countZeros % 3 == 0
}

func main() {
    fmt.Println(divisivelPor3Zeros("000111"))  // True
    fmt.Println(divisivelPor3Zeros("0011"))    // False
}
