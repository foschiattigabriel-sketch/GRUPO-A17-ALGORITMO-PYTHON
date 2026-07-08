def ver_estadisticas():
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
    print(f"La más elegida por el público es: {ranking[0][1]['titulo']}")
    print("-----------------------------------------------------")


def encuesta_satisfaccion():
    print("\n----------------------------------------------------")
    print("     ENCUESTA DE SATISFACCION - CINE PLUS")
    print("----------------------------------------------------")
    print("Nos gustaria conocer tu opinion para mejorar la app.")
    print("Es completamente opcional y solo toma 1 minuto.")
    print("----------------------------------------------------")
    print("1. Responder encuesta")
    print("2. Salir de la encuesta")

    while True:
        opcion_encuesta = input("Selecciona una opcion (1 o 2): ").strip()
        if opcion_encuesta == "1":
            break
        if opcion_encuesta == "2":
            print("Esta bien, ¡gracias por usar Cine Plus!")
            exit()
        else:
            print("Opcion invalida. Ingresa 1 para responder o 2 para saltar.")

    respuestas = {}

    # Pregunta 1: Puntuacion general
    while True:
        print("Pregunta 1: ¿Como calificarias tu experiencia general con la app?")
        print("1. Muy mala")
        print("2. Mala")
        print("3. Regular")
        print("4. Buena")
        print("5. Excelente")
        rta1 = input("Selecciona una opcion (1-5): ").strip()
        if rta1 in ["1", "2", "3", "4", "5"]:
            opciones_p1 = {"1": "Muy mala", "2": "Mala", "3": "Regular", "4": "Buena", "5": "Excelente"}
            respuestas["experiencia_general"] = opciones_p1[rta1]
            break
        else:
            print("Opcion invalida. Selecciona un numero del 1 al 5.")

    # Pregunta 2: Facilidad de uso
    while True:
        print("\nPregunta 2: ¿Te resulto facil usar el sistema de reservas?")
        print("1. Si, muy facil")
        print("2. Mas o menos")
        print("3. No, me resulto confuso")
        rta2 = input("Selecciona una opcion (1-3): ").strip()
        if rta2 in ["1", "2", "3"]:
            opciones_p2 = {"1": "Si, muy facil", "2": "Mas o menos", "3": "No, me resulto confuso"}
            respuestas["facilidad_de_uso"] = opciones_p2[rta2]
            break
        else:
            print("Opcion invalida. Selecciona un numero del 1 al 3.")

    # Pregunta 3: Volveria a usar la app
    while True:
        print("\nPregunta 3: ¿Volveria a usar Cine Plus para tus proximas reservas?")
        print("1. Si, definitivamente")
        print("2. Tal vez")
        print("3. No")
        rta3 = input("Selecciona una opcion (1-3): ").strip()
        if rta3 in ["1", "2", "3"]:
            opciones_p3 = {"1": "Si, definitivamente", "2": "Tal vez", "3": "No"}
            respuestas["volveria_a_usar"] = opciones_p3[rta3]
            break
        else:
            print("Opcion invalida. Selecciona un numero del 1 al 3.")

    # Mostrar resumen de respuestas
    print("\n--- Gracias por completar la encuesta ---")
    print(f"Experiencia general  : {respuestas['experiencia_general']}")
    print(f"Facilidad de uso     : {respuestas['facilidad_de_uso']}")
    print(f"Volveria a usar      : {respuestas['volveria_a_usar']}")
    print("Tus respuestas fueron registradas. ¡Nos ayudan mucho a mejorar!")
    print("MUCHAS GRACIAS, QUE TENGA UN EXCELENTE DIA!")
    exit()


peliculas = {
    1: {"titulo": "Avengers: Endgame", "entradas": 100, "entradas_totales": 100, "precio": 5000, "horario1": "10:30", "horario2": "18:30", "horario3": "20:00"},
    2: {"titulo": "El señor de los anillos", "entradas": 50, "entradas_totales": 50, "precio": 4500, "horario1": "09:00", "horario2": "16:00", "horario3": "19:30"},
    3: {"titulo": "El planeta de los simios", "entradas": 5, "entradas_totales": 5, "precio": 4000, "horario1": "13:30", "horario2": "17:00", "horario3": "21:30"}
}

