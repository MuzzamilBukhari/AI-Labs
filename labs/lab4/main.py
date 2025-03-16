import heapq
import random

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

graph_weighted = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1),('C', 2),('D', 2), ('E', 5)],
    'C': [('A', 4),('B', 2), ('F', 3), ('G', 6)],
    'D': [],
    'E': [('B', 5)],
    'F': [('C', 3)],
    'G': [('C', 6)]
}


def get_children(node):
    return graph.get(node, [])

def get_children_weighted(node):
    return graph_weighted.get(node, [])

def search_with_closed_list(initial, target):
    closed_list = set()
    x = initial

    while True:
        if x == target:
            return f"Success: Found {target}"

        children = get_children(x)

        if not children:
            return "Failure: No more nodes to explore"

        closed_list.add(x)

        # Select a new node that is not in the closed list
        for child in children:
            if child not in closed_list:
                x = child
                break


def search_with_open_list(initial, target):
    open_list = [initial]  # Stack (LIFO)
    closed_list = set()  # Track visited nodes

    while open_list:
        x = open_list.pop()  # LIFO: Take top node from stack

        if x == target:
            return f"Success: Found {target}"

        closed_list.add(x)  # Mark node as visited

        children = get_children(x)

        for child in children:  # Add new nodes to stack 
            if child not in closed_list and child not in open_list:
                open_list.append(child)

    return "Failure: Target not found"

def random_search(initial, target):
    x = initial  # Step 1: Start from initial node
    
    while True:
        if x == target:  # Step 2: Check if it's the target node
            return f"Success: Found {target}"
        
        children = get_children(x)  # Step 3: Expand the node

        if not children:  # If no children, stop with failure
            return "Failure: Target not found"
        
        x = random.choice(children)  # Step 4: Pick a random child and return to step 2


def uniform_cost_search(initial, target):
    open_list = []  # Priority queue (min-heap)
    closed_list = set()  # To track visited nodes
    costs = {initial: 0}  # Store cost of reaching each node

    heapq.heappush(open_list, (0, initial))  # Step 1: Add initial node with cost 0
    
    while open_list:
        c_x, x = heapq.heappop(open_list)  # Step 2: Get the node with lowest cost

        if x == target:
            return f"Success: Found {target} with cost {c_x}"

        closed_list.add(x)  # Step 3: Move x to the closed list

        childrens = get_children_weighted(x)
        for x_prime, cost in childrens:  # Step 4: Expand node
            if x_prime in closed_list:
                continue

            new_cost = c_x + cost  # C(x') = C(x) + d(x, x')

            if x_prime not in costs or new_cost < costs[x_prime]:
                costs[x_prime] = new_cost  # Update cost
                heapq.heappush(open_list, (new_cost, x_prime))  # Push to open list
        # print(costs)

    return "Failure: Target not found"

# Main Function
def main():
    print("Choose a search algorithm to test:")
    print("1. Closed List Search")
    print("2. Open List Search")
    print("3. Random Search")
    print("4. Uniform Cost Search")

    choice = input("Enter the number of your choice: ")

    initial_node = input("Enter the Initial node: ")
    target_node = input("Enter the element you want to search: ")

    if choice == "1":
        result = search_with_closed_list(initial_node, target_node)
    elif choice == "2":
        result = search_with_open_list(initial_node, target_node)
    elif choice == "3":
        result = random_search(initial_node, target_node)
    elif choice == "4":
        result = uniform_cost_search(initial_node, target_node)
    else:
        result = "Invalid choice! Please enter a number between 1 and 4."

    print(result)

if __name__ == "__main__":
    main()