import sys
import time

def convertir_a_binario_hexadecimal(datos):
    """
    Convertir los números a binario y hexadecimal.

    Args:
        datos (list): Lista de números.

    Returns:
        tuple: Tupla que contiene listas con los resultados binarios y hexadecimales.
    """
    resultados_binarios = []
    resultados_hexadecimales = []

    for item in datos:
        try:
            num = int(item)
            resultados_binarios.append(bin(num)[2:])  # Eliminar el prefijo '0b'
            resultados_hexadecimales.append(hex(num)[2:])  # Eliminar el prefijo '0x'
        except ValueError:
            print(f"Error: No se pudo convertir '{item}' a un número")

    return resultados_binarios, resultados_hexadecimales

def procesar_archivo(ruta_archivo):
    """
    Leer datos desde un archivo.

    Args:
        ruta_archivo (str): Ruta al archivo de entrada.

    Returns:
        list: Lista de datos leídos desde el archivo.
    """
    try:
        with open(ruta_archivo, 'r') as archivo:
            datos = [linea.strip() for linea in archivo]
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None

    return datos

def escribir_resultados_a_archivo(resultados_binarios, resultados_hexadecimales):
    """
    Escribir resultados a un archivo.

    Args:
        resultados_binarios (list): Lista de resultados binarios.
        resultados_hexadecimales (list): Lista de resultados hexadecimales.
    """
    with open("ResultadosConversion.txt", 'w') as archivo_resultados:
        archivo_resultados.write("Resultados Binarios:\n")
        archivo_resultados.write("\n".join(resultados_binarios) + "\n\n")
        archivo_resultados.write("Resultados Hexadecimales:\n")
        archivo_resultados.write("\n".join(resultados_hexadecimales) + "\n")

def convertir_numeros(ruta_archivo):
    """
    Realizar la conversión de números y mostrar resultados.

    Args:
        ruta_archivo (str): Ruta al archivo de entrada.
    """
    tiempo_inicio = time.time()

    datos = procesar_archivo(ruta_archivo)

    if datos is None:
        return

    resultados_binarios, resultados_hexadecimales = convertir_a_binario_hexadecimal(datos)

    tiempo_transcurrido = time.time() - tiempo_inicio

    print("Resultados Binarios:")
    print("\n".join(resultados_binarios))
    print("\nResultados Hexadecimales:")
    print("\n".join(resultados_hexadecimales))
    print(f"Tiempo Transcurrido: {tiempo_transcurrido:.6f} segundos")

    escribir_resultados_a_archivo(resultados_binarios, resultados_hexadecimales)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python convertirNumeros.py archivoConDatos.txt")
    else:
        convertir_numeros(sys.argv[1])
