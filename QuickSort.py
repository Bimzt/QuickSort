import random
def generate_random_numbers():
    numbers = []
    for i in range(100):
        data = random.randint(0, 9)
        numbers.append(data)
    return numbers

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    data = generate_random_numbers()
    print("Data:")
    print(', '.join(map(str, data)))
    sorted_data = quicksort(data)
    print("\nData setelah diurutkan:")
    print(', '.join(map(str, sorted_data)))
    print(f"\nJumlah elemen: {len(sorted_data)}")

"""
Alasan memilih algoritma Quicksort:
1. Quicksort memiliki kompleksitas waktu O(n log n), yang sangat efisien untuk data berukuran besar.
2. Quicksort dapat dijadikan sebagai algoritma in-place yang menggunakan sedikit memori.
3. Meskipun kompleksitas waktu terburuknya adalah O(n²), Quicksort umumnya memiliki kinerja yang sangat baik dalam praktiknya.
4. Quicksort bekerja dengan baik untuk berbagai jenis data dan dapat dioptimalkan untuk kasus-kasus spesifik.
5. Algoritma ini cukup mudah dipakai dalam program.
"""