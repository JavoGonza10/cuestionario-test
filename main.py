import json
import random
import time


def cargar_preguntas():
    """Esta funcion devuelve la lista de preguntas del cuestionario."""
    preguntas = [
        {"enunciado": "¿Cuál es la capital de Francia?",
         "opciones": ["A) Madrid", "B) Berlín", "C) París", "D) Roma"],
         "respuesta_correcta": "C",
         "tema": "geografia"},
        {"enunciado": "¿Cuál es el planeta más grande del sistema solar?",
         "opciones": ["A) Marte", "B) Júpiter", "C) Saturno", "D) Venus"],
         "respuesta_correcta": "B",
         "tema": "astronomia"},
        {"enunciado": "¿Cuál es el océano más grande del mundo?",
         "opciones": ["A) Atlántico", "B) Índico", "C) Pacífico", "D) Ártico"],
         "respuesta_correcta": "C",
         "tema": "geografia"},
        {"enunciado": "¿Cuál es el país más poblado del mundo?",
         "opciones": ["A) India", "B) Estados Unidos", "C) China", "D) Rusia"],
         "respuesta_correcta": "C",
         "tema": "geografia"},
        {"enunciado": "¿Cuál es el río más largo del mundo?",
         "opciones": ["A) Amazonas", "B) Nilo", "C) Yangtsé", "D) Misisipi"],
         "respuesta_correcta": "A",
         "tema": "geografia"},
        {"enunciado": "¿Quién compuso la Novena Sinfonía, conocida como la 'Coral'?",
         "opciones": ["A) Mozart", "B) Beethoven", "C) Bach", "D) Chopin"],
         "respuesta_correcta": "B",
         "tema": "musica"},
        {"enunciado": "¿Quién compuso 'Las cuatro estaciones'?",
         "opciones": ["A) Vivaldi", "B) Haydn", "C) Verdi", "D) Wagner"],
         "respuesta_correcta": "A",
         "tema": "musica"},
    ]
    return preguntas


def guardar_ranking(ranking):
    """Guarda el ranking en el archivo JSON, escribiendo en el archivo y asegurando que los caracteres especiales se escriban correctamente."""
    with open("ranking.json", "w", encoding="utf-8") as archivo:
        json.dump(ranking, archivo, ensure_ascii=False, indent=2)


