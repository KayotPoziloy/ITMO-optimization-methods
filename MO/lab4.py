# Шаг 1 основная функция
def f(x, y):
    return x**4 + y**4 - 4*x*y


eps = 1e-6
h = 0.1


# Шаг 2 производная по x1 и по x2
def fx(x, y):
    return 4 * (x**3 - y)


def fy(x, y):
    return 4 * y**3 - 4 * x


# Шаг 3
x0 = 0.1
y0 = 0.1

x_old = x0
y_old = y0
while True:
    # Шаг 4
    dx = fx(x_old, y_old)
    dy = fy(x_old, y_old)

    x_new = x_old - h * dx
    y_new = y_old - h * dy

    M = [x_new, y_new]
    print("M: ", M)
    # Шаг 5
    f_old = f(x_old, y_old)
    f_new = f(x_new, y_new)
    # Шаг 6
    if abs(f_new - f_old) < eps:
        print(M)
        break

    x_old = x_new
    y_old = y_new
