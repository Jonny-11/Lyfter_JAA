#Ejercicios de Iterables y Listas
#1
first_list = ["Aprender", "en", "ayuda", "a", "problemas", "complejos"]
second_list = ["programación", "Python", "mucho", "resolver", "técnicos", "reales"]
word_place=0
for order in first_list and second_list:
    print(first_list[word_place],second_list[word_place])
    word_place = word_place+1