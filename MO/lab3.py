from math import e

a, b, eps1, eps2, deltaX = 1, 1.5, 0.0001, 0.01, 0.5


# основная функция
def f(x):
    return 1/x + e**x if x != 0 else 100000


# Шаг 1 - 5
def initial_values(a):
    # Шаг 1
    x1 = a
    # Шаг 2
    x2 = x1 + deltaX

    # Шаг 3
    f1, f2 = f(x1), f(x2)

    # Шаг 4
    if f1 > f2:
        x3 = x1 + 2 * deltaX
        x_min = x1
    else:
        x3 = x1 - deltaX
        x_min = x3

    # Шаг 5
    f3 = f(x3)

    return x1, x2, x3, f1, f2, f3, x_min


cnt = 0

x1, x2, x3, f1, f2, f3, x_min = initial_values(a)

while True:
    cnt += 1

    # Шаг 6
    f_min = min(f1, f2, f3)
    x_min = [x1, x2, x3][[f1, f2, f3].index(f_min)]

    # Шаг 7
    denominator = (x2 - x3) * f1 + (x3 - x1) * f2 + (x1 - x2) * f3

    if denominator == 0:
        x1 = x_min
        continue

    xm = 0.5 * (((x2**2 - x3**2) * f1 + (x3**2 - x1**2) * f2 + (x1**2 - x2**2) * f3) / denominator)
    fxm = f(xm)

    print(abs((f_min - fxm)/fxm), abs((x_min - xm)/xm))
    # Шаг 8
    if (abs((f_min - fxm)/fxm) < eps1) & (abs((x_min - xm)/xm) < eps2):
        print(xm, cnt)
        break
    else:
        if (x1 <= xm <= x3) | (x1 >= xm >= x3):
            x1, x2, x3, f1, f2, f3, x_min = initial_values(min(xm, x_min))
            # f_min = min(f1, f3, fxm)
            # x_min = [x1, x3, xm][[f1, f3, fxm].index(f_min)]
            # x1 = x_min
            # x2 = x1 + deltaX
            # if f1 > f2:
            #     x3 = x1 + 2 * deltaX
            #     x_min = x1
            # else:
            #     x3 = x1 - deltaX
            #     x_min = x3
        else:
            x1, x2, x3, f1, f2, f3, x_min = initial_values(xm)
            continue

