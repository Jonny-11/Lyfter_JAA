#Ejercicios de Iterables y Listas
#3
while True:
    try:
        print("Introduce un numero de fin de lista mayor que 0")
        end_size = int(input())
        if end_size > 0:
            break
    except:
        print("Solo se permiten numeros enteros o mayor a 0")
num_list = list(range(0,end_size))
print(num_list)
num_list.insert(0,int(num_list[end_size-1]))
num_list.insert(end_size,int(num_list[1]))
num_list.pop(1)
num_list.pop(end_size)
print(num_list)