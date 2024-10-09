package main
import "fmt"

func aAposCadaB(s string) bool {
    for i := 0; i < len(s)-1; i++ {
        if s[i] == 'b' && s[i+1] != 'a' {
            return false
        }
    }
    return true
}

func main() {
    fmt.Println(aAposCadaB("baa"))   // False
    fmt.Println(aAposCadaB("abab"))  // True
}
