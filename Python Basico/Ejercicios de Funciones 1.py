#Ejercicios de Funciones
#1


def str_1(string_1 = "Pizza", quantity = 1, string_2 = "no"):
    print(string_1)
    print(quantity)
    str_2(string_2)


def str_2(string_2):
    if string_2.lower() == "si":
        print("Con bebida")
    if string_2.lower() == "no":
        print("Sin bebida")


def start():
    print("Ingrese una comida y cantidad")
    string_1 = input("Tipo de Comida -> ")
    quantity = input("Cantidad -> ")
    print("Desea agregar una bebida")
    string_2 = input("Si o No -> ")
    str_1(string_1,quantity, string_2)

start()