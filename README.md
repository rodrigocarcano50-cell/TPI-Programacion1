# Gestión de Datos de Países en Python

Trabajo Práctico Integrador de Programación 1. Autor: Rodrigo Carcano.

## Descripción

Programa de consola en Python que lee el archivo `paises.csv` y permite buscar países por nombre, filtrarlos, ordenarlos y ver estadísticas generales. La búsqueda y el filtro por continente no distinguen mayúsculas ni acentos. Los errores del archivo y de las entradas del usuario se manejan con `try/except`.

## Requisitos

- Python 3.x.
- Solo se usa la biblioteca estándar (`csv`, `re` y `unicodedata`). No hace falta instalar nada.

## Instrucciones de uso

1. Abrir una terminal en la carpeta que contiene `main.py` y `paises.csv`.
2. Ejecutar:

```bash
python main.py
```

3. Elegir una opción del menú escribiendo su número y presionando Enter:

```
--- MENÚ PRINCIPAL ---
1. Buscar país por nombre
2. Filtrar países
3. Ordenar países
4. Mostrar estadísticas
5. Salir
Opción:
```

## Datos de ejemplo

El archivo `paises.csv` tiene 7 registros:

| Nombre | Población | Superficie (km²) | Continente |
|---|---|---|---|
| Argentina | 45376763 | 2780400 | América |
| Japón | 125800000 | 377975 | Asia |
| Brasil | 213993437 | 8515767 | América |
| Alemania | 83149300 | 357022 | Europa |
| Australia | 25687041 | 7692024 | Oceanía |
| Francia | 68170228 | 551695 | Europa |
| España | 47415750 | 505990 | Europa |

## Ejemplos de entrada y salida

Las salidas corresponden al `paises.csv` del repositorio (7 registros). Lo que aparece después de `Opción:`, `Seleccione ...:`, `Ingrese ...:` y de las preguntas de mínimo y máximo es lo que escribe el usuario.

### 1. Buscar país por nombre

Nombre que existe:

```
Opción: 1
Ingrese el nombre del país a buscar: Argentina
Nombre: Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: América
```

Sin acento ni mayúscula:

```
Opción: 1
Ingrese el nombre del país a buscar: japon
Nombre: Japón | Población: 125800000 | Superficie: 377975 km² | Continente: Asia
```

Nombre que no existe:

```
Opción: 1
Ingrese el nombre del país a buscar: Egipto
No se encontró ningún país que coincida con 'Egipto'.
```

### 2. Filtrar por continente

```
Opción: 2
1. Por Continente
2. Por Rango de Población
3. Por Rango de Superficie
Seleccione filtro (1-3): 1
Ingrese continente: Europa
Nombre: Alemania | Población: 83149300 | Superficie: 357022 km² | Continente: Europa
Nombre: Francia | Población: 68170228 | Superficie: 551695 km² | Continente: Europa
Nombre: España | Población: 47415750 | Superficie: 505990 km² | Continente: Europa
```

Sin acento ni mayúscula:

```
Opción: 2
1. Por Continente
2. Por Rango de Población
3. Por Rango de Superficie
Seleccione filtro (1-3): 1
Ingrese continente: america
Nombre: Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: América
Nombre: Brasil | Población: 213993437 | Superficie: 8515767 km² | Continente: América
```

### 3. Filtrar por rango de población

```
Opción: 2
1. Por Continente
2. Por Rango de Población
3. Por Rango de Superficie
Seleccione filtro (1-3): 2
Población mínima: 10000000
Población máxima: 100000000
Nombre: Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: América
Nombre: Alemania | Población: 83149300 | Superficie: 357022 km² | Continente: Europa
Nombre: Australia | Población: 25687041 | Superficie: 7692024 km² | Continente: Oceanía
Nombre: Francia | Población: 68170228 | Superficie: 551695 km² | Continente: Europa
Nombre: España | Población: 47415750 | Superficie: 505990 km² | Continente: Europa
```

### 4. Filtrar por rango de superficie

```
Opción: 2
1. Por Continente
2. Por Rango de Población
3. Por Rango de Superficie
Seleccione filtro (1-3): 3
Superficie mínima: 1000000
Superficie máxima: 8000000
Nombre: Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: América
Nombre: Australia | Población: 25687041 | Superficie: 7692024 km² | Continente: Oceanía
```

### 5. Ordenar por nombre (ascendente)

```
Opción: 3
1. Por Nombre
2. Por Población
3. Por Superficie
Seleccione criterio (1-3): 1
1. Ascendente
2. Descendente
Seleccione sentido (1-2): 1
Nombre: Alemania | Población: 83149300 | Superficie: 357022 km² | Continente: Europa
Nombre: Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: América
Nombre: Australia | Población: 25687041 | Superficie: 7692024 km² | Continente: Oceanía
Nombre: Brasil | Población: 213993437 | Superficie: 8515767 km² | Continente: América
Nombre: España | Población: 47415750 | Superficie: 505990 km² | Continente: Europa
Nombre: Francia | Población: 68170228 | Superficie: 551695 km² | Continente: Europa
Nombre: Japón | Población: 125800000 | Superficie: 377975 km² | Continente: Asia
```

