package main
import (
    "fmt"
    "strings"
)

func duasVezes010(s string) bool {
    return strings.Count(s, "010") >= 2
}

func main() {
    fmt.Println(duasVezes010("0101010"))  // True
    fmt.Println(duasVezes010("101010"))   // False
}
