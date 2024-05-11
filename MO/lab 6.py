import random

distances = [
    [0, 1, 7, 2, 8],
    [1, 0, 10, 3, 1],
    [7, 10, 0, 2, 6],
    [2, 3, 2, 0, 4],
    [8, 1, 6, 4, 0]
]


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


# функция скрещивает две особи. Точка разрыва после второго генома
# сделать точку разрыва в рандомном месте
def cross(parents):
    break_point = random.randint(1, 4)

    descendants = []
    first_child = []
    second_child = []

    first_child.append(parents[0][0])
    first_child.append(parents[0][1])
    second_child.append(parents[1][0])
    second_child.append(parents[1][1])

    for i in range(2, 5):
        first_genome = parents[0][i]
        second_genome = parents[1][i]
        if second_genome not in first_child:
            first_child.append(second_genome)
        if first_genome not in second_child:
            second_child.append(first_genome)
    for i in range(2, 5):
        first_genome = parents[0][i]
        second_genome = parents[1][i]
        if first_genome not in first_child:
            first_child.append(first_genome)
        if second_genome not in second_child:
            second_child.append(second_genome)
    # заполнять детей недостающими числами

    descendants.append(first_child)
    descendants.append(second_child)
    return descendants


population = start_population()
par = parents(population)
print(population)
print(par)
print(cross(par))
