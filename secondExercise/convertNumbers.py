import sys
import time

def convert_to_binary_and_hex(data):
    binary_results = []
    hex_results = []
    
    for item in data:
        try:
            num = int(item)
            binary_results.append(bin(num)[2:])  # Removing '0b' prefix
            hex_results.append(hex(num)[2:])  # Removing '0x' prefix
        except ValueError:
            print(f"Error: Could not convert '{item}' to a number")

    return binary_results, hex_results

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = [line.strip() for line in file]
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None

    return data

def write_results_to_file(binary_results, hex_results):
    with open("ConversionResults.txt", 'w') as result_file:
        result_file.write("Binary Results:\n")
        result_file.write("\n".join(binary_results) + "\n\n")
        result_file.write("Hexadecimal Results:\n")
        result_file.write("\n".join(hex_results) + "\n")

def convert_numbers(file_path):
    start_time = time.time()

    data = process_file(file_path)

    if data is None:
        return

    binary_results, hex_results = convert_to_binary_and_hex(data)

    elapsed_time = time.time() - start_time

    print("Binary Results:")
    print("\n".join(binary_results))
    print("\nHexadecimal Results:")
    print("\n".join(hex_results))
    print(f"Time Elapsed: {elapsed_time:.6f} seconds")

    write_results_to_file(binary_results, hex_results)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
    else:
        convert_numbers(sys.argv[1])
