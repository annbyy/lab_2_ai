from read_graph import read_graph

def dfs(graph, start, goal):
    stack = [(start, [start])]

    while stack:
        (current, path) = stack.pop()

        for neighbor in graph[current]:
            if neighbor in path:
                continue
            if neighbor == goal:
                return path + [neighbor]
            stack.append((neighbor, path + [neighbor]))

    return []

# Example usage
if __name__ == "__main__":
    graph = read_graph('map.csv')
    print(dfs(graph, 'Arad', 'Bucharest'))
