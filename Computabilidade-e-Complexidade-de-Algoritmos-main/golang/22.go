package main
import "fmt"

func diferencaMultiplo3(s string) bool {
    diferenca := 0
    for _, char := range s {
        if char == 'a' {
            diferenca++
        } else if char == 'b' {
            diferenca--
        }
    }
    return diferenca%3 == 0
}

func main() {
    fmt.Println(diferencaMultiplo3("aaabbb"))  // True
    fmt.Println(diferencaMultiplo3("aab"))     // False
}
