# -*- coding: utf-8 -*-



"""
Created on Mon Nov 15 08:51:21 2021

@author: KaiJax
"""
'''
1. Поработайте с переменными, создайте несколько, выведите на экран, 
запросите у пользователя несколько чисел и строк и сохраните в переменные, 
выведите на экран.
'''
perem = 0
perem2 = 'строка'

input_int = int(input('Введите число '))
input_str = input('Введите строку ')

perem = input_int
print(perem)

perem2 = input_str
print(perem2)

'''
2. Пользователь вводит время в секундах. Переведите время в часы, 
минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
'''
sec = int(input('Вччедите время в секундах '))
minutes = sec // 60
sec = sec % 60
sec = str(sec)
if len(sec) < 2:
    sec = '0' + sec
hour = minutes // 60
hour = str(hour)
if len(hour) < 2: # форматирование через 0, например 01 час
    hour = '0' + str(hour)
minutes = minutes % 60
minutes = str(minutes)
if len(minutes) < 2:
    minutes = '0' + str(minutes)
print(f'Текущее время: {hour}:{minutes}:{sec}')

'''
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, 
пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''
chislo = input('Введите число ')
chislo2 = int(chislo*2)
chislo3 = int(chislo*3)
chislo = int(chislo)
print(f'{chislo}+{chislo2}+{chislo3}={chislo+chislo2+chislo3}')

'''
4. Пользователь вводит целое положительное число. 
Найдите самую большую цифру в числе. Для решения используйте цикл while 
и арифметические операции.
'''
integer = input('Введите целое положительное число ')

maximus = 0
i = 0
while i < len(integer):
    if maximus < int(integer[i]):
        maximus = int(integer[i])
    i += 1
print(f'Максимальное число: {maximus}')

'''
5. Запросите у пользователя значения выручки и издержек фирмы. 
Определите, с каким финансовым результатом работает фирма 
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). 
Выведите соответствующее сообщение. Если фирма отработала с прибылью, 
вычислите рентабельность выручки (соотношение прибыли к выручке). 
Далее запросите численность сотрудников фирмы и определите прибыль фирмы 
в расчете на одного сотрудника.
'''
vyruchka = float(input('Напишите Вашу выручку '))
izderzhki = float(input('Напишите Вашу издержку '))
zarabotok = vyruchka-izderzhki
if zarabotok > 0:
    print('Ваша прибыль составляет:', zarabotok, ' руб.')
    print('Ваша рентабельность выручки:', zarabotok/vyruchka)
else:
    print('Ваш убыток составляет:', zarabotok, ' руб.')


if zarabotok > 0:
    stuff = int(input('Сколько у Вас сотрудников? Введите число'))
    print('Ваша прибыль на одного сотрудника:', zarabotok/stuff, ' руб.')


'''
6. Спортсмен занимается ежедневными пробежками. 
В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. 
Требуется определить номер дня, на который общий результат спортсмена 
составит не менее b километров. Программа должна принимать 
значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
'''

a = int(input('Введите число a '))
b = int(input('Введите число b '))

day = 1
while a < b:
    print(f'{day}-й день: {round(a, 2)}')
    a = a * 1.1
    day +=1
print(f'Ответ: на {day}-й день спортсмен достиг результата — не менее {b} км.')
