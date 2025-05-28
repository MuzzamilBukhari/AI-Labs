from itertools import permutations

def tsp_brute_force(graph, start=0):
    num_cities = len(graph)
    cities = list(range(num_cities))
    # print(cities)
    cities.remove(start)
    
    min_path = []
    min_cost = float('inf')
    # print(min_cost)
    print(permutations(cities))
    for perm in permutations(cities):
        print(perm)
        current_cost = 0
        k = start
        for j in perm:
            current_cost += graph[k][j]
            k = j
        current_cost += graph[k][start]  # Return to starting city
        
        if current_cost < min_cost:
            min_cost = current_cost
            min_path = [start] + list(perm) + [start]
    
    print(f"Minimum cost: {min_cost}")
    print("Path taken:", " -> ".join(map(str, min_path)))

# Example graph (4 cities)
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tsp_brute_force(graph)

