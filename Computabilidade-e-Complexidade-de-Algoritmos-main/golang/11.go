package main
import "fmt"

func imparAs(s string) bool {
    estado := "q0"
    for _, char := range s {
        if estado == "q0" && char == 'a' {
            estado = "q1"
        } else if estado == "q1" && char == 'a' {
            estado = "q0"
        }
    }
    return estado == "q1"
}

func main() {
    fmt.Println(imparAs("a"))    // True
    fmt.Println(imparAs("aa"))   // False
    fmt.Println(imparAs("aba"))  // True
}
