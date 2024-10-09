package main
import (
    "fmt"
    "strings"
)

func aAntesDeB(s string) bool {
    return !strings.Contains(s, "ba")
}

func main() {
    fmt.Println(aAntesDeB("aaabbb"))  // True
    fmt.Println(aAntesDeB("abba"))    // False
}
