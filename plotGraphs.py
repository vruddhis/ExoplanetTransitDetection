import matplotlib.pyplot as plt
import math
from collections import Counter

def plot_visibility_graph(points, graph):
    plt.figure(figsize=(8, 6))
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    plt.scatter(x_coords, y_coords)
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):  
            if graph[i][j] == 1:
                x_vals = [points[i][0], points[j][0]]
                y_vals = [points[i][1], points[j][1]]
                plt.plot(x_vals, y_vals)

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Visibility Graph")
    plt.grid(True, linestyle="--")
    plt.show()



