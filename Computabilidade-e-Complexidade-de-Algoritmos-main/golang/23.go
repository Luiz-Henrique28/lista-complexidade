package main
import (
    "fmt"
    "strings"
)

func contem101Ou110(s string) bool {
    return strings.Contains(s, "101") || strings.Contains(s, "110")
}

func main() {
    fmt.Println(contem101Ou110("1101"))  // True
    fmt.Println(contem101Ou110("1001"))  // False
}
