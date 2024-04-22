eps = 1e-6


# Шаг 1 основная функция
def f(x, y):
    return x ** 4 + y ** 4 - 4 * x * y


# Шаг 2 производная по x1 и по x2
def fx(x, y):
    return 4 * (x ** 3 - y)


def fy(x, y):
    return 4 * y ** 3 - 4 * x


def find_x(x, y):
    pass


def func(x, y, dx, dy, h):
    return f(x - h * dx, y - h * dy)


def find_h(x, y):
    dx = fx(x, y)
    dy = fy(x, y)
    # df(x - h*dx, y - h*dy) / dy
    # g = f(x - h*dx, y - h*dy) = 4(x-h*dx)^4 + 4(y-h*dy)^4 - 4(x-h*dx)(y-h*dy)
    # dg/dh = 4*dx*(x-h*dx)^3 + 4*dy*(x-h*dy)^3 - 4((-dx)(y-h*dx) + (-dy)(x-h*dx)) = 0
    # d/dh( (x-h(4*(x^3-y)) )^4+(y-h(4*y^3-4*x))^4-4*(x-h(4*(x^3-y)))((y-h(4*y^3-4*x))) )
    a = 0
    b = dx ** 2 + dy ** 2

    while b - a > 2 * eps:
        m1 = a + (b - a) / 3
        m2 = b - (b - a) / 3

        y1 = func(x, y, dx, dy, m1)
        y2 = func(x, y, dx, dy, m2)

        if y1 > y2:
            a = m1
        else:
            b = m2

    return (a + b) / 2

# Шаг 3
x0 = 0.1
y0 = 0.1

x_old = x0
y_old = y0
while True:
    # Шаг 4
    dx = fx(x_old, y_old)
    dy = fy(x_old, y_old)
    h = find_h(x_old, y_old)

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
