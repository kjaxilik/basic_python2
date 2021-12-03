

with open('text_1.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Input new string or empty string to done: ')
        if not line:
            break
        # f.write(f'{line}\n')
        print(line, file=f)


# вариант более компактный

print('Введите данные для записи в файл \n для окончания ввода введите пустую строку')
with open('task_1.txt', 'w', encoding='utf-8') as my_file:
    while(line := input()) != '':
        my_file.write(f'{line}\n')

# третий вариант

my_file = open('text_1.txt', 'w', encoding='utf-8')

line = ''
while line:
    line = input('gbibnt или не пишите!: ')
    my_file.write(f'{line}\n') if line != '' else my_file.close()





# урок 6

class MyAuto:
    # атрибуты класса
    # name = 'Lexus'
    # nodel = 'RX 350L'
    # year = 2021
    a_count = 0
    
    
    # конструктор
    # атрибуты объекта
    def __init__(self, n, m, y):
        self.name = n
        self.model = m
        self.year = y
        MyAuto.a_count += 1  # если поставить self то счетчик обнулится при добавлении следующего объекта
        print(n, m, y)
        # self.on_start()
    
    # методы 
    def on_start(self, speed):
        print(f'Go-go!{self.name} with speed {speed}')
    def on_stop(self):
        print('Stop!')

auto_1 = MyAuto('Mazda', 'CX9', 2021)
# print(auto_1.name)
# auto_1.name = 'Mazda'
# print(auto_1.name)
auto_1.on_start(15)
print(auto_1.a_count)

auto_2 = MyAuto('Lada', 'Niva 4x4', 2019)
print(auto_1.a_count)
auto_2.on_start(35)
# print(auto_2.name)




# вывод разными цветами текст и фон
def out_red(text):
    print("\033[31m {}" .format(text))
def out_yellow(text):
    print("\033[33m {}" .format(text))
def out_blue(text):
    print("\033[34m {}" .format(text))
out_red("Вывод красным цветом")
out_yellow("Текст жёлтого цвета")
out_blue("Синий текст")



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    

print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)





