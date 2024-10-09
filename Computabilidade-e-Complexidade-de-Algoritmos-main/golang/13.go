package main
import "fmt"

func maisUns(s string) bool {
    count1, count0 := 0, 0
    for _, char := range s {
        if char == '1' {
            count1++
        } else if char == '0' {
            count0++
        }
    }
    return count1 > count0
}

func main() {
    fmt.Println(maisUns("110"))    // True
    fmt.Println(maisUns("10100"))  // False
}
