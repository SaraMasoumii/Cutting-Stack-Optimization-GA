import random as rd

def initial_population(n, size_of_pop) -> list:
    list_of_orders = []
    order = []
    for i in range(n):
        order.append(i)
    for i in range(size_of_pop):
        new_order = order.copy()
        rd.shuffle(new_order)
        list_of_orders.append(new_order)
    return list_of_orders


def crossover(list_of_orders, n, mutation_rate) -> list:
    rd.shuffle(list_of_orders)
    size = len(list_of_orders)
    for i in range(0, size, 2):
        mom = list_of_orders[i]
        dad = list_of_orders[i + 1]
        first_child = [mom[j] if rd.random() < 0.5 else dad[j] for j in range(len(mom))]
        second_child = [dad[j] if rd.random() < 0.5 else mom[j] for j in range(len(dad))]
        list_of_orders.append(mutation(first_child, mutation_rate))
        list_of_orders.append(mutation(second_child, mutation_rate))
    return list_of_orders


def mutation(child, mutation_rate) -> list:
    n = len(child)
    if rd.random() <= mutation_rate:
        indexes = rd.sample(range(n), 2)
        a = child[indexes[0]]
        b = child[indexes[1]]
        child[indexes[0]] = b
        child[indexes[1]] = a
    return child


def order_fitness(order, roll_length) -> int:
    num_of_rolls = 1
    s = 0
    for i in range(len(order)):
        if s + requests[order[i]] <= roll_length:
            s += requests[order[i]]
        else:
            num_of_rolls += 1
            s = requests[order[i]]
    return num_of_rolls


def calculate_fitness(list_of_orders, roll_length) -> list:
    list_of_fitness = []
    for i in list_of_orders:
        list_of_fitness.append(order_fitness(i, roll_length))
    return list_of_fitness


def eliminate(list_of_orders, roll_length):
    size = len(list_of_orders)
    list_of_fitness = calculate_fitness(list_of_orders, roll_length)
    sorted_orders = [x for _, x in sorted(zip(list_of_fitness, list_of_orders))]
    final_orders = sorted_orders[: size // 2]
    min_fitness = min(list_of_fitness)
    return final_orders, min_fitness

def read_txt_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        roll_length = int(lines[0].split(":")[1].strip())

        sizes_start_index = lines.index('Requests:\n') + 1
        requests = list(map(int, lines[sizes_start_index].split(", ")))
        ans = int(lines[lines.index('ans:\n') + 1: ][0])
    return roll_length, requests, ans



roll_length, requests, ans = read_txt_file('input4.txt')
n = len(requests)
minimum = n
mutation_rate = 0.2

pop = initial_population(n, 100)
generation = 0

while minimum > ans:
    pop = crossover(pop, n, mutation_rate)
    pop, minimum = eliminate(pop, roll_length)
    generation += 1
    print('min number of rolls by now:', minimum, 'Generation:', generation)

print('minimum number of rolls:', minimum, '\n order:', pop[0])
