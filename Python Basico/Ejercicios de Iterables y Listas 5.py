#Ejercicios de Iterables y Listas
#5
#import random
num_list=[]
large_num = None
print("Introduce 10 numeros")
while True:
    try:
        num = int(input())
        #num = random.randint(0,30)
        num_list.append(num)
        if len(num_list) == 10:
            break
    except:
        print("Solo se permiten numeros enteros o mayor a 0")
large_num = num_list[0]
for num_order in num_list:
    if num_order > large_num:
        large_num = num_order
print("Tus numeros",num_list,",el numero mas alto de la lista es",large_num)
