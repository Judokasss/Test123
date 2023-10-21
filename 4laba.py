class BinarySearch:
    def __init__(self, arr):
        self.arr = sorted(arr)

    def binary_search(self, key):
        left = 0
        right = len(self.arr) - 1
        positions = []

        while left <= right:
            mid = (left + right) // 2

            if self.arr[mid] == key:
                positions.append(mid)
                i = mid - 1
                while i >= 0 and self.arr[i] == key:  # Проверяем элементы влево
                    positions.append(i)
                    i -= 1
                i = mid + 1
                while i < len(self.arr) and self.arr[i] == key:  # Проверяем элементы вправо
                    positions.append(i)
                    i += 1
                break
            elif self.arr[mid] < key:
                left = mid + 1
            else:
                right = mid - 1

        return sorted(positions)  # Возвращаем отсортированный список позиций

def get_input():
    while True:
        try:
            n = int(input("Введите размер массива (целое положительное число от 1 до 100): "))
            if n <= 0 or n > 100:
                raise ValueError("Размер массива должен быть положительным числом от 1 до 100.")
                
            arr = []
            for i in range(n):
                while True:
                    try:
                        element = int(input(f"Введите элемент {i+1}: "))
                        if element < -100 or element > 100:
                            raise ValueError("Значение вне диапазона допустимых значений (-100 до 100).")
                        break
                    except ValueError as e:
                        print(str(e))
                arr.append(element)
            while True:
                try:
                    key = int(input("Введите ключ для поиска: "))
                    if key < -100 or key > 100:
                        raise ValueError("Значение вне диапазона допустимых значений (-100 до 100).")
                    break
                except ValueError as e:
                    print(str(e))
            
            return arr, key
        except ValueError as e:
            print(f"Ошибка: некорректный ввод данных. {str(e)}")
            continue

def main():
    arr, key = get_input()
    if arr is None or key is None:
        return

    search = BinarySearch(arr)
    positions = search.binary_search(key)

    if len(positions) == 0:
        print("Элемент не найден.")
    else:
        for pos in positions:
            print(f"Элемент {key} найден в отсортированном массиве на позиции {pos + 1}.")

    print("Отсортированный массив:")
    print(search.arr)

if __name__ == "__main__":
    main()