package main
import "fmt"
import "strings"

func contem101(s string) bool {
    return strings.Contains(s, "101")
}

func main() {
    fmt.Println(contem101("1101"))  // True
    fmt.Println(contem101("1110"))  // False
}
