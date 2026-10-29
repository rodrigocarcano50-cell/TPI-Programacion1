# TPI Rodrigo Carcano - Programación 1 (UTN)
# Programa de consola que lee datos de países desde un archivo CSV
# y permite buscarlos, filtrarlos, ordenarlos y ver estadísticas.

import csv
import os


# ---------------------------------------------------------------
# Carga de datos
# ---------------------------------------------------------------

def cargar_datos_csv(nombre_archivo):
    """Lee el archivo CSV y devuelve una lista de diccionarios, uno por país.
    Si una fila tiene población o superficie que no son números, se saltea."""
    lista_paises = []

    # Si el archivo no existe, aviso y devuelvo la lista vacía
    if not os.path.exists(nombre_archivo):
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
        return lista_paises

    archivo_csv = open(nombre_archivo, mode='r', encoding='utf-8')
    # DictReader usa la primera línea del CSV como nombres de las columnas
    lector_csv = csv.DictReader(archivo_csv)
    for registro in lector_csv:
        texto_poblacion = registro['poblacion'].strip()
        texto_superficie = registro['superficie'].strip()

        # Solo guardo el país si los dos valores numéricos son válidos
        if texto_poblacion.isdigit() and texto_superficie.isdigit():
            lista_paises.append({
                'nombre': registro['nombre'].strip(),
                'poblacion': int(texto_poblacion),
                'superficie': int(texto_superficie),
                'continente': registro['continente'].strip()
            })
        else:
            print("Error de formato en una línea del CSV. Registro omitido.")
    archivo_csv.close()

    return lista_paises


# ---------------------------------------------------------------
# Funciones para pedir datos al usuario (con validación)
# ---------------------------------------------------------------

def solicitar_entero_positivo(texto_pregunta):
    """Pide un número entero positivo y repite la pregunta hasta que sea válido."""
    while True:
        dato_ingresado = input(texto_pregunta).strip()
        # isdigit() solo da True si son todos dígitos (sin letras, signos ni decimales)
        if dato_ingresado.isdigit():
            return int(dato_ingresado)
        print("Los datos ingresados son inválidos. Ingrese un número entero positivo.")


def solicitar_opcion(texto_pregunta, opciones_validas):
    """Pide una opción y repite la pregunta hasta que esté dentro de opciones_validas."""
    while True:
        eleccion = input(texto_pregunta).strip()
        if eleccion in opciones_validas:
            return eleccion
        print("Los datos ingresados son inválidos. Intente nuevamente.")


def solicitar_rango(texto_minimo, texto_maximo):
    """Pide un mínimo y un máximo. Si el mínimo es mayor que el máximo, vuelve a pedir los dos."""
    while True:
        valor_minimo = solicitar_entero_positivo(texto_minimo)
        valor_maximo = solicitar_entero_positivo(texto_maximo)
        if valor_minimo <= valor_maximo:
            return valor_minimo, valor_maximo
        print("Los datos ingresados son inválidos. El mínimo no puede ser mayor que el máximo.")


# ---------------------------------------------------------------
# Funcionalidades del menú
# ---------------------------------------------------------------

def mostrar_paises(paises_a_mostrar):
    """Muestra por pantalla los datos de cada país de la lista."""
    if not paises_a_mostrar:
        print("No hay países para mostrar.")
        return
    for pais in paises_a_mostrar:
        print(f"Nombre: {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}")


def buscar_pais(lista_paises):
    """Busca países cuyo nombre contenga el texto ingresado (no distingue mayúsculas)."""
    # No dejo que el usuario busque con el texto vacío
    while True:
        texto_buscado = input("Ingrese el nombre del país a buscar: ").strip().lower()
        if texto_buscado:
            break
        print("Los datos ingresados son inválidos. El nombre no puede estar vacío.")

    # Coincidencia parcial: "arg" encuentra "Argentina"
    coincidencias = [pais for pais in lista_paises if texto_buscado in pais['nombre'].lower()]
    mostrar_paises(coincidencias)


