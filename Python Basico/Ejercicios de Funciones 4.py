#Ejercicios de Funciones
#4

def lower_and_upper_case_counter(word_evaluate):
    upper_letters = 0
    lower_letters = 0
    for letters in range(len(word_evaluate)):
        if word_evaluate[letters].isupper() == True:
            upper_letters = upper_letters+1

        if word_evaluate[letters].islower() == True:
            lower_letters = lower_letters+1
    print("Hay",f"{upper_letters}","mayusculas","y",f"{lower_letters}","minusculas")
    return [upper_letters ,lower_letters]


print("Escribe una palabra")
word = input()
print("----------------------")
lower_and_upper_case_counter(word)