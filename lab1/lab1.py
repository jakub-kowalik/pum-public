"""
1. Genorowanie miast
2. Obliczanie dystansu pomiedzy miastami
3. Wizualizacja
4. Algorytm DFS
5. Algorytm BFS

1. X, Y, Z
"""
import random

punkty = [[100, 100, 50]]

def city_generator():
    return [random.randint(-100, 100), random.randint(-100, 100), random.randint(0, 50)]


if __name__ == '__main__':
    for i in range(0, 10):
        print(city_generator())

