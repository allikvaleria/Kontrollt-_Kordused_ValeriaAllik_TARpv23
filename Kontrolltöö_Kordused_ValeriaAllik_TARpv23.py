#1 Вариант


#1 Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n елок. Изображение одной елки имеет размер 4×9 символов, между двумя соседними елками также имеется пустой (из пробелов) столбец. Разрешается вывести пустой столбец после последней елки. Для упрощения рисования скопируйте елку из примера в среду разработки. Елки должны простоложиться горизонтально.

#   /V\    
#  / V \
# / V V \  
#/VV V VV\    

#2 Перемножить все не чётные значения в диапазоне от 0 до введенного пользователем числа(R);

#3 Дано N чисел. Найти количество положительных чисел среди них; N рандомное число

#4 Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

#5 Найти сумму ряда чисел от A до B. Полученный результат вывести на экран;


#1
n=int(input("Vali arv 1 kuni 9 :"))
for i in range(n):
    print("   /V\    ")
    print("  / V \   ")
    print(" / V V \  ")
    print("/VV V VV\ ")
    print()


#2
R=int(input("Sisesta arv :"))
if R%2==0:
    for i in range(0,R):
        R+=1
        print(R)
while True:
    R+=1
    print("vale")
    break


#3
import random
N=int(input("Sisesta numbrid : "))
positivset=0
mittepositiivsed=0
for i in range(N):
    if N > 0:
        positivset +=1
    mittepositiivsed +=1
print("positivsed : ")


#4
num = int(input("Sisesta naturaalarv: "))
paarisarv = 0
paaritu_arv = 0

while num > 0:
    a = num % 10
    if a % 2 == 0:
         paarisarv+= 1
    else:
         paaritu_arv+= 1
    num //= 10
print("Paarisarvude arv:", paarisarv)
print("Paaritu arv:", paaritu_arv)