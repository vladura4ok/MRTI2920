""" Написать функцию для вычисления суммы всех элементов вложенных списков.
Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элменетов - 34
Функция должна быть рекурсивной, то есть она должна обходить каждый элемент списка и
вызывать саму себя, если текущий элемент так же является списком. """


def recursion(list_):
    s = 0
    for i in list_:
        if type(i) != type(list()):
            s += i
        else:
            s = s + recursion(i)

    return s


# _____________________________________________________________________________________
a = [1, 2, [2, 4, [[7, 8], 4, 6]]]
print("Sum of list items ", recursion(a))
