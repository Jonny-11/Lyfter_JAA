#Ejercicios de Funciones
#5


def string_plus_hyphen(word):
    words_list = word.split("-")
    sort_list = sorted(words_list)
    final_str = str("-".join(sort_list))
    #print(str(final_str))
    return final_str


my_word = input("Palabra: ")
print(string_plus_hyphen(my_word))