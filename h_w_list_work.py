import random
import datetime


# вывод даты
def date():
    watch = datetime.datetime.now()
    str_watch = watch.strftime("%d.%m.%y %H.%M.%S")
    return str_watch


# вывод операции
def operation():
    ops = [" Пополнение ", " Снятие ", " Оплата связи "]
    index = random.randint(0, 2)
    return ops[index]


# вывод суммы операции
def amount():
    amts = [100, 200, 300, 400, 500]
    index = random.randint(0, 4)
    return str(amts[index])


# вывод статуса операции
def status():
    sts = [" Успешно", " Ошибка"]
    index = random.randint(0, 1)
    return sts[index]


# Вывод случайного лога
log_ful = []
for _ in range(2000):
    log_string = date() + operation() + amount() + status()
    log_ful.append(log_string)
print(log_ful)

# счетчик ошибок
counter_fail = 0
for fail in log_ful:
    if fail.lower().find(" ошибка") != -1:
        counter_fail += 1
print("Всего ошибок: ", counter_fail)

# счетчик успешных oплат связи
counter_pay = 0
for pay in log_ful:
    if pay.lower().find(" оплата связи ") != -1 and pay.lower().find(" успешно") != -1:
        counter_pay += 1
print("Всего успешных oплат связи: ", counter_pay)

# счетчик успешных пополнений
counter_replen = 0
for replen in log_ful:
    if (
        replen.lower().find(" пополнение ") != -1
        and replen.lower().find(" успешно") != -1
    ):
        counter_replen += 1
print("Всего успешных пополнений: ", counter_replen)

# счетчик успешных снятий
counter_removal = 0
for removal in log_ful:
    if (
        removal.lower().find(" снятие ") != -1
        and removal.lower().find(" успешно") != -1
    ):
        counter_removal += 1
print("Всего успешных снятий: ", counter_removal)

# список успешной оплаты связи
all_pay = []
for pay_secs in log_ful:
    if (
        pay_secs.lower().find(" оплата связи ") != -1
        and pay_secs.lower().find(" успешно") != -1
    ):
        all_pay.append(pay_secs)
# print(all_pay)

# список сумм оплаты связи
pay_sum_string = []
for pay_num_string in all_pay:
    num_string = pay_num_string[31:34]
    pay_sum_string.append(num_string)

# общая сумма пополнений связи
pay_sum = 0
for num_str in pay_sum_string:
    num = int(num_str)
    pay_sum += num
print("Всего заработано на пополнениях: ", pay_sum)

# всего пополнений на 500
pay_500_all = []
for pay_500 in log_ful:
    if pay_500.lower().find("оплата связи 500 успешно") != -1:
        pay_500_all.append(pay_500)
# print(pay_500_all)

# время пополнений на 500
time_pay_500 = []
for time in pay_500_all:
    time_pay_500.append(time[8:18])
print("Время пополнений на 500:", time_pay_500)
