REPOSITORIO DEL GRUPO A17 DE LA MATERIA ALGORITMO Y ESTRUCTURA DE DATOS

Esta conformado por:

-Salas, maidana Lucas Mariano  31814
-Sanguina, Comparin Franco     31884
-Sanguina, Ignacio Ezequiel    31639
-Foschiatti, gabriel agustin   31165
-Pertile, Tiago Ezequiel       31337


*En este repositorio se encuentra nuestro archivo en formato python para ejecutar el programa/algoritmo, tambien se encuentra un video demo probandolo. Es el siguiente: https://youtu.be/P2WSV-Bj9Qw

     peliculas = {
    1: {"titulo": "Avengers: Endgame", "entradas": 100, "precio": 5000, "horario1": "10:30", "horario2": "18:30", "horario3": "20:00"},
    2: {"titulo": "El señor de los anillos", "entradas": 50, "precio": 4500, "horario1": "09:00", "horario2": "16:00", "horario3": "19:30"},
    3: {"titulo": "El planeta de los simios", "entradas": 5, "precio": 4000, "horario1": "13:30", "horario2": "17:00", "horario3": "21:30"}
    }

    def menu_reservas():
    while True:
        print("mostrar_cartelera()")
        cod_peli=int(input("Seleccione el numero correspondiente a la pelicula que quieres ver. Escriba 0 para volver al menú principal: "))
        if cod_peli==0:
            return
        pelicula_seleccionada = peliculas[cod_peli]
        titulo_peli = pelicula_seleccionada["titulo"]
        if pelicula_seleccionada["entradas"]>=0:
            while True:
                if cod_peli == 1 :
                    print("Horarios de Avengers: Endgame:")
                    print("1. 10:30")
                    print("2. 18:30")
                    print("3. 20:00")
                    horario_elegido=int(input("elige el numero del horario que desees: "))
                if cod_peli == 2 :
                    print("Horarios de El Señor de los Anillos:")
                    print("1. 09:00")
                    print("2. 16:00")
                    print("3. 19:30")
                    horario_elegido=int(input("elige el numero del horario que desees: "))
                if cod_peli == 3 :
                    print("Horarios de El planeta de los simios:")
                    print("1. 13:30")
                    print("2. 17:00")
                    print("3. 21:30")
                    horario_elegido=int(input("elige el numero del horario que desees: "))
                if horario_elegido==1:
                    hora= pelicula_seleccionada["horario1"]
                    break
                if horario_elegido==2:
                        hora=pelicula_seleccionada["horario2"]
                        break
                if horario_elegido==3:
                    hora=pelicula_seleccionada["horario3"]
                    break           
                else:
                    print("numero no valido. Vuelva a intentarlo")
        else:
            print("No quedan entradas para esta función. Vuelve más tarde.")
        entradas_pedidas=int(input(f"¿Cuantas entradas deseas? (Disponibles: {pelicula_seleccionada["entradas"]}): "))
        while True:
            if entradas_pedidas >= pelicula_seleccionada["entradas"]:
                print("No hay suficientes entradas disponibles. Intente más tarde.")
                continue
            else:
                break
        while True:
            print(titulo_peli, "|", hora, "|", entradas_pedidas, "entradas""|" "Total:", pelicula_seleccionada["entradas"])
            confir_rta=input("CONFIRMAR COMPRA(S/N): ")
            if confir_rta.upper()== "S":
                pelicula_seleccionada["entradas"]=pelicula_seleccionada["entradas"]-entradas_pedidas
                print("¡Reserva hecha con éxito!")
                return
            if confir_rta.upper()== "N":
                print("Reserva cancelada")
                return
            



                
        
    

    def menu_principal():
         while True:            
             print("------------------------------------------------------------------------------------")
             print("BIENVENIDO A CINE PLUS, LAS MEJORES RESERVAS PARA TU VISITA AL CINE EN UN SOLO LUGAR")
             print("------------------------------------------------------------------------------------")
             print("1. Reservar entrada")
             print("2. Ver estadisticas y ventas actuales")
             print("3. Salir")
        eleccion =input("seleccione una de las opciones: ").strip()
        if eleccion == "1":
            menu_reservas()
        if eleccion=="2":
            print("menu_estadisticas_ventas()")
        if eleccion=="3":
            print("Gracias por visitarnos, ¡vuelve pronto!")
            break
        else:
            print("Opcion invalida")
    menu_principal()" 

*este fue el primer codigo que sacamos, probamos cosas y fue cambiando durante el transcurso del trabajo, agregando, cambiando y sacando cosas.

    "def ver_estadisticas():
    entradas_totales_vendidas = 0
    ventas_por_pelicula = {}


    # Calculo cuántas entradas se vendieron de cada película
    for cod, peli in peliculas.items():
        vendidas = peli["entradas_totales"] - peli["entradas"]
        ventas_por_pelicula[cod] = {
            "titulo": peli["titulo"],
            "vendidas": vendidas
        }
        entradas_totales_vendidas += vendidas

    print("=====================================================")
    print("¿QUÉ ES TENDENCIA? - POPULARIDAD EN CARTELERA")
    print("=====================================================")

    if entradas_totales_vendidas == 0:
        print("Todavía no hay ventas registradas.")
        return

    # Ordeno de más a menos vendida para armar un ranking
    ranking = sorted(ventas_por_pelicula.items(), key=lambda item: item[1]["vendidas"], reverse=True)

    for posicion, (cod, datos) in enumerate(ranking, start=1):
        porcentaje = (datos["vendidas"] / entradas_totales_vendidas) * 100
        print(f"{posicion}° - {datos['titulo']} ({porcentaje:.2f}% de las entradas vendidas)")

    print("-----------------------------------------------------")
    print(f"La más elegida por el público es: {ranking[0][1]['titulo']}" )
    print("-----------------------------------------------------")"

*este es el la parte de codigo que creamos en principio para el tema de las estadisticas.

    while True:
        opcion_encuesta = input("Selecciona una opcion (1 o 2): ").strip()
        if opcion_encuesta == "1":
            break
        elif opcion_encuesta == "2":
            print("Esta bien, ¡gracias igual por usar Cine Plus!")
            return
        else:
            print("Opcion invalida. Ingresa 1 para responder o 2 para saltar.")"

 *esta parte fue la primera que utilizamos como un cuerpo de codigo para crear la parte de encuestas.
