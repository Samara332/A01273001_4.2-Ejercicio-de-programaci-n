import sys
import time

def contar_frecuencia_palabras(ruta_archivo):
    """
    Contar la frecuencia de cada palabra distinta en el archivo.

    Args:
        ruta_archivo (str): Ruta al archivo de entrada.

    Returns:
        dict: Diccionario que contiene las frecuencias de las palabras.
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            palabras = archivo.read().split()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None

    frecuencia_palabras = {}
    for palabra in palabras:
        # Convertir la palabra a minúsculas para contar de manera insensible a mayúsculas
        palabra = palabra.lower()
        frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1

    return frecuencia_palabras

def escribir_resultados_a_archivo(frecuencia_palabras):
    """
    Escribir frecuencias de palabras a un archivo.

    Args:
        frecuencia_palabras (dict): Diccionario que contiene las frecuencias de las palabras.
    """
    with open("ResultadosConteoPalabras.txt", 'w', encoding='utf-8') as archivo_resultados:
        archivo_resultados.write("Palabra\tFrecuencia\n")
        for palabra, frecuencia in frecuencia_palabras.items():
            archivo_resultados.write(f"{palabra}\t{frecuencia}\n")

def conteo_palabras(ruta_archivo):
    """
    Realizar el conteo de palabras y mostrar los resultados.

    Args:
        ruta_archivo (str): Ruta al archivo de entrada.
    """
    tiempo_inicio = time.time()

    frecuencia_palabras = contar_frecuencia_palabras(ruta_archivo)

    if frecuencia_palabras is None:
        return

    tiempo_transcurrido = time.time() - tiempo_inicio

    print("Palabra\tFrecuencia")
    for palabra, frecuencia in frecuencia_palabras.items():
        print(f"{palabra}\t{frecuencia}")

    print(f"Tiempo transcurrido: {tiempo_transcurrido:.6f} segundos")

    escribir_resultados_a_archivo(frecuencia_palabras)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python conteo_palabras.py archivoConDatos.txt")
    else:
        conteo_palabras(sys.argv[1])
