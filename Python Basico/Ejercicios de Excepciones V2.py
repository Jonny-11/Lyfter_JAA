#Ejercicios de Excepciones
#1


def number_and_operator_separator(num):
    new_list = []
    new_num = ""
    #num = input("Tu numero: ")
    dived_num_list = list(num)
    list_size = int(len(dived_num_list))
    n = 1
    
    #first_num_in_list = dived_num_list.isdigit()
    for num_finder in dived_num_list:
        if num_finder.isdigit() == True:
            #print("Is the first number in the list is:",f"{num_finder}")
            #print(dived_num_list.index(num_finder))
            del dived_num_list[0:dived_num_list.index(num_finder)]
            break
        #print(dived_num_list.index())
        #print("--------------------")
    new_dived_num_list = len(dived_num_list)
    #print(dived_num_list)
    #print(new_dived_num_list)
    dived_num_list.reverse()
    # if dived_num_list[list_size]
    #print(list_size)




    for num_finder_reverse in dived_num_list:
        if num_finder_reverse.isdigit() == True:
            #print("El ultimo elemento no es un numero")
            #print("Is the first number in the list is:",f"{num_finder_reverse}")
            #print(dived_num_list.index(num_finder))
            del dived_num_list[0:dived_num_list.index(num_finder_reverse)]
            break
    #print(dived_num_list)
    new_dived_num_list = len(dived_num_list)
    dived_num_list.reverse()
    #print(dived_num_list)
    #print("Antes del While")


    while "+" in dived_num_list or "-" in dived_num_list or "/" in dived_num_list or "*" in dived_num_list:
        #print("En while")
        # index_of_operators_sum = dived_num_list.index("+")
        # index_of_operators_min = dived_num_list.index("-")
        # index_of_operators_multiplication = dived_num_list.index("*")
        # index_of_operators_division = dived_num_list.index("/")


        # if "-" in dived_num_list:
        #     index_of_operators_min = dived_num_list.index("-")
        # if "+" in dived_num_list:
        #     index_of_operators_sum = dived_num_list.index("+")

        # print(index_of_operators_sum)

        if "-" in dived_num_list:
            index_of_operators_min = dived_num_list.index("-")
            #print(index_of_operators_min)

            if ("+" == dived_num_list[index_of_operators_min+1] or "-" == dived_num_list[index_of_operators_min+1] or
                "*" == dived_num_list[index_of_operators_min+1] or "/" == dived_num_list[index_of_operators_min+1]):
                    
                    del dived_num_list[index_of_operators_min+1]

            if ("+" == dived_num_list[index_of_operators_min-1] or "-" == dived_num_list[index_of_operators_min-1] or
                "*" == dived_num_list[index_of_operators_min-1] or "/" == dived_num_list[index_of_operators_min-1]):\
                
                del dived_num_list[index_of_operators_min-1]

            else:
                break



        if "+" in dived_num_list:
            index_of_operators_sum = dived_num_list.index("+")

            if ("+" == dived_num_list[index_of_operators_sum+1] or "-" == dived_num_list[index_of_operators_sum+1] or
                "*" == dived_num_list[index_of_operators_sum+1] or "/" == dived_num_list[index_of_operators_sum+1]):
                    
                    del dived_num_list[index_of_operators_sum+1]

            if ("+" == dived_num_list[index_of_operators_sum-1] or "-" == dived_num_list[index_of_operators_sum-1] or
                "*" == dived_num_list[index_of_operators_sum-1] or "/" == dived_num_list[index_of_operators_sum-1]):

                del dived_num_list[index_of_operators_sum-1]

            else:
                break







        if "*" in dived_num_list:
            index_of_operators_multiplication = dived_num_list.index("*")

            if ("+" == dived_num_list[index_of_operators_multiplication+1] or "-" == dived_num_list[index_of_operators_multiplication+1] or
                "*" == dived_num_list[index_of_operators_multiplication+1] or "/" == dived_num_list[index_of_operators_multiplication+1]):
                    
                    del dived_num_list[index_of_operators_multiplication+1]            
            
            if ("+" == dived_num_list[index_of_operators_multiplication-1] or "-" == dived_num_list[index_of_operators_multiplication-1] or
                "*" == dived_num_list[index_of_operators_multiplication-1] or "/" == dived_num_list[index_of_operators_multiplication-1]):
                    
                    del dived_num_list[index_of_operators_multiplication-1]

            else:
                break


        if "/" in dived_num_list:

            index_of_operators_division = dived_num_list.index("/")

            if ("+" == dived_num_list[index_of_operators_division+1] or "-" == dived_num_list[index_of_operators_division+1] or
                "*" == dived_num_list[index_of_operators_division+1] or "/" == dived_num_list[index_of_operators_division+1]):
                    
                    del dived_num_list[index_of_operators_division+1]            
            
            if ("+" == dived_num_list[index_of_operators_division-1] or "-" == dived_num_list[index_of_operators_division-1] or
                "*" == dived_num_list[index_of_operators_division-1] or "/" == dived_num_list[index_of_operators_division-1]):
                    
                    del dived_num_list[index_of_operators_division-1]

            else:
                break



    



    #print("Fin del While")
    #print(dived_num_list)
    new_dived_num_list = len(dived_num_list)





    for evaluate in dived_num_list:
        if evaluate.isdigit():
            new_num += evaluate
            #print(new_num)
            if evaluate.isdigit() and new_dived_num_list == n:
                new_list.append(new_num)



        if evaluate == "+" or evaluate == "-" or evaluate == "/" or evaluate == "*":

                    new_list.append(new_num)
                    new_list.append(evaluate)
                    new_num = ""


        n = n+1
        #print(dived_num_list)
        #print(new_list)
    #print(new_list)
    print(new_list,"lista generada")
    return new_list