mostrar_cartelera = {
    1: "Avengers: Endgame",
    2: "El señor de los anillos",
    3: "El planeta de los simios"
}


def menu_reservas():
    while True:
        print("Cartelera:")
        for cod_peli, titulo in mostrar_cartelera.items():
            print(f"{cod_peli}. {titulo}")
        cod_peli = int(input("Seleccione el numero correspondiente a la pelicula que quieres ver. Escriba 0 para volver al menú principal: "))
        if cod_peli == 0:
            return
        pelicula_seleccionada = peliculas[cod_peli]
        titulo_peli = pelicula_seleccionada["titulo"]
        if pelicula_seleccionada["entradas"] > 0:
            while True:
                if cod_peli == 1:
                    print("Horarios de Avengers: Endgame:")
                    print("1. 10:30")
                    print("2. 18:30")
                    print("3. 20:00")
                    horario_elegido = int(input("elige el numero del horario que desees: "))
                if cod_peli == 2:
                    print("Horarios de El Señor de los Anillos:")
                    print("1. 09:00")
                    print("2. 16:00")
                    print("3. 19:30")
                    horario_elegido = int(input("elige el numero del horario que desees: "))
                if cod_peli == 3:
                    print("Horarios de El planeta de los simios:")
                    print("1. 13:30")
                    print("2. 17:00")
                    print("3. 21:30")
                    horario_elegido = int(input("elige el numero del horario que desees: "))
                if horario_elegido == 1:
                    hora = pelicula_seleccionada["horario1"]
                    break
                if horario_elegido == 2:
                    hora = pelicula_seleccionada["horario2"]
                    break
                if horario_elegido == 3:
                    hora = pelicula_seleccionada["horario3"]
                    break
                else:
                    print("numero no valido. Vuelva a intentarlo")
        else:
            print("No quedan entradas para esta función. Vuelve más tarde.")
            return

        while True:
            entradas_pedidas = int(input(f"¿Cuantas entradas deseas? (Disponibles: {pelicula_seleccionada['entradas']}): "))
            if entradas_pedidas > pelicula_seleccionada["entradas"] or entradas_pedidas <= 0:
                print("No hay suficientes entradas disponibles. Intente más tarde.")
                continue
            else:
                break

        while True:
            print(titulo_peli, "|", hora, "|", entradas_pedidas, "entradas", "| Total:", entradas_pedidas * pelicula_seleccionada["precio"])
            confir_rta = input("CONFIRMAR COMPRA(SI/NO): ")
            if confir_rta.lower() == "si":
                pelicula_seleccionada["entradas"] = pelicula_seleccionada["entradas"] - entradas_pedidas
                print("¡Reserva hecha con éxito!")
                return
            if confir_rta.lower() == "no":
                print("Reserva cancelada :(")
                return
            else:
                print("Respuesta invalida. Ingresa si para reservar o no para cancelar.")


def menu_principal():
    while True:
        print("------------------------------------------------------------------------------------")
        print("BIENVENIDO A CINE PLUS, LAS MEJORES RESERVAS PARA TU VISITA AL CINE EN UN SOLO LUGAR")
        print("------------------------------------------------------------------------------------")
        print("1. Reservar entrada")
        print("2. Ver estadisticas de las mas vendidas")
        print("3. Salir")
        eleccion = input("seleccione una de las opciones: ").strip()
        if eleccion == "1":
            menu_reservas()
        elif eleccion == "2":
            ver_estadisticas()
        elif eleccion == "3":
            print("Gracias por visitarnos, ¡vuelve pronto!")
            encuesta_satisfaccion()
        else:
            print("Opcion invalida")


menu_principal()
