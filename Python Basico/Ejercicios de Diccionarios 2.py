#Ejercicios de Diccionarios
#3
print("Escribe tu nombre")
user_name = input()
print("Escribe tu apellido")
user_last_name = input()
list_a = ["first_name", "last_name", "role"]
list_b = [user_name,user_last_name, "Electromechanical Engineer"]
my_dictionary = {list_a[0]:list_b[0],
                list_a[1]:list_b[1],
                list_a[2]:list_b[2]}
print("------------------------")
print("Nombre: "+f"{my_dictionary[list_a[0]]}\n"
        "Apellido: "+f"{my_dictionary[list_a[1]]}\n"
        "Posición: "+f"{my_dictionary[list_a[2]]}\n")