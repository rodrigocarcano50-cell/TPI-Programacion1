import csv
import re
import unicodedata


# ---------------------------------------------------------------------------
# Carga de datos
# ---------------------------------------------------------------------------

def cargar_datos_csv(ruta_archivo):
    """Lee el CSV de países y devuelve una lista de diccionarios.
    Las filas mal formadas se informan y se omiten; si el archivo falla, devuelve []."""
    paises = []
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    poblacion = int(fila['poblacion'].strip())
                    superficie = int(fila['superficie'].strip())
                    if poblacion < 0 or superficie < 0:
                        print(f"Error en la línea {lector.line_num}: los valores no pueden ser negativos. Registro omitido.")
                        continue
                    paises.append({
                        'nombre': fila['nombre'].strip(),
                        'poblacion': poblacion,
                        'superficie': superficie,
                        'continente': fila['continente'].strip()
                    })
                except KeyError as e:
                    print(f"Error en la línea {lector.line_num}: falta la columna {e}. Registro omitido.")
                except ValueError:
                    print(f"Error en la línea {lector.line_num}: población o superficie no es un entero válido. Registro omitido.")
                except AttributeError:
                    # Una fila con menos campos deja valores en None, y None no tiene .strip()
                    print(f"Error en la línea {lector.line_num}: faltan datos en la fila. Registro omitido.")
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{ruta_archivo}'.")
        return []
    except UnicodeDecodeError:
        print(f"Error: el archivo '{ruta_archivo}' no está en UTF-8.")
        return []

    if not paises:
        print("Error: no hay países válidos para cargar.")
    return paises


# ---------------------------------------------------------------------------
# Entrada y salida
# ---------------------------------------------------------------------------

def solicitar_entero_positivo(mensaje):
    """Pide un número por teclado hasta que sea un entero mayor o igual a 0 y lo devuelve."""
    while True:
        entrada = input(mensaje).strip()
        # Un "-" inicial es un negativo: se valida aparte para dar el mensaje específico
        if re.fullmatch(r"-\d+", entrada):
            print("Entrada inválida. El número no puede ser negativo.")
            continue
        # Solo dígitos: rechaza "+5" o "1_000" (que int() aceptaría) y "1.5"
        if not re.fullmatch(r"\d+", entrada):
            print("Entrada inválida. Ingrese un número entero positivo.")
            continue
        try:
            return int(entrada)
        except ValueError:
            # Respaldo por si int() no puede convertir algún dígito aceptado por \d
            print("Entrada inválida. Ingrese un número entero positivo.")


def mostrar_paises(lista):
    """Imprime los países de la lista, uno por línea. No devuelve nada."""
    if not lista:
        print("No hay países para mostrar.")
        return
    for p in lista:
        print(f"Nombre: {p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km² | Continente: {p['continente']}")


# ---------------------------------------------------------------------------
# Lógica (no pide datos ni imprime)
# ---------------------------------------------------------------------------

def normalizar_texto(texto):
    """Devuelve el texto en minúsculas y sin acentos, para comparar sin distinguirlos.
    Ejemplo: 'Japón' -> 'japon'."""
    # NFD separa cada letra de su acento; los acentos quedan como caracteres de categoría Mn
    descompuesto = unicodedata.normalize('NFD', texto)
    sin_acentos = ''.join(c for c in descompuesto if unicodedata.category(c) != 'Mn')
    return sin_acentos.lower()


def buscar_por_nombre(paises, texto):
    """Devuelve los países cuyo nombre contiene el texto, sin distinguir mayúsculas ni acentos."""
    texto = normalizar_texto(texto)
    return [p for p in paises if texto in normalizar_texto(p['nombre'])]


def filtrar_por_continente(paises, continente):
    """Devuelve los países del continente indicado, sin distinguir mayúsculas ni acentos."""
    continente = normalizar_texto(continente)
    return [p for p in paises if normalizar_texto(p['continente']) == continente]


def filtrar_por_rango(paises, clave, minimo, maximo):
    """Devuelve los países cuyo valor en 'clave' está entre minimo y maximo (incluidos)."""
    return [p for p in paises if minimo <= p[clave] <= maximo]


def ordenar_lista(paises, clave, descendente):
    """Devuelve una lista nueva con los países ordenados por 'clave'."""
    # key=lambda indica a sorted qué campo de cada diccionario comparar
    return sorted(paises, key=lambda x: x[clave], reverse=descendente)


