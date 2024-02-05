import sys
import time

def calcular_media(numeros):
    """
    Calcular la media de una lista de números.

    Args:
        numeros (list): Lista de números.

    Returns:
        float: Valor de la media.
    """
    return sum(numeros) / len(numeros)

def calcular_mediana(numeros):
    """
    Calcular la mediana de una lista de números.

    Args:
        numeros (list): Lista de números.

    Returns:
        float: Valor de la mediana.
    """
    sorted_numbers = sorted(numeros)
    n = len(sorted_numbers)
    if n % 2 == 0:
        middle1 = sorted_numbers[n // 2 - 1]
        middle2 = sorted_numbers[n // 2]
        return (middle1 + middle2) / 2
    else:
        return sorted_numbers[n // 2]

def calcular_moda(numeros):
    """
    Calcular la moda de una lista de números.

    Args:
        numeros (list): Lista de números.

    Returns:
        float: Valor de la moda.
    """
    counts = {}
    for num in numeros:
        counts[num] = counts.get(num, 0) + 1
    moda = max(counts, key=counts.get)
    return moda

def calcular_varianza(numeros, media):
    """
    Calcular la varianza de una lista de números.

    Args:
        numeros (list): Lista de números.
        media (float): Valor de la media.

    Returns:
        float: Valor de la varianza.
    """
    squared_diff = sum((x - media) ** 2 for x in numeros)
    return squared_diff / len(numeros)

def calcular_desviacion_estandar(varianza):
    """
    Calcular la desviación estándar a partir de la varianza.

    Args:
        varianza (float): Valor de la varianza.

    Returns:
        float: Valor de la desviación estándar.
    """
    return varianza ** 0.5

def calcular_estadisticas_descriptivas(ruta_archivo):
    """
    Calcular estadísticas descriptivas a partir de un archivo de números.

    Args:
        ruta_archivo (str): Ruta al archivo con datos numéricos.
    """
    try:
        with open(ruta_archivo, 'r') as archivo:
            datos = [float(linea.strip()) for linea in archivo]
    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {e}")
        return

    tiempo_inicio = time.time()

    media = calcular_media(datos)
    mediana = calcular_mediana(datos)
    moda = calcular_moda(datos)
    varianza = calcular_varianza(datos, media)
    desviacion_estandar = calcular_desviacion_estandar(varianza)

    tiempo_transcurrido = time.time() - tiempo_inicio

    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")
    print(f"Varianza: {varianza}")
    print(f"Desviación Estándar: {desviacion_estandar}")
    print(f"Tiempo Transcurrido: {tiempo_transcurrido:.6f} segundos")

    with open("ResultadosEstadisticos.txt", 'w') as archivo_resultados:
        archivo_resultados.write(f"Media: {media}\n")
        archivo_resultados.write(f"Mediana: {mediana}\n")
        archivo_resultados.write(f"Moda: {moda}\n")
        archivo_resultados.write(f"Varianza: {varianza}\n")
        archivo_resultados.write(f"Desviación Estándar: {desviacion_estandar}\n")
        archivo_resultados.write(f"Tiempo Transcurrido: {tiempo_transcurrido:.6f} segundos\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python calcularEstadisticas.py archivoConDatos.txt")
    else:
        calcular_estadisticas_descriptivas(sys.argv[1])
