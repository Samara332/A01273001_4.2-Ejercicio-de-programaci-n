import sys
import time

def count_word_frequency(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None

    word_frequency = {}
    for word in words:
        word = word.lower()
        word_frequency[word] = word_frequency.get(word, 0) + 1

    return word_frequency

def write_results_to_file(word_frequency):
    with open("WordCountResults.txt", 'w') as result_file:
        result_file.write("Word\tFrequency\n")
        for word, frequency in word_frequency.items():
            result_file.write(f"{word}\t{frequency}\n")

def word_count(file_path):
    start_time = time.time()

    word_frequency = count_word_frequency(file_path)

    if word_frequency is None:
        return

    elapsed_time = time.time() - start_time

    print("Word\tFrequency")
    for word, frequency in word_frequency.items():
        print(f"{word}\t{frequency}")

    print(f"Time Elapsed: {elapsed_time:.6f} seconds")

    write_results_to_file(word_frequency)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
    else:
        word_count(sys.argv[1])
