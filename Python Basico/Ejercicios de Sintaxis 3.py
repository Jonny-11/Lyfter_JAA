# Ejercicios de Sintaxis
# 3
import random
num = random.randint(1,10)
print("Adivina un numero del 1 al 10")
print("introduce un numero")
user_num = int(input())
while num != user_num:
    print("Numero incorrecto")
    print("introduce un numero")
    user_num = int(input())
print("Numero correcto es el" ,f"{user_num}")