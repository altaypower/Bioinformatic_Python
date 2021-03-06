"""
Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:

f(x)= \begin{cases}   1 - (x + 2)^2,\quad &\text{при } x\le -2\\  -\frac x2 ,\quad &\text{при } -2 \lt x \le 2\\   (x-2)^2 + 1,\quad &\text{при } 2 \lt x \end{cases}
f(x)=
⎩
⎨
⎧
​

 1−(x+2)
2
 ,
 −
2
x
​
 ,
 (x−2)
2
 +1,
​

при x≤−2
при −2<x≤2
при 2<x
​

Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.
Sample Input 1:
4.5
Sample Output 1:
7.25
Sample Input 2:
-4.5
Sample Output 2:
-5.25

def f(x):
    return float(x<-2 and 1-(x+2)**2 or 2<x and (x-2)**2+1 or -2<=x<=2 and -x/2)

"""