### 6. Ordenar por nombre (descendente)

```
Opción: 3
1. Por Nombre
2. Por Población
3. Por Superficie
Seleccione criterio (1-3): 1
1. Ascendente
2. Descendente
Seleccione sentido (1-2): 2
Nombre: Japón | Población: 125800000 | Superficie: 377975 km² | Continente: Asia
Nombre: Francia | Población: 68170228 | Superficie: 551695 km² | Continente: Europa
Nombre: España | Población: 47415750 | Superficie: 505990 km² | Continente: Europa
Nombre: Brasil | Población: 213993437 | Superficie: 8515767 km² | Continente: América
Nombre: Australia | Población: 25687041 | Superficie: 7692024 km² | Continente: Oceanía
Nombre: Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: América
Nombre: Alemania | Población: 83149300 | Superficie: 357022 km² | Continente: Europa
```

### 7. Ordenar por población (ascendente)

```
Opción: 3
1. Por Nombre
2. Por Población
3. Por Superficie
Seleccione criterio (1-3): 2
1. Ascendente
2. Descendente
Seleccione sentido (1-2): 1
Nombre: Australia | Población: 25687041 | Superficie: 7692024 km² | Continente: Oceanía
Nombre: Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: América
Nombre: España | Población: 47415750 | Superficie: 505990 km² | Continente: Europa
Nombre: Francia | Población: 68170228 | Superficie: 551695 km² | Continente: Europa
Nombre: Alemania | Población: 83149300 | Superficie: 357022 km² | Continente: Europa
Nombre: Japón | Población: 125800000 | Superficie: 377975 km² | Continente: Asia
Nombre: Brasil | Población: 213993437 | Superficie: 8515767 km² | Continente: América
```

### 8. Ordenar por población (descendente)

```
Opción: 3
1. Por Nombre
2. Por Población
3. Por Superficie
Seleccione criterio (1-3): 2
1. Ascendente
2. Descendente
Seleccione sentido (1-2): 2
Nombre: Brasil | Población: 213993437 | Superficie: 8515767 km² | Continente: América
Nombre: Japón | Población: 125800000 | Superficie: 377975 km² | Continente: Asia
Nombre: Alemania | Población: 83149300 | Superficie: 357022 km² | Continente: Europa
Nombre: Francia | Población: 68170228 | Superficie: 551695 km² | Continente: Europa
Nombre: España | Población: 47415750 | Superficie: 505990 km² | Continente: Europa
Nombre: Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: América
Nombre: Australia | Población: 25687041 | Superficie: 7692024 km² | Continente: Oceanía
```

### 9. Ordenar por superficie (ascendente)

```
Opción: 3
1. Por Nombre
2. Por Población
3. Por Superficie
Seleccione criterio (1-3): 3
1. Ascendente
2. Descendente
Seleccione sentido (1-2): 1
Nombre: Alemania | Población: 83149300 | Superficie: 357022 km² | Continente: Europa
Nombre: Japón | Población: 125800000 | Superficie: 377975 km² | Continente: Asia
Nombre: España | Población: 47415750 | Superficie: 505990 km² | Continente: Europa
Nombre: Francia | Población: 68170228 | Superficie: 551695 km² | Continente: Europa
Nombre: Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: América
Nombre: Australia | Población: 25687041 | Superficie: 7692024 km² | Continente: Oceanía
Nombre: Brasil | Población: 213993437 | Superficie: 8515767 km² | Continente: América
```

### 10. Ordenar por superficie (descendente)

```
Opción: 3
1. Por Nombre
2. Por Población
3. Por Superficie
Seleccione criterio (1-3): 3
1. Ascendente
2. Descendente
Seleccione sentido (1-2): 2
Nombre: Brasil | Población: 213993437 | Superficie: 8515767 km² | Continente: América
Nombre: Australia | Población: 25687041 | Superficie: 7692024 km² | Continente: Oceanía
Nombre: Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: América
Nombre: Francia | Población: 68170228 | Superficie: 551695 km² | Continente: Europa
Nombre: España | Población: 47415750 | Superficie: 505990 km² | Continente: Europa
Nombre: Japón | Población: 125800000 | Superficie: 377975 km² | Continente: Asia
Nombre: Alemania | Población: 83149300 | Superficie: 357022 km² | Continente: Europa
```

### 11. Mostrar estadísticas

```
Opción: 4
País con mayor población: Brasil (213993437)
País con menor población: Australia (25687041)
Promedio de población: 87084645.57
Promedio de superficie: 2968696.14
Cantidad de países por continente:
 - América: 2
 - Asia: 1
 - Europa: 3
 - Oceanía: 1
```

