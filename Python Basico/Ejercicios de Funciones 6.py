#Ejercicios de Funciones
#6


def prime_numbers_identification(my_num_list):
    num_quantity = len(my_num_list)
    n = 0
    no_prime_num = []
    prime_num_list = []
    for num_quantity in my_num_list:
        num_to_divide = list(range(2,num_quantity))
        for divisor in num_to_divide:
            if num_quantity > 1:
                    check_1 = num_quantity%divisor
                    if check_1 == 0:
                        no_prime_num.append(num_quantity)
                        break
    for num_to_compare in my_num_list:
        if num_to_compare > 1:
            if num_to_compare not in no_prime_num:
                prime_num_list.append(num_to_compare)
    return prime_num_list


print("--------------------------------")
print("Numeros primos de tu lista:",f"{prime_numbers_identification([1, 4, 6, 7, 13, 9, 67, 8 ,11,2])}")
print("--------------------------------")

