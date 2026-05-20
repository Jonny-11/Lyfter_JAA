# Ejercicios de Manejo de CSVs
#1

import csv

def save_video_games():
    video_games = []
    
    n = int(input("¿Cuántos videojuegos desea ingresar?: "))

    for i in range(n):
        print("\nVideojuego", i+1)
        name = input("Nombre: ")
        genre = input("Género: ")
        developer = input("Desarrollador: ")
        esrb = input("Clasificación ESRB: ")

        video_games.append([name, genre, developer, esrb])

    # Guardar en CSV
    with open("video_games.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        # Headers
        writer.writerow(["Name", "Genre", "Developer", "ESRB Rating"])
        
        # Data
        writer.writerows(video_games)

    print("\nDatos guardados en video_games.csv")

save_video_games()