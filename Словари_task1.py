"""
Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь
 dd и два числа: keykey и valuevalue.
Если ключ keykey есть в словаре dd, то добавьте значение valuevalue в список,
который хранится по этому ключу.
Если ключа keykey нет в словаре, то нужно добавить значение в список по
ключу 2 * key2∗key. Если и ключа 2 * key2∗key нет, то нужно добавить
ключ 2 * key2∗key в словарь и сопоставить ему список из переданного элемента
 [value][value].
Требуется реализовать только эту функцию, кода вне её не должно быть.
Функция не должна вызывать внутри себя функция nput print.


"""

def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    elif 2 * key in d:
        d[2 * key] += [value]
    else:
        d[2 * key] = [value]

d = {}

update_dictionary(d, 1, -3)

print(d)