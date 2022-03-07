"""
1. Genorowanie miast
2. Obliczanie dystansu pomiedzy miastami
3. Wizualizacja
4. Algorytm DFS
5. Algorytm BFS

1. X, Y, Z

  A B C D
A 0 2 1 3
B 5 0
C    0
D      0


"""
import random
import matplotlib.pyplot as plt

random.seed(1234)

punkty = [[100, 100, 50]]


def city_generator():
    return [random.randint(-100, 100), random.randint(-100, 100), random.randint(0, 50)]


def city_distance(x, y):
    return ((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2 + (y[2] - x[2]) ** 2) ** (1 / 2)


def adjacency_matrix_generator(vertices_list):
    adjacency_matrix = list()
    for i in vertices_list:
        matrix_row = list()
        for j in vertices_list:
            if i == j:
                matrix_row.append(None)
            else:
                matrix_row.append(city_distance(i, j))
        adjacency_matrix.append(matrix_row)
    return (vertices_list, adjacency_matrix)


def visualize_cities(vertices_list, path=None):
    xs, ys, zs = zip(*vertices_list)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(xs, ys, zs)

    if path is not None:
        for i in range(len(path) - 1):
            plt.plot([path[i][0], path[i + 1][0]],
                     [path[i][1], path[i + 1][1]],
                     [path[i][2], path[i + 1][2]])

    plt.show()


def dfs_alghoritm(paths, vertices, start, visited=None):
    if visited is None:
        visited = list()
    print("node ", start)
    if start not in visited:
        visited.append(start)

        possible_next = list()
        for x in vertices:
            if x is not start and x not in visited:
                possible_next.append(x)

        for x in possible_next:
            dfs_alghoritm(paths, vertices, x, list(visited))

    if len(vertices) == len(visited):
        if visited not in paths:
            paths.append(visited)
    return visited


if __name__ == '__main__':
    cities = list()
    for i in range(0, 3):
        cities.append(city_generator())

    matrix = adjacency_matrix_generator(cities)

    # print(matrix)
    for x in matrix[1]:
        print(x)

    all_pathes = list()

    answer = dfs_alghoritm(all_pathes, cities, cities[0])
    print(all_pathes)
    visualize_cities(cities, all_pathes[0])
