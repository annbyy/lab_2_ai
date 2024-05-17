from collections import deque
from read_graph import read_graph

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    def bfs(queue, visited, parents, other_visited):
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current
                queue.append(neighbor)
                if neighbor in other_visited:
                    return neighbor
        return None

    forward_queue = deque([start])
    forward_visited = {start}
    forward_parents = {start: None}

    backward_queue = deque([goal])
    backward_visited = {goal}
    backward_parents = {goal: None}

    meeting_point = None

    while forward_queue and backward_queue:
        if forward_queue:
            meeting_point = bfs(forward_queue, forward_visited, forward_parents, backward_visited)
            if meeting_point:
                break

        if backward_queue:
            meeting_point = bfs(backward_queue, backward_visited, backward_parents, forward_visited)
            if meeting_point:
                break

    if not meeting_point:
        return []

    path = []
    node = meeting_point
    while node:
        path.append(node)
        node = forward_parents[node]
    path = path[::-1]
    node = backward_parents[meeting_point]
    while node:
        path.append(node)
        node = backward_parents[node]

    return path

# Example usage
if __name__ == "__main__":
    graph = read_graph('map.csv')
    print(bidirectional_search(graph, 'Arad', 'Bucharest'))
