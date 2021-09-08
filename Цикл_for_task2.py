"""
Напишите программу, которая считывает с клавиатуры два числа a a a и b b b, считает и выводит
на консоль среднее арифметическое всех чисел из отрезка [a;b] [a; b] [a;b], которые кратны
числу 3 3 3.
В приведенном ниже примере среднее арифметическое считается для чисел на отрезке
[−5;12] [-5; 12] [−5;12]. Всего чисел, делящихся на 3 3 3, на этом отрезке
6 6 6: −3,0,3,6,9,12 -3, 0, 3, 6, 9, 12 −3,0,3,6,9,12. Их среднее арифметическое равно
4.5 4.5 4.5
На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое
делится на 3 3 3.
"""

result = [i for i in range(int(input()), int(input()) + 1) if i % 3 == 0]
print(sum(result)/len(result))