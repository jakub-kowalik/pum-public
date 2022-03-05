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
    return adjacency_matrix


def visualize_cities(vertices_list):
    xs, ys, zs = zip(*vertices_list)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(xs, ys, zs)
    plt.show()


if __name__ == '__main__':
    cities = list()
    for i in range(0, 5):
        cities.append(city_generator())

    matrix = adjacency_matrix_generator(cities)

    for x in matrix:
        print(x)


    visualize_cities(cities)
