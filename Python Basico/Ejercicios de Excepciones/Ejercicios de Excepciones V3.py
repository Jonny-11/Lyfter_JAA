#Ejercicios de Excepciones
#1


def calculator():
    current_number = 0

    while True:
        print("\nNúmero actual:", current_number)
        print("Seleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Borrar resultado")
        print("6. Salir")
        print("---------------------------------")
        try:
            option = int(input("Opción: "))

            if option == 6:
                print("Saliendo de la calculadora...")
                break

            if option == 5:
                current_number = 0
                print("Resultado borrado.")
                continue
            if option in [1, 2, 3, 4]:
            
                try:
                    number = float(input("Ingrese el número: "))

                    if option == 1:
                        current_number += number
                    elif option == 2:
                        current_number -= number
                    elif option == 3:
                        current_number *= number
                    elif option == 4:
                        if number == 0:
                            print("Error: No se puede dividir entre 0.")
                            continue
                        current_number /= number
                except:
                    print("Numero no valido")
                    print("Introduce un nuevo numero")
                    print("---------------------------------")
                print("Nuevo resultado:", current_number)
            else:
                print("Opcion no disponible")
        except:
            
            print("Opción inválida, no has seleccionado alguna de las opciones")
    print("---------------------------------")
    return current_number

print("Resultado de operaciones",calculator())
