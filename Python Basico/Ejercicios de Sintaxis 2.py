# Ejercicios de Sintaxis
# 2
print("Introduce tu nombre")
name = input("")
print("Introduce tu apellido")
last_name = input("")
print("Introduce tu edad")
age = int(input())
if age==0 and age<=2:
    print("Eres un bebé")
if age>2 and age<=10:
    print("Eres un niño")
if age>10 and age<=12:
    print("Eres un preadolescente")
if age>12 and age<=17:
    print("Eres un adolescente")
if age>17 and age<=29:
    print("Eres un adulto joven")
if age>29 and age<=59:
    print("Eres un adulto")
if age>59:
    print("Eres un adulto mayor")