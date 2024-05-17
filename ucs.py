import heapq
from read_graph import read_graph

def uniform_cost_search(graph, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    cost_so_far = {start: 0}

    while open_set:
        current_cost, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor, distance in graph[current].items():
            new_cost = current_cost + distance
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(open_set, (new_cost, neighbor))
                came_from[neighbor] = current

    return []

# Example usage
if __name__ == "__main__":
    graph = read_graph('map.csv')
    print(uniform_cost_search(graph, 'Arad', 'Bucharest'))
