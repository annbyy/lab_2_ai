from collections import deque
from read_graph import read_graph

def bfs(graph, start, goal):
    queue = deque([start])
    came_from = {start: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for neighbor in graph[current]:
            if neighbor not in came_from:
                came_from[neighbor] = current
                queue.append(neighbor)

    return []

# Example usage
if __name__ == "__main__":
    graph = read_graph('map.csv')
    print(bfs(graph, 'Arad', 'Bucharest'))
