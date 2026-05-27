#Ejercicios de Funciones
#2

def input_num_list():
    print("Digite números para sumar")
    print("Cuando termine de digitar números, presione Enter")
    my_num_list = []
    while True:
        try:
            user_num = int(input("Introduce un numero "))
            my_num_list.append(user_num)
        except:
            return my_num_list
            print("except")


def sum_num(numbers):
    num_sum = sum(numbers)
    return num_sum


user_num = input_num_list()
print("Numeros digitados")
print(user_num)
user_sum_num = sum_num(user_num)
print("________________________")
print("Total:",user_sum_num)