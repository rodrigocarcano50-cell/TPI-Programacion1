# TPI Rodrigo Carcano

Trabajo Práctico Integrador de Programación 1 (UTN).

## ¿De qué se trata?

Es un programa de consola hecho en Python que lee un archivo `paises.csv` con datos de distintos países (nombre, población, superficie y continente) y permite consultarlos desde un menú. Con el programa se puede:

- Buscar un país por su nombre (también funciona escribiendo solo una parte, por ejemplo "arg").
- Filtrar los países por continente, por rango de población o por rango de superficie.
- Ordenar la lista por nombre, población o superficie, de menor a mayor o al revés.
- Ver estadísticas generales: el país más poblado, el menos poblado, los promedios y cuántos países hay en cada continente.

Si el usuario escribe algo que no corresponde (una letra donde va un número, una opción que no existe, un mínimo mayor que el máximo, etc.), el programa avisa que el dato es inválido y vuelve a hacer la misma pregunta, sin volver al menú principal.

## Cómo ejecutarlo

1. Tener instalado Python 3.
2. Dejar `main.py` y `paises.csv` en la misma carpeta.
3. Abrir una terminal en esa carpeta y correr:

```bash
python main.py
```

## Ejemplos de uso

### Buscar un país

```
Opción: 1
Ingrese el nombre del país a buscar: fra
Nombre: Francia | Población: 68170228 | Superficie: 551695 km² | Continente: Europa
```

### Filtrar por continente

```
Opción: 2
Seleccione filtro (1-3): 1
Ingrese continente: Europa
Nombre: Alemania | Población: 83149300 | Superficie: 357022 km² | Continente: Europa
Nombre: Francia | Población: 68170228 | Superficie: 551695 km² | Continente: Europa
Nombre: España | Población: 47415750 | Superficie: 505990 km² | Continente: Europa
```

### Filtrar por rango de población

```
Opción: 2
Seleccione filtro (1-3): 2
Población mínima: 10000000
Población máxima: 100000000
Nombre: Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: América
Nombre: Alemania | Población: 83149300 | Superficie: 357022 km² | Continente: Europa
Nombre: Australia | Población: 25687041 | Superficie: 7692024 km² | Continente: Oceanía
Nombre: Francia | Población: 68170228 | Superficie: 551695 km² | Continente: Europa
Nombre: España | Población: 47415750 | Superficie: 505990 km² | Continente: Europa
```

### Ordenar por superficie (de mayor a menor), con un error en el medio

```
Opción: 3
Seleccione criterio (1-3): 7
Los datos ingresados son inválidos. Intente nuevamente.
Seleccione criterio (1-3): 3
Seleccione sentido (1-2): 2
Nombre: Brasil | Población: 213993437 | Superficie: 8515767 km² | Continente: América
Nombre: Australia | Población: 25687041 | Superficie: 7692024 km² | Continente: Oceanía
Nombre: Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: América
Nombre: Francia | Población: 68170228 | Superficie: 551695 km² | Continente: Europa
Nombre: España | Población: 47415750 | Superficie: 505990 km² | Continente: Europa
Nombre: Japón | Población: 125800000 | Superficie: 377975 km² | Continente: Asia
Nombre: Alemania | Población: 83149300 | Superficie: 357022 km² | Continente: Europa
```

### Estadísticas

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
