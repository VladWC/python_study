import random


def create_matrix(user_row, user_columm):
    # Создаёт матрицу заданного размера со случайными числами
    return [[random.randint(1, 10) for i in range(user_columm)] for i in range(user_row)]


def sort_up(matrix):
    # Сортирует матрицу по возрастанию
    for row in matrix:
        for i in range(len(row) - 1):
            for j in range(0, len(row) - i - 1):
                if row[j] > row[j + 1]:
                    row[j], row[j + 1] = row[j + 1], row[j]
    return matrix


def sort_revers(matrix):
    # сортирует матрицу по убыванию
    for row in matrix:
        for i in range(len(row) - 1):
            for j in range(0, len(row) - i - 1):
                if row[j] < row[j + 1]:
                    row[j], row[j + 1] = row[j + 1], row[j]
    return matrix


def column_sums(matrix):
    # Вычисляет сумму чисел в каждом столбце матрицы
    return [sum(user_columm) for user_columm in zip(*matrix)]


def print_matrix(matrix):
    # Выводит матрицу на экран
    for i in matrix:
        print(i)

    # основная программа


user_row = int(input("Сколько будет строк? \n"))
user_columm = int(input("Сколько будет столбцов? \n"))

# Создание и вывод исходной матрицы
matrix = create_matrix(user_row, user_columm)
print("Исходная матрица:")
print_matrix(matrix)

while True:
    user_choise = input(
        "1 - сортировать по возрастанию. \n2 - сортировать по убыванию. \n3 - вывести сумму столбцов. \n0 - завершить программу. \n"
    )
    if user_choise == "1":
        sort_matrix = sort_up(matrix)
        print_matrix(sort_matrix)
    elif user_choise == "2":
        sort_matrix = sort_revers(matrix)
        print_matrix(sort_matrix)
    elif user_choise == "3":
        column_sums(matrix)
        print_matrix(matrix)
        print("Сумма столбцов: \n", column_sums(matrix))
    elif user_choise == "0":
        print("Программа завершена")
        break
    else:
        print("Введите числа 1 2 3 или 0")
