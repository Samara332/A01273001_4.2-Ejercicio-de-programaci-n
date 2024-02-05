import sys
import time

def calcular_media(numbers):
    return sum(numbers) / len(numbers)

def calcular_mediana(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        middle1 = sorted_numbers[n // 2 - 1]
        middle2 = sorted_numbers[n // 2]
        return (middle1 + middle2) / 2
    else:
        return sorted_numbers[n // 2]

def calcular_moda(numbers):
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    mode = max(counts, key=counts.get)
    return mode

def calcular_varianza(numbers, mean):
    squared_diff = sum((x - mean) ** 2 for x in numbers)
    return squared_diff / len(numbers)

def calcular_desviacion_estandar(variance):
    return variance ** 0.5

def compute_statistics(file_path):
    try:
        with open(file_path, 'r') as file:
            data = []
            for line in file:
                try:
                    num = float(line.strip())
                    data.append(num)
                except ValueError:
                    print(f"Error: Could not convert string to float '{line.strip()}'")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    start_time = time.time()

    if not data:
        print("Error: No valid numeric data found in the file.")
        return

    mean = calcular_media(data)
    median = calcular_mediana(data)
    mode = calcular_moda(data)
    variance = calcular_varianza(data, mean)
    standard_deviation = calcular_desviacion_estandar(variance)

    elapsed_time = time.time() - start_time

    print(f"Media: {mean}")
    print(f"Mediana: {median}")
    print(f"Moda: {mode}")
    print(f"Varianza: {variance}")
    print(f"Desviacion estandar: {standard_deviation}")
    print(f"Tiempo de compilacion: {elapsed_time:.6f} segundos")

    with open("StatisticsResults.txt", 'w') as result_file:
        result_file.write(f"Media: {mean}\n")
        result_file.write(f"Mediana: {median}\n")
        result_file.write(f"Moda: {mode}\n")
        result_file.write(f"Varianza: {variance}\n")
        result_file.write(f"Desviacion estandar: {standard_deviation}\n")
        result_file.write(f"Tiempo de compilacion: {elapsed_time:.6f} segundos\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
    else:
        compute_statistics(sys.argv[1])
