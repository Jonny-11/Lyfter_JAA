#Ejercicios de Diccionarios
#3
user_name = ("Jonathan")
user_last_name = ("Abad")
user_position = "Electromechanical Engineer"
list_a = ["first_name", "last_name", "role"]
list_b = [user_name,user_last_name, user_position]
my_dictionary = {list_a[0]:list_b[0],
                list_a[1]:list_b[1],
                list_a[2]:list_b[2]}
print("------------------------")
print("Nombre: "+f"{my_dictionary[list_a[0]]}\n"
        "Apellido: "+f"{my_dictionary[list_a[1]]}\n"
        "Posición: "+f"{my_dictionary[list_a[2]]}\n")
print("Deseas Eliminar datos? Si/No")
while True:
    try:
        delete_user_data = input().strip().lower()
        if delete_user_data == "si":
            break
        if delete_user_data == "no":
            print("------------------------")
            print("No se borran datos")
            break
        else:
            print("Escoge Si/No")
    except:
        print("Escoge Si/No")
print("------------------------")
if delete_user_data == "si":
    print("Escoge una de las tres opciones (1,2,3)")
    print("Eliminar nombre (1)")
    print("Eliminar apellido (2)")
    print("Eliminar posición (3)")
    while True:
        try:
            delete_option = int(input())
            if 1 <= delete_option <= 3:
                new_list = list_a.pop(delete_option-1)
                new_dictionary = my_dictionary.pop(new_list)
                break
            else:
                print("Solo puede poner números (1,2,3)")
        except:
                print("Solo puede poner números (1,2,3)")
    print("------------------------")
    if new_dictionary == user_name:
        print("Borraste nombre")
    if new_dictionary == user_last_name:
        print("Borraste apellido")
    if new_dictionary == user_position:
        print("Borraste posición")
    print(new_dictionary)
    print("------------------------")
    print("Lista actualizada")
    for data in my_dictionary.values():
        print(data)
else:
    print("Fin")
print("Fin")