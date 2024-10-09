package main
import "fmt"

func inicioFimIgual(s string) bool {
    if len(s) < 1 {
        return false
    }
    return s[0] == s[len(s)-1]
}

func main() {
    fmt.Println(inicioFimIgual("101"))  // True
    fmt.Println(inicioFimIgual("100"))  // False
}
