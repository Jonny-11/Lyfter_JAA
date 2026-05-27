#Ejercicios de Iterables y Listas
#4
num_list = list(range(0,21))
even_list=[]
print(num_list)
for even in num_list:
    if even  % 2 == 0:
        even_list.append(even)
print(even_list)