def calcular_estadisticas(paises):
    """Devuelve un diccionario con mayor y menor población, promedios y conteo por continente."""
    # max/min comparan los diccionarios usando solo el campo 'poblacion'
    mayor_pob = max(paises, key=lambda x: x['poblacion'])
    menor_pob = min(paises, key=lambda x: x['poblacion'])
    prom_pob = sum(x['poblacion'] for x in paises) / len(paises)
    prom_sup = sum(x['superficie'] for x in paises) / len(paises)

    conteo_cont = {}
    for p in paises:
        # get(..., 0) arranca en 0 la primera vez que aparece un continente
        conteo_cont[p['continente']] = conteo_cont.get(p['continente'], 0) + 1

    return {
        'mayor_pob': mayor_pob,
        'menor_pob': menor_pob,
        'prom_pob': prom_pob,
        'prom_sup': prom_sup,
        'conteo_cont': conteo_cont,
    }


# ---------------------------------------------------------------------------
# Interfaz (pide datos y muestra resultados)
# ---------------------------------------------------------------------------

def solicitar_opcion(mensaje, opciones_validas, mensaje_error):
    """Pide una opción hasta que esté en opciones_validas y la devuelve."""
    while True:
        opcion = input(mensaje).strip()
        if opcion in opciones_validas:
            return opcion
        print(mensaje_error)


def solicitar_texto(mensaje):
    """Pide un texto hasta que no esté vacío y lo devuelve."""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Entrada inválida. No puede quedar vacía.")


def pedir_rango(etiqueta):
    """Pide un mínimo y un máximo hasta que el mínimo no supere al máximo. Devuelve (min, max)."""
    while True:
        minimo = solicitar_entero_positivo(f"{etiqueta} mínima: ")
        maximo = solicitar_entero_positivo(f"{etiqueta} máxima: ")
        if minimo <= maximo:
            return minimo, maximo
        print("Error: el valor mínimo no puede ser mayor que el máximo.")


def buscar_pais(paises):
    """Pide un nombre, busca coincidencias parciales y las muestra."""
    nombre = solicitar_texto("Ingrese el nombre del país a buscar: ")
    resultados = buscar_por_nombre(paises, nombre)
    if not resultados:
        print(f"No se encontró ningún país que coincida con '{nombre}'.")
        return
    mostrar_paises(resultados)


def filtrar_paises(paises):
    """Pide un tipo de filtro y sus datos, y muestra los países que lo cumplen."""
    print("1. Por Continente\n2. Por Rango de Población\n3. Por Rango de Superficie")
    opcion = solicitar_opcion("Seleccione filtro (1-3): ", ["1", "2", "3"], "Opción inválida.")

    if opcion == "1":
        cont = solicitar_texto("Ingrese continente: ")
        resultados = filtrar_por_continente(paises, cont)
    elif opcion == "2":
        minimo, maximo = pedir_rango("Población")
        resultados = filtrar_por_rango(paises, 'poblacion', minimo, maximo)
    else:
        minimo, maximo = pedir_rango("Superficie")
        resultados = filtrar_por_rango(paises, 'superficie', minimo, maximo)

    mostrar_paises(resultados)


def ordenar_paises(paises):
    """Pide criterio y sentido de orden, y muestra la lista ordenada."""
    mapa = {"1": "nombre", "2": "poblacion", "3": "superficie"}
    print("1. Por Nombre\n2. Por Población\n3. Por Superficie")
    criterio = solicitar_opcion("Seleccione criterio (1-3): ", mapa, "Criterio inválido.")

    print("1. Ascendente\n2. Descendente")
    sentido = solicitar_opcion("Seleccione sentido (1-2): ", ["1", "2"], "Sentido inválido.")

    mostrar_paises(ordenar_lista(paises, mapa[criterio], sentido == "2"))


def mostrar_estadisticas(paises):
    """Calcula e imprime las estadísticas generales de los países."""
    if not paises:
        print("No hay datos.")
        return

    est = calcular_estadisticas(paises)
    print(f"País con mayor población: {est['mayor_pob']['nombre']} ({est['mayor_pob']['poblacion']})")
    print(f"País con menor población: {est['menor_pob']['nombre']} ({est['menor_pob']['poblacion']})")
    print(f"Promedio de población: {est['prom_pob']:.2f}")
    print(f"Promedio de superficie: {est['prom_sup']:.2f}")
    print("Cantidad de países por continente:")
    for c, cant in est['conteo_cont'].items():
        print(f" - {c}: {cant}")


def menu():
    """Carga los datos y muestra el menú principal hasta que el usuario elige salir."""
    paises = cargar_datos_csv("paises.csv")
    if not paises:
        return

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Buscar país por nombre")
        print("2. Filtrar países")
        print("3. Ordenar países")
        print("4. Mostrar estadísticas")
        print("5. Salir")

        op = input("Opción: ").strip()
        if op == "1":
            buscar_pais(paises)
        elif op == "2":
            filtrar_paises(paises)
        elif op == "3":
            ordenar_paises(paises)
        elif op == "4":
            mostrar_estadisticas(paises)
        elif op == "5":
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
