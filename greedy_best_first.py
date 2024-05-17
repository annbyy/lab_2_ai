import heapq
from read_graph import read_graph

def greedy_best_first_search(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (heuristic[start], start))
    came_from = {}
    visited = set()  # To keep track of visited nodes

    while open_set:
        _, current = heapq.heappop(open_set)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in graph[current]:
            if neighbor not in visited:
                came_from[neighbor] = current
                heapq.heappush(open_set, (heuristic[neighbor], neighbor))

    return []

# Example usage
if __name__ == "__main__":
    distance_Bucharest = {
        "Arad": 366, "Bucharest": 0, "Craiova": 160, "Drobita": 242, "Eforie": 161, 
        "Fagaras": 176, "Giurgiu": 77, "Hirsova": 151, "Iasi": 226, "Lugoj": 244, 
        "Mehedia": 241, "Neamt": 234, "Oradea": 380, "Pitesti": 100, "RM": 193, 
        "Sibiu": 253, "Timisoara": 329, "Urziceni": 80, "Vaslui": 199, "Zerind": 374
    }
    graph = read_graph('map.csv')
    print(greedy_best_first_search(graph, 'Arad', 'Bucharest', distance_Bucharest))
