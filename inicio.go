package main

import (
	"fmt"
	"reflect"
)

func main() {
	fmt.Println("Hola soy.. ")
	/*
		Esto es un comentariooo....
	*/

	//variables
	var nombre string = "Kevin"
	fmt.Println(nombre)
	var edad int = 19
	var apellido string = "Castillo"
	fmt.Println(nombre, apellido, "y tengo", edad, "años")

	fmt.Println(reflect.TypeOf(edad))
	if edad >= 18 {
		fmt.Println("Eres mayor de edad")
	} else {
		fmt.Println("Menor de edad")
	}

	var MyBol bool = false
	MyBol = true
	fmt.Println(MyBol)

	//Esto es unico de Golang
	Ciudad := "Atenas"
	fmt.Println(Ciudad)

}
