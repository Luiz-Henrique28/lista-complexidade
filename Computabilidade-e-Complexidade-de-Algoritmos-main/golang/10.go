package main
import "fmt"
import "strings"

func zeroSeguidoUm(s string) bool {
    return strings.Contains(s, "01")
}

func main() {
    fmt.Println(zeroSeguidoUm("101"))  // True
    fmt.Println(zeroSeguidoUm("111"))  // False
}
