package main
import "fmt"
import "strings"

func contem010(s string) bool {
    return strings.Contains(s, "010")
}

func main() {
    fmt.Println(contem010("001010"))  // True
    fmt.Println(contem010("1101"))    // False
}
