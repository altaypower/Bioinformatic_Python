"""
Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в
строке, и после первого введенного нуля выводит сумму полученных на вход чисел.
"""

num=int(input())
summa=0
while num != 0:
    summa = summa +num
    num=int(input())
print(summa)