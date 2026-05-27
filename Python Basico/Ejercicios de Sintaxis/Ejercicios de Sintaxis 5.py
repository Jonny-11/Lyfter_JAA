# Ejercicios de Sintaxis
# 5
print("Introduce cantidad de notas")
while True:
    try:
        quantity = int(input())
        break
    except:
        print("Solo se permiten numeros enteros")
grade_quantity = 0
user_grades = []
aprove_grade = []
fail_grade = []
aprove_count = 0
fail_count = 0
if quantity > 0:
    while quantity != grade_quantity:
        print("Introduce nota ganada")
        grade = int(input())
        while grade < 0:
            print("Las notas no pueden ser negativas")
            grade = int(input())
        user_grades.append(grade)
        grade_quantity = grade_quantity+1
    for aprove in user_grades:
        if aprove >= 70:
            aprove_grade.append(aprove)
            aprove_count = aprove_count+1
    for fail in user_grades:
        if fail < 70:
            fail_grade.append(fail)
            fail_count = fail_count+1

    print("Cantidad de aprobadas:",f"{aprove_count}")
    print("Cantidad de desaprobadas:",f"{fail_count}")
    print("Promedio de todas las notas", f"{sum(user_grades)/len(user_grades)}")
    if aprove_count > 0:
        print("Promedio de notas mayor a 70:", f"{sum(aprove_grade)/len(aprove_grade)}")
    if fail_count > 0:
        print("Promedio de notas menor a 70:", f"{sum(fail_grade)/len(fail_grade)}")
else:
    print("No hay notas")