##########################################################################################################################################


def calculator(user_numbers):
    while True:
        try:
            start_up = input("Desea iniciar la calculadora? (Si/No): ")
            user_choice = start_up.lower()
            if user_choice == "si":



                    #initial_arithmetic_request = input("Introduce una equacion con suma, resta, multiplicacion o divicion: ")

                    initial_arithmetic_request = user_numbers

                    # user_num_1 = int(input("Introduce un numero: "))
                    # user_num_2 = int(input("Introduce un segundo numero: "))
                    #user_num_1 = (input("Introduce una suma, resta, multiplicacion o divicion: "))
                    # number_and_operator_separator(user_numbers)
                    user_num_list = number_and_operator_separator(initial_arithmetic_request)
                    #user_num_list = list(initial_arithmetic_request)
                    #print(user_num_list)
                    #print("----------------------------")


                    while "/" in user_num_list:
                        if "/" in user_num_list:
                            list_index = user_num_list.index("/")
                            start_list_index = list_index-1
                            end_list_index =  list_index+2
                            if list_index != 0:
                                result_of_div = int(user_num_list[list_index-1]) / int(user_num_list[list_index+1]) 
                                del user_num_list[start_list_index:end_list_index]
                                #print(result_of_div)
                                #print(user_num_list)
                                user_num_list.insert(list_index-1, result_of_div)


                    while "*" in user_num_list:
                        if "*" in user_num_list:
                            list_index = user_num_list.index("*")
                            start_list_index = list_index-1
                            end_list_index =  list_index+2
                            if list_index != 0:
                                result_of_mult = int(user_num_list[list_index-1]) * int(user_num_list[list_index+1]) 
                                del user_num_list[start_list_index:end_list_index]
                                #print(result_of_mult)
                                #print(user_num_list)
                                user_num_list.insert(list_index-1, result_of_mult)



                    while "+" in user_num_list:
                        if "+" in user_num_list:
                            list_index = user_num_list.index("+")
                            start_list_index = list_index-1
                            end_list_index =  list_index+2
                            if list_index != 0:
                                result_of_sum = int(user_num_list[list_index-1]) + int(user_num_list[list_index+1]) 
                                del user_num_list[start_list_index:end_list_index]
                                #print(result_of_sum)
                                #print(user_num_list)
                                user_num_list.insert(list_index-1, result_of_sum)

                    while "-" in user_num_list:
                        if "-" in user_num_list:
                            list_index = user_num_list.index("-")
                            start_list_index = list_index-1
                            end_list_index =  list_index+2
                            if list_index != 0:
                                result_of_min = int(user_num_list[list_index-1]) - int(user_num_list[list_index+1]) 
                                del user_num_list[start_list_index:end_list_index]
                                #print(result_of_min)
                                #print(user_num_list)
                                user_num_list.insert(list_index-1, result_of_min)

                    return user_num_list
                        # else:
                        #     del user_num_list[0]
                        #     print("----------------------------")
                        #     print(user_num_list)
                    if user_choice == "no":
                        #print("Programa cerrado")
                        break
        except:
            print("Hubo un error / Dividido entre 0")
            break




user_numbers = input("Introduce tu numero: ")
print("Resultado:",calculator(user_numbers))

# print(calculator(user_numbers))
#print(number_and_operator_separator())        