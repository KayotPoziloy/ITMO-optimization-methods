import random

distances = [
    [0, 1, 7, 2, 8],
    [1, 0, 10, 3, 1],
    [7, 10, 0, 2, 6],
    [2, 3, 2, 0, 4],
    [8, 1, 6, 4, 0]
]


# функция считает расстояние между двумя городами
def distance(point1, point2):
    return distances[point1][point2]


# функция считает полное расстояние маршрута
def all_distance(being):
    summ_of_distance = 0
    for i in range(4):
        # print(being[i])
        summ_of_distance += distance(being[i], being[i+1])
    summ_of_distance += distance(being[-1], being[0])
    return summ_of_distance


# функция возвращает начальную популяцию
def start_population():
    population = []
    # available_distances = distances
    while True:
        random_list = random.sample(range(5), 5)
        if random_list not in population:
            population.append(random_list)
        if len(population) == 4:
            break
    return population


# функция вычленяет две особи из популяции
def parents(population):
    random_list = random.sample(population, 2)
    return random_list


# функция скрещивает две особи
def cross(parents):
    break_point = random.randint(1, 4)
    print("bp:", break_point)

    descendants = []
    first_child = []
    second_child = []

    for i in range(0, break_point):
        first_child.append(parents[0][i])
        second_child.append(parents[1][i])

    for i in range(break_point, 5):
        first_genome = parents[0][i]
        second_genome = parents[1][i]
        if second_genome not in first_child:
            first_child.append(second_genome)
        if first_genome not in second_child:
            second_child.append(first_genome)
    for i in range(break_point, 5):
        first_genome = parents[0][i]
        second_genome = parents[1][i]
        if first_genome not in first_child:
            first_child.append(first_genome)
        if second_genome not in second_child:
            second_child.append(second_genome)

    descendants.append(first_child)
    descendants.append(second_child)
    return descendants


population = start_population()
print("начальная популяция", population)
for _ in range(5):
    par = parents(population)
    print("родители", par)
    crossover = cross(par)
    print("потомство", crossover)
    population.append(crossover[0])
    population.append(crossover[1])

    # сортируем популяции по сумме расстояний в порядке возрастания
    population.sort(key=lambda being: all_distance(being))
    print("популяция с потомством", population)

    # итоговое поколение
    population = population[:-2]

    for i in range(len(population)):
        print("суммa расстояний", population[i], all_distance(population[i]))

