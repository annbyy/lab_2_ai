import csv

def read_graph(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        cities = next(reader)
        graph = {city: {} for city in cities}

        for i, row in enumerate(reader):
            for j, distance in enumerate(row):
                if distance != '-1' and distance != '0':
                    graph[cities[i]][cities[j]] = int(distance)
    return graph

# Example usage to verify the graph is read correctly
if __name__ == "__main__":
    graph = read_graph('map.csv')
    print(graph)
