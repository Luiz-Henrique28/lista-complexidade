package main
import (
    "fmt"
    "strings"
)

func exatamenteUmAb(s string) bool {
    return strings.Count(s, "ab") == 1
}

func main() {
    fmt.Println(exatamenteUmAb("abab"))  // False
    fmt.Println(exatamenteUmAb("aab"))   // True
}
