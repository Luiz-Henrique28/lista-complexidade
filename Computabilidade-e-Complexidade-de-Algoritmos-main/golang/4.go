package main
import "fmt"

func aoMenosUmZero(s string) bool {
    estado := "q0"
    for _, char := range s {
        if estado == "q0" && char == '0' {
            estado = "q1"
        }
    }
    return estado == "q1"
}

func main() {
    fmt.Println(aoMenosUmZero("110"))  // True
    fmt.Println(aoMenosUmZero("111"))  // False
}
