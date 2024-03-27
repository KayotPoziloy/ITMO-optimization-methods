from math import e

a, b, eps = 0.5, 1.5, 0.001


# основная функция
def f(x):
    return 1/x + e**x


# производная функции
def f_derivative(x):
    return e**x - 1/x**2


# вторая производная функции
def f_derivative_scnd(x):
    return e**x + 2/x**3


# длина интервала
def interval_len(a, b):
    return (a + b)/2


# Метод половинного деления
# Суть в том, что интервал сужается к искомой пока не удовлетворит погрешности
def half_division(a, b, eps):

    while b - a > 2*eps:

        x1 = (a + b - eps)/2
        x2 = (a + b + eps)/2
        y1 = f(x1)
        y2 = f(x2)

        if y1 > y2:
            a = x1
        else:
            b = x2

    return interval_len(a, b)


# Метод золотого сечения
# Тоже, что и деление пополам, только деление по золотому сечению
def golden_section(a, b, eps):

    while (b - a)/2 >= eps:
        x1 = a + 0.382*(b - a)
        x2 = a + 0.618*(b - a)
        y1 = f(x1)
        y2 = f(x2)

        if y1 > y2:
            a = x1
            x1 = x2
            x2 = b + 0.382*(x2 - a)
        else:
            b = x2
            x2 = x1
            x1 = a + 0.618*(b - x1)

    return interval_len(a, b)


# Метод хорд
def chord(a, b, eps):
    while True:
        x = a - f_derivative(a)/(f_derivative(a) - f_derivative(b))*(a-b)

        y = f_derivative(x)
        print(f_derivative(a), f_derivative(b), x, y, f_derivative(x))
        if y <= eps:
            return x
        else:
            if y > 0:
                b = x
            else:
                a = x


# Метод Ньютона
def newton(a, b, eps):
    x0 = b
    while True:
        y1 = f_derivative(x0)
        y2 = f_derivative_scnd(x0)
        x = x0 - y1/y2
        yx = f_derivative(x)
        if abs(yx) <= eps:
            return x
        else:
            x0 = x


# print(half_division(a, b, eps))
# print(golden_section(a, b, eps))
print(chord(a, b, eps))
# print(newton(a, b, eps))
