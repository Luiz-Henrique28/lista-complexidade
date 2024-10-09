package main
import "fmt"

func blocosDeZeros(s string) bool {
    estado := "q0"
    for _, char := range s {
        if estado == "q0" && char == '0' {
            estado = "q1"
        } else if estado == "q1" {
            if char == '1' {
                estado = "q2"
            }
        } else if estado == "q2" && char == '0' {
            return false
        }
    }
    return true
}

func main() {
    fmt.Println(blocosDeZeros("00111"))  // True
    fmt.Println(blocosDeZeros("010"))    // False
}
