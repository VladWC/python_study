import random

user_row = int(input("Сколько будет строк? \n"))
user_columm = int(input("Сколько будет столбцов? \n"))

final_list = []
elemment_columm = []


def elemen_random():
    for i in range(user_row):
        value = random.randint(0, 9)
    return value


# def elemment_columm_random():
#     for i in range(user_row):
#         elemment_columm.append(elemen_random())
#     return elemment_columm
# print(elemment_columm_random())

# def final_list_random():
#     for i in range(user_columm):
#         for j in range(user_row):
#             elemment_columm.append(elemen_random())
#     return final_list
# print(final_list_random())

# user_answer = int(input("1 - вывести сумму строки. \n2 - вывести сумму столбца.\n"))

# if user_answer == 1:
#     print(stroka_sum)
# elif user_answer == 2:
#     print(columm_sum)
