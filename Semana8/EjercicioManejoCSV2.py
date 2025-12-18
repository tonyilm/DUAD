import csv
import os


def videogames_csv(file_path,data,headers):
    file_exists = os.path.exists(file_path)
    with open(file_path,"a",encoding = "utf-8",newline="") as file:
        writer = csv.DictWriter(file,dialect="excel-tab",fieldnames=headers)
        if not file_exists:
            writer.writeheader()
        writer.writerows(data)

number_of_games = int(input("Ingrese el numero de videojuegos a registrar : "))
videogames_list = []


for index in range(number_of_games):
    print(f"Ingresando videojuego numero {index+1}")
    nombre = input("Nombre: ")
    genero = input("Género: ")
    desarrollador = input("Desarollador : ")
    clasificacion = input("Clasificación ESRB: ")


    video_game = {
    "Nombre": nombre,
    "Género": genero,
    "Desarrollador": desarrollador,
    "Clasificación ESRB": clasificacion

}

    videogames_list.append(video_game)


videogames_csv("videogames_file_2.csv",videogames_list,videogames_list[0].keys())