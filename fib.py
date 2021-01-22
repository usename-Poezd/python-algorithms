def fib(n):
    """
    Вычесление чисел фибоначи
    :param n: Номер элемента ряда Фибоначчи
    :return: Число Фиббоначи
    """
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b

    return a

n = int(input("Номер элемента ряда Фибоначчи: "))

print(fib(n))