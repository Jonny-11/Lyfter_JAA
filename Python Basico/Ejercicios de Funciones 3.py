#Ejercicios de Funciones
#3

def invert_string():
    my_string = input("Introduce una palabra: ")
    #my_string = "Pizza con jamon y hongos"
    str_num = len(my_string)
    result_list = []
    for inverse_str in range(len(my_string) -1 ,-1, -1):
        result_list.append(my_string[inverse_str])
    final_result = "".join(result_list)
    return final_result
print(invert_string())