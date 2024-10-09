package main
import "fmt"

func doisUns(s string) bool {
    estado := "q0"
    for _, char := range s {
        if estado == "q0" && char == '1' {
            estado = "q1"
        } else if estado == "q1" && char == '1' {
            estado = "q2"
        } else if estado == "q2" && char == '1' {
            estado = "q3"
        }
    }
    return estado == "q2"
}

func main() {
    fmt.Println(doisUns("1100"))  // True
    fmt.Println(doisUns("111"))   // False
}
