#!/usr/bin/python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    A = list(map(float, input("Введите несколько"
                              "вещественных чисел: ").split()))
    i_min = 0
    min_sum = 0
    null_count = 0    

    #Поиск минимального значения
    for i in A:
        if i < i_min:
            i_min = i
        if i == float(0):
            null_count += 1

    for i in range(A.index(i_min) + 1, len(A), 1):
        min_sum += A[i]

    print(f"Наименьший элемент - [{A.index(i_min)}] {i_min}")
    print(f"Количество элементов, равных нулю - {null_count}")
    print(f"Сумма элементов, находящихся после минимального - {min_sum}")
