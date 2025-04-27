import random

# 1
print("Задание 1")
myList = [x*3 for x in range(0, 10)]
print(myList)

# 2
print("Задание 2")
same_list = ["Яблоко", "Банан", "Дата", "вишня"]
sort_same_list = [x for x in same_list if x.istitle()]
print(sort_same_list)

# 3
print("Задание 3")
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
join_list = [x for x in list1 if x in list2]
print(join_list)

# 4
print("Задание 4")
list_list = [[1, 2], [3, 4], [5, 6]]
list_list_join = [num for row in list_list for num in row]
print(list_list_join)

# 5
print("Задание 5")
sours_list = ["int", "12", "abc", "64"]
sort_sours_list = [row for row in sours_list if row.isdigit()]
print(sort_sours_list)

# 6
print("Задание 6")
corteg = [(x, y) for x in range(-2, 2) for y in range(-2, 2) if x!=y]
print(corteg)

# 7
print("Задание 7")
add_even = ["even" if x%2==0 else "add" for x in range(30)]
print(add_even)

# 8
print("Задание 8")
cratno = ["Кратно 3" if x%3==0 else "Кратно 7" if x%7==0 else "Кратно 2" if x%2==0 else None for x in range(100)]
print(cratno)
