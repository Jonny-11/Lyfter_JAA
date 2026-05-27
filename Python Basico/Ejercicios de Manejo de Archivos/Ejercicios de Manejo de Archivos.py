# Ejercicios de Manejo de Archivos
#


def file_opener(user_file_to_open):
    user_list = []
    with open(user_file_to_open) as file:
        for line_read in file.readlines():
            print(line_read)
            user_list.append(line_read)
    print("-------------------------")
    user_list.sort()        
    return user_list


def new_file_and_order(user_list):
    with open("canciones ordenadas.txt","w") as file:
        for new_list in user_list:
            file.write(new_list)
            print(new_list)





my_list = file_opener("canciones.txt")
new_file_and_order(my_list)