def filtrar_paises(lista_paises):
    """Filtra los países por continente, por rango de población o por rango de superficie."""
    print("1. Por Continente\n2. Por Rango de Población\n3. Por Rango de Superficie")
    tipo_filtro = solicitar_opcion("Seleccione filtro (1-3): ", ["1", "2", "3"])

    if tipo_filtro == "1":
        # Armo un conjunto con los continentes que hay en el CSV para validar lo ingresado
        continentes_disponibles = {pais['continente'].lower() for pais in lista_paises}
        while True:
            continente_elegido = input("Ingrese continente: ").strip().lower()
            if continente_elegido in continentes_disponibles:
                break
            print("Los datos ingresados son inválidos. Ese continente no existe en los datos.")
        paises_filtrados = [pais for pais in lista_paises if pais['continente'].lower() == continente_elegido]
    elif tipo_filtro == "2":
        poblacion_minima, poblacion_maxima = solicitar_rango("Población mínima: ", "Población máxima: ")
        paises_filtrados = [pais for pais in lista_paises if poblacion_minima <= pais['poblacion'] <= poblacion_maxima]
    else:
        superficie_minima, superficie_maxima = solicitar_rango("Superficie mínima: ", "Superficie máxima: ")
        paises_filtrados = [pais for pais in lista_paises if superficie_minima <= pais['superficie'] <= superficie_maxima]

    mostrar_paises(paises_filtrados)


def ordenar_paises(lista_paises):
    """Ordena los países por nombre, población o superficie, en forma ascendente o descendente."""
    print("1. Por Nombre\n2. Por Población\n3. Por Superficie")
    campo_elegido = solicitar_opcion("Seleccione criterio (1-3): ", ["1", "2", "3"])
    # Relaciono cada opción del menú con la clave del diccionario por la que se ordena
    campos_orden = {"1": "nombre", "2": "poblacion", "3": "superficie"}

    print("1. Ascendente\n2. Descendente")
    tipo_orden = solicitar_opcion("Seleccione sentido (1-2): ", ["1", "2"])

    es_descendente = tipo_orden == "2"
    # sorted() devuelve una lista nueva, así no se modifica el orden original
    paises_ordenados = sorted(lista_paises, key=lambda pais: pais[campos_orden[campo_elegido]], reverse=es_descendente)
    mostrar_paises(paises_ordenados)


def mostrar_estadisticas(lista_paises):
    """Muestra el país más y menos poblado, los promedios y la cantidad de países por continente."""
    if not lista_paises:
        print("No hay datos.")
        return

    pais_mas_poblado = max(lista_paises, key=lambda pais: pais['poblacion'])
    pais_menos_poblado = min(lista_paises, key=lambda pais: pais['poblacion'])
    promedio_poblacion = sum(pais['poblacion'] for pais in lista_paises) / len(lista_paises)
    promedio_superficie = sum(pais['superficie'] for pais in lista_paises) / len(lista_paises)

    # Cuento cuántos países hay en cada continente usando un diccionario
    paises_por_continente = {}
    for pais in lista_paises:
        paises_por_continente[pais['continente']] = paises_por_continente.get(pais['continente'], 0) + 1

    print(f"País con mayor población: {pais_mas_poblado['nombre']} ({pais_mas_poblado['poblacion']})")
    print(f"País con menor población: {pais_menos_poblado['nombre']} ({pais_menos_poblado['poblacion']})")
    print(f"Promedio de población: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f}")
    print("Cantidad de países por continente:")
    for nombre_continente, cantidad in paises_por_continente.items():
        print(f" - {nombre_continente}: {cantidad}")


# ---------------------------------------------------------------
# Menú principal
# ---------------------------------------------------------------

def menu():
    """Carga los datos y muestra el menú hasta que el usuario elija salir."""
    lista_paises = cargar_datos_csv("paises.csv")
    # Si no se pudo cargar ningún país, no tiene sentido seguir
    if not lista_paises:
        return

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Buscar país por nombre")
        print("2. Filtrar países")
        print("3. Ordenar países")
        print("4. Mostrar estadísticas")
        print("5. Salir")

        opcion_menu = solicitar_opcion("Opción: ", ["1", "2", "3", "4", "5"])
        if opcion_menu == "1":
            buscar_pais(lista_paises)
        elif opcion_menu == "2":
            filtrar_paises(lista_paises)
        elif opcion_menu == "3":
            ordenar_paises(lista_paises)
        elif opcion_menu == "4":
            mostrar_estadisticas(lista_paises)
        else:
            break


# El menú se ejecuta solo si se corre este archivo directamente
if __name__ == "__main__":
    menu()
