package main
import "fmt"

func peloMenosUmZero(s string) bool {
    for _, char := range s {
        if char == '0' {
            return true
        }
    }
    return false
}

func main() {
    fmt.Println(peloMenosUmZero("101"))  // True
    fmt.Println(peloMenosUmZero("111"))  // False
}
