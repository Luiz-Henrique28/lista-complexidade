package main
import "fmt"
import "strings"

func sem11Ou00(s string) bool {
    return !strings.Contains(s, "11") && !strings.Contains(s, "00")
}

func main() {
    fmt.Println(sem11Ou00("1010"))  // True
    fmt.Println(sem11Ou00("1100"))  // False
}
