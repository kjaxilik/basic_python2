"""
Домашнее задание к уроку 2
"""

#1 Создать список и заполнить его элементами различных типов данных. 
# Реализовать скрипт проверки типа данных каждого элемента. 
# Использовать функцию type() для проверки типа. 
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

v = ['windows', 2021, 20.51, 'job jurney', 5, 'John']
for i in range(10):
    v.append(v[i-1])

chk = ['string' if type(x) == str else 'int' for x in v]


# 2. Для списка реализовать обмен значений соседних элементов, т.е. 
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
# При нечетном количестве элементов последний сохранить на своем месте. 
# Для заполнения списка элементов необходимо использовать функцию input().

v2 = input('Введите элементы списка через пробел: ').split()

for i in range(0, len(v2)-1, 2):
    v2[i], v2[i+1] = v2[i+1], v2[i]

print(v2)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
# Напишите решения через list и через dict.

ch = input('Введите целое число от 1 до 12: ')

if int(ch) <= 12 and int(ch) >= 1:
    ################# Вывод из list:#################
    vrem_goda = [0,'Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
    
    print('Вывод из list:',vrem_goda[int(ch)])
    
    ################# Вывод из dict#################
    keys = [str(x) for x in range(13)]
    dct = dict(zip(keys, vrem_goda))
    # если пользователь ввел число через 0
    if int(ch) != 10:
        ch = ch.replace('0', '')
    print('Вывод из dict:',dct[ch])
    
else:
    print('Ошибка! Введите целое число от 1 до 12')





# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать. 
# Если в слово длинное, выводить только первые 10 букв в слове.

v = input('введите строку из нескольких слов: ').split()

for i in range(int(len(v))):
    print(i, '. ', v[i][:10], sep=(''))





# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы 
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]

my_list.append(int(input('Введите элемент рейтинга от 1 до 10: ')))

lenth = len(my_list)
my_list.sort(reverse=True)
print(my_list)

for i in range(5):
    numb = int(input('Введите элемент рейтинга от 1 до 10: '))
    my_list.append(numb)
    my_list.sort(reverse=True)
    ind = my_list.index(numb)
    if ind == 0:
        my_list.pop(ind + lenth)
    else:
        my_list.pop(ind-1)
    print(my_list)



# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента 
# — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, 
# единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]


rng = int(input('Сколько товаров будете добавлять? '))
lst = []
for i in range(0, rng):
    nazvanie = input('Введите наименование товара №'+ str(i+1)+ ': ')
    price = input('Введите стоимость товара №'+ str(i+1)+  ': ')
    qnt = input('Введите количество товара №'+ str(i+1)+ ': ')
    edinica = input('Введите единицу измерения товара №'+ str(i+1)+ ': ')
    # adding elements with i+1 (starting with 1)
    lst.append([i+1, {'название': nazvanie, 'цена': price, 'количество': qnt, 'eд': edinica}])

tovary = tuple(lst) #converting list into tuple

# Необходимо собрать аналитику о товарах. Реализовать словарь, 
# в котором каждый ключ — характеристика товара, например название, 
# а значение — список значений-характеристик, 
# например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

# print(tovary[0][1].items())
# print(tovary[0][1].keys())

# создаем список ключей словаря:
k = list(tovary[0][1].keys())
# создаем пустой словарь
dct_an = dict()

for i in range(len(tovary)):
    # фильтруем только словарь текущего товара сохраняем в dict:
    dct = tovary[i][1]
    for i in range(len(dct)):
        # сохраняем текущий ключ в val
        val = dct_an.get(k[i])
        # проверка есть ли такой ключ?
        if val != None:
            # если есть такой ключ проверяем тип значения:
            if type(val) is list:
                # если значение лист добавляем значение
                val.append(dct.get(k[i]))
                dct_an[k[i]] = val
            else:
                # если не лист создаем лист и добавляем значения
                temp = []
                temp.append(dct_an.get(k[i]))
                temp.append(dct.get(k[i]))
                dct_an[k[i]] = temp
        else:
            # добавление ключа в словарь
            dct_an[k[i]] = dct.get(k[i])
            