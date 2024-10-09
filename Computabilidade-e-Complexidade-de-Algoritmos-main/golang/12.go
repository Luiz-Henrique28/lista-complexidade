package main
import "fmt"
import "strings"

func contem110(s string) bool {
    return strings.Contains(s, "110")
}

func main() {
    fmt.Println(contem110("1110"))  // True
    fmt.Println(contem110("1011"))  // False
}
