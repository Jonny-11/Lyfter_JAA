# Ejercicios de Manejo de CSVs
#1

import csv

def save_video_games_tsv():
    video_games = []
    
    n = int(input("¿Cuántos videojuegos desea ingresar?: "))

    for i in range(n):
        print("\nVideojuego", i+1)
        name = input("Nombre: ")
        genre = input("Género: ")
        developer = input("Desarrollador: ")
        esrb_rating = input("Clasificación ESRB: ")

        video_games.append([name, genre, developer, esrb_rating])

    # Guardar en archivo separado por tabulaciones
    with open("video_games.tsv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter="\t")
        
        # Headers
        writer.writerow(["Name", "Genre", "Developer", "ESRB Rating"])
        
        # Data
        writer.writerows(video_games)

    print("\nDatos guardados en video_games.tsv")

save_video_games_tsv()