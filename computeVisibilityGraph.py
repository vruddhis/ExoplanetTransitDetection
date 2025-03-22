def visibility_graph(points):
    #assumption is already sorted by x coordinate
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    n = len(y_coords)
    graph = [[0] * n for _ in range(n)]  #adjacency matrix

    def find_max_index_in_subarray(subarray, offset):
        max_val = subarray[0]
        max_idx = 0
        for i in range(1, len(subarray)):
            if subarray[i] > max_val:
                max_val = subarray[i]
                max_idx = i
        return max_idx + offset  

    def visibility_graph_subarray(x, y, left, right, graph):
        if left >= right:
            return
        
        k = find_max_index_in_subarray(x[left:right + 1], left)
        for i in range(left, right + 1):
            if i == k:
                continue

            visible = True
            for j in range(min(i + 1, k + 1), max(i, k)):
                if x[j] >= x[i] + (x[k] - x[i]) * ((y[j] - y[i]) / (y[k] - y[i])):
                    visible = False
                    break

            if visible:
                graph[k][i] = 1
                graph[i][k] = 1
        
        visibility_graph_subarray(x, y, left, k - 1, graph) 
        visibility_graph_subarray(x, y, k + 1, right, graph) 

    visibility_graph_subarray(y_coords, x_coords, 0, n - 1, graph)
    return graph


def horizontal_visibility_graph(points):
    #assumption is already sorted by x coordinate
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    n = len(y_coords)
    graph = [[0] * n for _ in range(n)]  #adjacency matrix

    def find_max_index_in_subarray(subarray, offset):
        max_val = subarray[0]
        max_idx = 0
        for i in range(1, len(subarray)):
            if subarray[i] > max_val:
                max_val = subarray[i]
                max_idx = i
        return max_idx + offset  

    def visibility_graph_subarray(y, x, left, right, graph):
        if left >= right:
            return
        
        k = find_max_index_in_subarray(y[left:right + 1], left)
        for i in range(left, right + 1):
            if i == k:
                continue

            visible = True
            for j in range(i + 1, k):
                if y[j] >= min(y[i], y[k]): 
                    visible = False
                    break

            if visible:
                graph[k][i] = 1
                graph[i][k] = 1
        
        visibility_graph_subarray(y, x, left, k - 1, graph)  
        visibility_graph_subarray(y, x, k + 1, right, graph)  

    visibility_graph_subarray(y_coords, x_coords, 0, n - 1, graph)
    return graph


