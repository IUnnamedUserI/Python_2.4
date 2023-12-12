#!/usr/bin/python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    A = list(map(int, input("Введите 10 целочисленных"
                            "элементов массива: ").split()))
    if (len(A) != 10):
        print("Количество элементов не равно 10. Завершение программы...")
        exit(1)
    
    result = []
    summ = 0

    result = [i for i in A if i < abs(3) and i % 9 == 0]
    summ = sum(i for i in A if i < abs(3) and i % 9 == 0)

    print(f"Элементы списка: {result}")
    print(f"Количество элементов: {len(result)}")
    print(f"Сумма элементов: {summ}")
