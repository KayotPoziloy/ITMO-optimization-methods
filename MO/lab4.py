import math


# Шаг 1 основная функция
def f(x1, x2):
    return math.exp(-x1 ** 2 + x2 ** 2 + 2 * x1 * x2 - x2)


eps = 0.2
h = 0.3


# Шаг 2 производная по x1 и по x2
def fx1(x1, x2):
    return -1 * (2 * math.exp(x2 ** 2) * x1 - 2 * x2 * math.exp(x2 ** 2)) * math.exp(-x1 ** 2 + 2 * x2 * x1 - x2)


def fx2(x1, x2):
    return (2 * x2 + 2 * x1 - 1) * math.exp(x2 ** 2 + 2 * x1 * x2 - x2 - x1 ** 2)


# Шаг 3
x01 = 0
x02 = 0
X0 = [x01, x02]
grad_f = [fx1(x01, x02), fx2(x01, x02)]

while True:
    # Шаг 4
    x1_old = x01
    x2_old = x02
    x1_new = x1_old - h * grad_f[0]
    x2_new = x2_old - h * grad_f[1]
    X = [x1_new, x2_new]

    # Шаг 5
    f_old = f(x1_old, x2_old)
    f_new = f(x1_new, x2_new)

    print(f_old, f_new)
    # Шаг 6
    if abs(f_new - f_old) < eps:
        print(X)
        break
