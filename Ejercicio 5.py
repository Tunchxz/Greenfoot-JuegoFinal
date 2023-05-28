from Ejercicio5_Mod import *

while True:
    print("\n---# Bienvenidx a Cinépolis #---")
    print("Elige una de estas opciones para iniciar:")
    print("1. Crear cuenta")
    print("2. Iniciar Sesión")
    print("3. Salir")
    opcion = input("Ingresa tu opción: ")
    if opcion == "1":
        crear_usuario()
    elif opcion == "2":
        user = input("Ingrese su nombre de usuario: ")
        iniciar_sesion(user)

        while True:
            print("----------# ¡Bienvenido de nuevo! #----------")
            print("¿Qué deseas realizar?")
            print("1. Ver películas de un año específico")
            print("2. Ver las primeras n películas de un género ordenadas por rating")
            print("3. Ver todos los documentales, Dramas, Ciencia Ficción, Animación y Comedia, de un año específico")
            print("4. Ver el promedio de duración (en minutos) de las películas de un género específico")
            print("5. Ver la cantidad de películas por año de lanzamiento de los últimos 5 años")
            print("6. Ver un gráfico de barras con la información de la opción 5")
            print("7. Ver las primeras n películas con más votos")
            print("8. Ver las películas de un director específico")
            print("9. Ver los primeros n directores que tienen una mayor cantidad de películas")
            print("10. Ver los primeros n directores cuya primera profesión no es director")
            print("11. Crear/Editar mi lista de favoritos")
            print("12. Ver mis recomendaciones de películas")
            print("13. Cerrar sesión y salir")
            opcion = input("Ingresa tu opción: ")

            if opcion == "1":
                show_info()
            if opcion == "2":
                rating_list()
            if opcion == "3":
                show_genre()
            if opcion == "4":
                genre_time()
            if opcion == "5":
                last_movies()
            if opcion == "6":
                movies_graph()
            if opcion == "7":
                movie_votes()
            if opcion == "8":
                driector_movies()
            if opcion == "9":
                most_movies_director()
            if opcion == "10":
                not_directors()
            if opcion == "11":
                favorite_list(user)
            if opcion == "12":
                generar_recomendaciones(user)
            if opcion == "13":
                print("¡Sesión cerrada con éxito!")
                break

    elif opcion == "3":
        print("¡Gracias por usar nuestro programa!")
        break
    else:
        print("Ingresa una opción válida")

