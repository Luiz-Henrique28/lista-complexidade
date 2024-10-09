package main
import "fmt"

func terminaCom1(s string) bool {
    estado := "q0"
    for _, char := range s {
        if estado == "q0" {
            if char == '0' {
                estado = "q0"
            } else if char == '1' {
                estado = "q1"
            }
        } else if estado == "q1" {
            if char == '0' {
                estado = "q0"
            } else if char == '1' {
                estado = "q1"
            }
        }
    }
    return estado == "q1"
}

func main() {
    fmt.Println(terminaCom1("101"))  // True
    fmt.Println(terminaCom1("100"))  // False
}
