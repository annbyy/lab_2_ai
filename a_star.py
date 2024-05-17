import heapq
from read_graph import read_graph

def a_star(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {city: float('inf') for city in graph}
    g_score[start] = 0
    f_score = {city: float('inf') for city in graph}
    f_score[start] = heuristic[start]

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor, distance in graph[current].items():
            tentative_g_score = g_score[current] + distance
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic[neighbor]
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

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
    print(a_star(graph, 'Arad', 'Bucharest', distance_Bucharest))
