# Ejercicios de Sintaxis
# 4
print("Introduce tres numeros")
user_num1 = int(input())
user_num2 = int(input())
user_num3 = int(input())
user_num_list = [user_num1,user_num2,user_num3]
if user_num1-user_num2 == 0 and user_num1-user_num3 == 10:
    print("Todos los numeros son iguales")
else:
    larges_number = max(user_num_list)
    print("El numero mayor es ",f"{larges_number}")