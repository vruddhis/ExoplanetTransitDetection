from computeVisibilityGraph import visibility_graph
from plotGraphs import plot_visibility_graph

points = [(1,2), (2,8), (3,4), (4,5)]

graph = visibility_graph(points)
plot_visibility_graph(points, graph)


