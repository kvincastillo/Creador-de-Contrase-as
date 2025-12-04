package main

import (
	"crypto/rand"
	"fmt"
	"math/big"
)

// caracteres que van a ser permitidos
const letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*?"

// hacemos una funcion para generar la contraseña
func PasswordGenerator(longitud int) (string, error) {
	password := ""
	for i := 0; i < longitud; i++ {
		num, err := rand.Int(rand.Reader, big.NewInt(int64(len(letters))))
		if err != nil {
			return "", err
		}
		password += string(letters[num.Int64()])
	}
	return password, nil
}

func main() {
	var longitud int
	fmt.Printf("Ingrese la cantidad de caracteres deseados: ")
	fmt.Scan(longitud)

	pass, err := PasswordGenerator(longitud)
	if err != nil {
		fmt.Println("Error al generar la contraseña!", err)
		return
	}
	fmt.Println("Contraseña genereada:", pass)
}
