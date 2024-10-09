package main
import "fmt"

func comprimentoPar(s string) bool {
    return len(s) % 2 == 0
}

func main() {
    fmt.Println(comprimentoPar("ab"))   // True
    fmt.Println(comprimentoPar("aba"))  // False
}
