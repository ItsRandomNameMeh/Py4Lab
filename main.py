import random
import time


massi = []
h = 0

def generate():#генерируем стартовый массив
    print("Введите количество элементов стартового массива:")
    global h
    h = int(input())
    file_write(h)


def file_write(h):#генерируем и записываем в файл несортированные элементы
    G = open("1.txt", "w")
    if type(h) != int:
        raise TypeError("length must be int value")
    if h < 0:
        raise ValueError("length must be positive value")
    for i in range(h):
        G.write(str(random.randint(-10000,10000)) + "\n")
    return G


def readfile():#функция считывания данных из файла
    global massi
    C = open("1.txt", "r")
    for i in C:
        massi.extend(map(int,i.split()))
    sh_sort(massi)

start = time.time() #начинаем отсчет времени только при за-пуске функции
def sh_sort(array):#шейкерная сортировка
    length = len(array)
    swapped = True
    start_ind = 0
    end_ind = length-1

    while (swapped == True):
         swapped = False

         for i in range(start_ind, end_ind):#Проход слева направо
             if(array[i]>array[i+1]):
                 array[i], array[i+1] = array[i+1],array[i]#обмен элементов
                 swapped = True
         if not swapped:
            break

         swapped = False

         end_ind = end_ind - 1

         for i in range(end_ind - 1, start_ind - 1, -1):
            if(array[i] > array[i+1]):
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
         start_ind = start_ind+1
    return array

end = time.time() #завершаем отсчет времени сразу после окон-чания сортировки
def writefile():#Запись отсортированного массива в файл
    V = open("2.txt", "w")
    for i in massi:
        V.write(str(i)+"\n")

print("Шейкерная сортировка")
generate()
readfile()
print("Отсортированный массив: ")
print(massi)
writefile()


print("Время выполнения программы на " + str(h) + " значений составляет " + str(end-start) + " секунд")
