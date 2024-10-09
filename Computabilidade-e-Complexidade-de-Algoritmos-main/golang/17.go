package main
import "fmt"
import "strings"

func termina01(s string) bool {
    return strings.HasSuffix(s, "01")
}

func main() {
    fmt.Println(termina01("1101"))  // True
    fmt.Println(termina01("1000"))  // False
}
