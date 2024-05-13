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


# функция определяет начальную популяцию
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


# функция определяет пары родителей
def parents(population):
    random_list = random.sample(population, 4)
    return random_list


def cross(parent, child, bp):
    start_index = bp + 1   # начальный индекс, с которого начнется проход по списку

    for i in range(start_index, start_index + len(parent)):
        # index = 0
        index = i % len(parent)  # геном начинающийся со второго выделенного элемента
        gene = parent[index]
        # print(i % len(parent))
        if gene not in child:
            for j in range(0, 5):
                if child[j] == "-":
                    child[j] = gene
                    break
    return child

# функция скрещивает две особи
def crossover(parents):
    first_break_point = random.randint(0, 3)
    second_break_point = random.randint(first_break_point + 2, 5)
    print("1 bp:", first_break_point)
    print("2 bp:", second_break_point)

    descendants = []
    first_child = ["-"] * 5
    second_child = ["-"] * 5
    third_child = ["-"] * 5
    fourth_child = ["-"] * 5

    # сохраняются выделенные зоны
    for i in range(first_break_point, second_break_point):
        first_child[i] = parents[0][1][i]
        second_child[i] = parents[0][0][i]
        third_child[i] = parents[1][1][i]
        fourth_child[i] = parents[1][0][i]

    print(first_child)
    print(second_child)
    print(third_child)
    print(fourth_child)

    first_child = cross(parents[0][0], first_child, first_break_point)
    second_child = cross(parents[0][1], second_child, first_break_point)
    third_child = cross(parents[1][0], third_child, first_break_point)
    fourth_child = cross(parents[1][1], fourth_child, first_break_point)

    descendants.append(first_child)
    descendants.append(second_child)
    descendants.append(third_child)
    descendants.append(fourth_child)
    return descendants


population = start_population()
print("начальная популяция", population)

for _ in range(5):
    par = parents(population)
    chunk_size = 2
    chunks = [par[i:i + chunk_size] for i in range(0, len(par), chunk_size)]
    print("пары родителей", chunks)
    crosses = crossover(chunks)
    print("потомство", crosses)
    population.append(crosses[0])
    population.append(crosses[1])
    population.append(crosses[2])
    population.append(crosses[3])

    # сортируем популяцию
    uniq_population = []
    for i in population:
        if i not in uniq_population:
            uniq_population.append(i)
    uniq_population.sort(key=lambda being: all_distance(being))

    # итоговое поколение
    sorted_population = []
    cnt = 0
    while cnt < 4:
        sorted_population.append(uniq_population[cnt])
        cnt += 1

    print("поколение {0}:".format(_ + 2))
    for i in range(len(sorted_population)):
        print("суммa расстояний", sorted_population[i], all_distance(sorted_population[i]))
    population = sorted_population
print("\nКротчайший путь:", population[0], all_distance(population[0]))