## Manejo de errores

Ante un dato inválido, el programa muestra un mensaje y vuelve a hacer la misma pregunta, sin volver al menú.

### Mínimo mayor que máximo

Se vuelven a pedir el mínimo y el máximo:

```
Opción: 2
1. Por Continente
2. Por Rango de Población
3. Por Rango de Superficie
Seleccione filtro (1-3): 2
Población mínima: 100
Población máxima: 50
Error: el valor mínimo no puede ser mayor que el máximo.
Población mínima: 10000000
Población máxima: 30000000
Nombre: Australia | Población: 25687041 | Superficie: 7692024 km² | Continente: Oceanía
```

### Entradas no numéricas

Solo se aceptan enteros escritos con dígitos, sin signo:

```
Opción: 2
1. Por Continente
2. Por Rango de Población
3. Por Rango de Superficie
Seleccione filtro (1-3): 2
Población mínima: abc
Entrada inválida. Ingrese un número entero positivo.
Población mínima: -3
Entrada inválida. El número no puede ser negativo.
Población mínima: +5
Entrada inválida. Ingrese un número entero positivo.
Población mínima: 1_000
Entrada inválida. Ingrese un número entero positivo.
Población mínima: 1.5
Entrada inválida. Ingrese un número entero positivo.
Población mínima: 10000000
Población máxima: 30000000
Nombre: Australia | Población: 25687041 | Superficie: 7692024 km² | Continente: Oceanía
```

### Opción de filtro inválida y continente vacío

```
Opción: 2
1. Por Continente
2. Por Rango de Población
3. Por Rango de Superficie
Seleccione filtro (1-3): 7
Opción inválida.
Seleccione filtro (1-3): x
Opción inválida.
Seleccione filtro (1-3): 1
Ingrese continente: 
Entrada inválida. No puede quedar vacía.
Ingrese continente: Europa
Nombre: Alemania | Población: 83149300 | Superficie: 357022 km² | Continente: Europa
Nombre: Francia | Población: 68170228 | Superficie: 551695 km² | Continente: Europa
Nombre: España | Población: 47415750 | Superficie: 505990 km² | Continente: Europa
```

### Criterio y sentido de orden inválidos

```
Opción: 3
1. Por Nombre
2. Por Población
3. Por Superficie
Seleccione criterio (1-3): 9
Criterio inválido.
Seleccione criterio (1-3): 2
1. Ascendente
2. Descendente
Seleccione sentido (1-2): 5
Sentido inválido.
Seleccione sentido (1-2): 1
Nombre: Australia | Población: 25687041 | Superficie: 7692024 km² | Continente: Oceanía
Nombre: Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: América
Nombre: España | Población: 47415750 | Superficie: 505990 km² | Continente: Europa
Nombre: Francia | Población: 68170228 | Superficie: 551695 km² | Continente: Europa
Nombre: Alemania | Población: 83149300 | Superficie: 357022 km² | Continente: Europa
Nombre: Japón | Población: 125800000 | Superficie: 377975 km² | Continente: Asia
Nombre: Brasil | Población: 213993437 | Superficie: 8515767 km² | Continente: América
```

### Rango sin resultados

```
Opción: 2
1. Por Continente
2. Por Rango de Población
3. Por Rango de Superficie
Seleccione filtro (1-3): 3
Superficie mínima: 0
Superficie máxima: 10
No hay países para mostrar.
```

### Opción de menú inválida

```
Opción: 9
Opción inválida.
```

Después del mensaje, el programa vuelve a mostrar el menú.

### Archivo inexistente

Si `paises.csv` no está en la carpeta, el programa termina con:

```
Error: no se encontró el archivo 'paises.csv'.
```

### CSV con filas mal formadas

En una copia de `paises.csv` se agregaron estas tres filas al final (líneas 9 a 11 del archivo):

```
Chile,abc,756102,América
Perú,33000000
Canadá,-5,9984670,América
```

El programa informa cada una y carga normalmente los otros 7 países:

```
Error en la línea 9: población o superficie no es un entero válido. Registro omitido.
Error en la línea 10: faltan datos en la fila. Registro omitido.
Error en la línea 11: los valores no pueden ser negativos. Registro omitido.
```

Si ninguna fila es válida, el programa además muestra `Error: no hay países válidos para cargar.` y termina.

## Formato del CSV

- Codificación UTF-8. Si no lo es, el programa muestra `Error: el archivo 'paises.csv' no está en UTF-8.`
- Primera línea con el encabezado `nombre,poblacion,superficie,continente`.
- `poblacion` y `superficie` deben ser enteros sin signo.
- El archivo debe terminar con un salto de línea. Si no, una fila agregada después queda pegada a la última.

## Participación de los integrantes

El trabajo fue realizado de forma individual por Rodrigo Carcano.