def cargar_ranking():
    """Carga el ranking desde el archivo JSON y hace el uso de try-except para manejar el caso en que el json no exista."""
    try:
        with open("ranking.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []


def mostrar_pregunta(pregunta):
    """Esta función muestra la pregunta y sus opciones."""
    print(pregunta["enunciado"])
    for opcion in pregunta["opciones"]:
        print(opcion)
    print()


def obtener_respuesta():
    """Pide la respuesta al usuario y la devuelve solo si es A, B, C o D. Si no, vuelve a pedirla."""
    while True:
        respuesta = input("Ingresa la letra de tu respuesta: ").strip().upper()
        if respuesta in ["A", "B", "C", "D"]:
            return respuesta
        else:
            print("Respuesta inválida. Por favor, ingresa A, B, C o D.")


def corregir_respuesta(respuesta, respuesta_correcta):
    """Esta función devuelve True si la respuesta coincide con la correcta, False si no."""
    return respuesta == respuesta_correcta


def mostrar_resultado(aciertos, total):
    """Esta función muestra el resultado final del cuestionario."""
    porcentaje = (aciertos / total) * 100
    print(f"Tu puntaje final es: {porcentaje:.2f}% = {aciertos}/{total}")
    if porcentaje >= 90:
        print("¡Felicidades!")
    elif porcentaje >= 70:
        print("¡Bien hecho!")
    else:
        print("Necesitas mejorar. ¡Sigue practicando!")



def listar_tema(preguntas):      
    """Esta función lista los temas disponibles en el cuestionario."""
    lista_temas = []
    for pregunta in preguntas:
        if pregunta["tema"] not in lista_temas:
            lista_temas.append(pregunta["tema"])
    return lista_temas

def elegir_tema(temas):
    """Esta función permite al usuario elegir un tema de la lista de temas disponibles."""
    print("Temas disponibles:")
    for i, tema in enumerate(temas, start=1):
        print(f"{i}. {tema}")
    
    while True:
        try:
            eleccion = int(input("Selecciona un tema por número: "))
            if eleccion >= 1 and eleccion <= len(temas):
                return temas[eleccion - 1]
            else:
                print("Número inválido. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

def filtrar_preguntas_por_tema(preguntas, tema):
    """Esta función filtra las preguntas según el tema elegido por el usuario."""
    preguntas_filtradas = []
    for pregunta in preguntas:
        if pregunta["tema"] == tema:
            preguntas_filtradas.append(pregunta)
    return preguntas_filtradas


def realizar_cuestionario(ranking):
    """Esta función realiza el cuestionario completo, desde pedir el nombre del usuario hasta mostrar el resultado final y guardar el ranking."""
    nombre = input("Ingresa tu nombre: ").strip()
    LIMITE_TIEMPO = 6 
    preguntas = cargar_preguntas()
    temas = listar_tema(preguntas)
    tema_elegido = elegir_tema(temas)
    preguntas = filtrar_preguntas_por_tema(preguntas, tema_elegido)
    random.shuffle(preguntas)  # Mezclar las preguntas para cada intento
    puntaje = 0

    for pregunta in preguntas:
        mostrar_pregunta(pregunta)
        inicio_tiempo = time.time()
        respuesta_usuario = obtener_respuesta()
        fin_tiempo = time.time()
        tiempo_respuesta = fin_tiempo - inicio_tiempo
        print(f"Tiempo de respuesta: {tiempo_respuesta:.2f} segundos")
        if tiempo_respuesta > LIMITE_TIEMPO:
            print(f"¡Tiempo excedido! Tenías {LIMITE_TIEMPO} segundos para responder.")
            print(f"La respuesta correcta era: {pregunta['respuesta_correcta']}")

        elif corregir_respuesta(respuesta_usuario, pregunta["respuesta_correcta"]):
            print("¡Correcto!")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta era: {pregunta['respuesta_correcta']}")

        print()  # Línea en blanco para separar preguntas

    mostrar_resultado(puntaje, len(preguntas))
    ranking.append({"nombre": nombre, "aciertos": puntaje, "total": len(preguntas)})
    guardar_ranking(ranking)


def mostrar_ranking(ranking):
    """Muestra el ranking de jugadores y sus puntajes en orden descendente es decir de mayor a menor."""
    if not ranking:
        print("Aún no hay resultados en el ranking.")
        return
    print("=== RANKING ===")
    ranking_ordenado = sorted(ranking, key=lambda jugador: jugador["aciertos"], reverse=True)
    posicion = 1
    for jugador in ranking_ordenado:
        print(f"{posicion}. {jugador['nombre']} - {jugador['aciertos']}/{jugador['total']}")
        posicion += 1


def main():
    """Muestra el menú principal en bucle hasta que el usuario elige salir."""
    ranking = cargar_ranking()
    while True:
        print("== MENU ==")
        print("1. Empezar cuestionario")
        print("2. Ranking")
        print("3. Salir")
        opcion = input("Selecciona una opción: ").strip()
        if opcion == "1":
            print("¡Bienvenido al cuestionario tienes un límite de tiempo de 6 segundos para cada pregunta!")
            realizar_cuestionario(ranking)
        elif opcion == "2":
            mostrar_ranking(ranking)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona 1, 2 o 3.")

    #Esto de abajo lo quise poner porque en una clase un compi lo escribió en un ejercicio y no tenia ni idea de para que servia,
    #asi que lo investigue y lo puse, basicamente es para que en el archivo main.py se ejecute la funcion main(), 
    #pero si se importa como modulo no se ejecute.
if __name__ == "__main__": 
    main()

    
