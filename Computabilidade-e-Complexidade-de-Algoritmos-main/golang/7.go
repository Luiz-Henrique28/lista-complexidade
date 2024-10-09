package main
import "fmt"
import "strings"

func comeca01Termina10(s string) bool {
    return strings.HasPrefix(s, "01") && strings.HasSuffix(s, "10")
}

func main() {
    fmt.Println(comeca01Termina10("0110"))  // True
    fmt.Println(comeca01Termina10("0100"))  // False
}
