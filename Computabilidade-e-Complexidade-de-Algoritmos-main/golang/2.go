package main
import "fmt"

func parDeZeros(s string) bool {
    estado := "q0"
    for _, char := range s {
        if estado == "q0" {
            if char == '0' {
                estado = "q1"
            } else if char == '1' {
                estado = "q0"
            }
        } else if estado == "q1" {
            if char == '0' {
                estado = "q0"
            } else if char == '1' {
                estado = "q1"
            }
        }
    }
    return estado == "q0"
}

func main() {
    fmt.Println(parDeZeros("101"))  // True
    fmt.Println(parDeZeros("100"))  // False
}
