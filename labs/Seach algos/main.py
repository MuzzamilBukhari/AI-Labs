# import heapq
# import random

# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F', 'G'],
#     'D': ['B'],
#     'E': ['B'],
#     'F': ['C'],
#     'G': ['C']
# }

# graph_weighted = {
#     'A': [('B', 1), ('C', 4)],
#     'B': [('A', 1),('C', 2),('D', 2), ('E', 5)],
#     'C': [('A', 4),('B', 2), ('F', 3), ('G', 6)],
#     'D': [],
#     'E': [('B', 5)],
#     'F': [('C', 3)],
#     'G': [('C', 6)]
# }


# def get_children(node):
#     return graph.get(node, [])

# def get_children_weighted(node):
#     return graph_weighted.get(node, [])

# def search_with_closed_list(initial, target):
#     closed_list = set()
#     x = initial

#     while True:
#         if x == target:
#             return f"Success: Found {target}"

#         children = get_children(x)

#         if not children:
#             return "Failure: No more nodes to explore"

#         closed_list.add(x)

#         # Select a new node that is not in the closed list
#         for child in children:
#             if child not in closed_list:
#                 x = child
#                 break


# def search_with_open_list(initial, target):
#     open_list = [initial]  # Stack (LIFO)
#     closed_list = set()  # Track visited nodes

#     while open_list:
#         x = open_list.pop()  # LIFO: Take top node from stack

#         if x == target:
#             return f"Success: Found {target}"

#         closed_list.add(x)  # Mark node as visited

#         children = get_children(x)

#         for child in children:  # Add new nodes to stack 
#             if child not in closed_list and child not in open_list:
#                 open_list.append(child)

#     return "Failure: Target not found"

# def random_search(initial, target):
#     x = initial  # Step 1: Start from initial node
    
#     while True:
#         if x == target:  # Step 2: Check if it's the target node
#             return f"Success: Found {target}"
        
#         children = get_children(x)  # Step 3: Expand the node

#         if not children:  # If no children, stop with failure
#             return "Failure: Target not found"
        
#         x = random.choice(children)  # Step 4: Pick a random child and return to step 2


# def uniform_cost_search(initial, target):
#     open_list = []  # Priority queue (min-heap)
#     closed_list = set()  # To track visited nodes
#     costs = {initial: 0}  # Store cost of reaching each node

#     heapq.heappush(open_list, (0, initial))  # Step 1: Add initial node with cost 0
    
#     while open_list:
#         c_x, x = heapq.heappop(open_list)  # Step 2: Get the node with lowest cost

#         if x == target:
#             return f"Success: Found {target} with cost {c_x}"

#         closed_list.add(x)  # Step 3: Move x to the closed list

#         childrens = get_children_weighted(x)
#         for x_prime, cost in childrens:  # Step 4: Expand node
#             if x_prime in closed_list:
#                 continue

#             new_cost = c_x + cost  # C(x') = C(x) + d(x, x')

#             if x_prime not in costs or new_cost < costs[x_prime]:
#                 costs[x_prime] = new_cost  # Update cost
#                 heapq.heappush(open_list, (new_cost, x_prime))  # Push to open list
#         # print(costs)

#     return "Failure: Target not found"

# # Main Function
# def main():
#     print("Choose a search algorithm to test:")
#     print("1. Closed List Search")
#     print("2. Open List Search")
#     print("3. Random Search")
#     print("4. Uniform Cost Search")

#     choice = input("Enter the number of your choice: ")

#     initial_node = input("Enter the Initial node: ")
#     target_node = input("Enter the element you want to search: ")

#     if choice == "1":
#         result = search_with_closed_list(initial_node, target_node)
#     elif choice == "2":
#         result = search_with_open_list(initial_node, target_node)
#     elif choice == "3":
#         result = random_search(initial_node, target_node)
#     elif choice == "4":
#         result = uniform_cost_search(initial_node, target_node)
#     else:
#         result = "Invalid choice! Please enter a number between 1 and 4."

#     print(result)

# if __name__ == "__main__":
#     main()


import streamlit as st
import heapq
import random
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba

# Define graph data
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
    path = [initial]

    while True:
        if x == target:
            return True, path, closed_list, f"Success: Found {target}"

        children = get_children(x)

        if not children:
            return False, path, closed_list, "Failure: No more nodes to explore"

        closed_list.add(x)

        # Select a new node that is not in the closed list
        next_node = None
        for child in children:
            if child not in closed_list:
                next_node = child
                break
        
        if next_node:
            x = next_node
            path.append(x)
        else:
            return False, path, closed_list, "Failure: No unvisited nodes available"

def search_with_open_list(initial, target):
    open_list = [initial]  # Stack (LIFO)
    closed_list = set()  # Track visited nodes
    path = []

    while open_list:
        x = open_list.pop()  # LIFO: Take top node from stack
        path.append(x)

        if x == target:
            return True, path, closed_list, f"Success: Found {target}"

        closed_list.add(x)  # Mark node as visited
        children = get_children(x)

        for child in children:  # Add new nodes to stack 
            if child not in closed_list and child not in open_list:
                open_list.append(child)

    return False, path, closed_list, "Failure: Target not found"

def random_search(initial, target):
    x = initial  # Step 1: Start from initial node
    path = [initial]
    visited = set([initial])
    
    max_steps = 20  # Prevent infinite loops in demo
    steps = 0
    
    while steps < max_steps:
        steps += 1
        if x == target:  # Step 2: Check if it's the target node
            return True, path, visited, f"Success: Found {target}"
        
        children = get_children(x)  # Step 3: Expand the node

        if not children:  # If no children, stop with failure
            return False, path, visited, "Failure: Target not found"
        
        x = random.choice(children)  # Step 4: Pick a random child and return to step 2
        path.append(x)
        visited.add(x)
    
    return False, path, visited, "Stopped: Maximum steps reached"

def uniform_cost_search(initial, target):
    open_list = []  # Priority queue (min-heap)
    closed_list = set()  # To track visited nodes
    costs = {initial: 0}  # Store cost of reaching each node
    path = []

    heapq.heappush(open_list, (0, initial))  # Step 1: Add initial node with cost 0
    
    while open_list:
        c_x, x = heapq.heappop(open_list)  # Step 2: Get the node with lowest cost
        path.append(x)

        if x == target:
            return True, path, closed_list, f"Success: Found {target} with cost {c_x}"

        closed_list.add(x)  # Step 3: Move x to the closed list

        childrens = get_children_weighted(x)
        for x_prime, cost in childrens:  # Step 4: Expand node
            if x_prime in closed_list:
                continue

            new_cost = c_x + cost  # C(x') = C(x) + d(x, x')

            if x_prime not in costs or new_cost < costs[x_prime]:
                costs[x_prime] = new_cost  # Update cost
                heapq.heappush(open_list, (new_cost, x_prime))  # Push to open list

    return False, path, closed_list, "Failure: Target not found"

def create_graph_visualization(path=None, visited=None):
    G = nx.Graph()
    
    # Add all nodes
    for node in graph.keys():
        G.add_node(node)
    
    # Add unweighted edges
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    
    # Create positions
    pos = nx.spring_layout(G, seed=42)
    
    plt.figure(figsize=(8, 6))
    
    # Draw the base graph
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    
    # Highlight path if provided
    if path and len(path) > 1:
        path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=2.5, edge_color='red')
    
    # Highlight visited nodes if provided
    if visited:
        visited_nodes = list(visited)
        nx.draw_networkx_nodes(G, pos, nodelist=visited_nodes, node_color='yellow', node_size=500)
    
    # Highlight path nodes
    if path:
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='green', node_size=500)
        
        # Highlight start and end nodes
        if len(path) > 0:
            nx.draw_networkx_nodes(G, pos, nodelist=[path[0]], node_color='blue', node_size=500)
            nx.draw_networkx_nodes(G, pos, nodelist=[path[-1]], node_color='red', node_size=500)
    
    # Add labels
    nx.draw_networkx_labels(G, pos, font_size=16, font_weight='bold')
    
    plt.axis('off')
    return plt

def create_weighted_graph_visualization(path=None, visited=None):
    G = nx.Graph()
    
    # Add all nodes
    for node in graph_weighted.keys():
        G.add_node(node)
    
    # Add weighted edges
    for node, neighbors in graph_weighted.items():
        for neighbor, weight in neighbors:
            G.add_edge(node, neighbor, weight=weight)
    
    # Create positions
    pos = nx.spring_layout(G, seed=42)
    
    plt.figure(figsize=(8, 6))
    
    # Draw the base graph
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    
    # Add edge labels (weights)
    edge_labels = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=14)
    
    # Highlight path if provided
    if path and len(path) > 1:
        path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
        valid_path_edges = [edge for edge in path_edges if G.has_edge(edge[0], edge[1])]
        nx.draw_networkx_edges(G, pos, edgelist=valid_path_edges, width=2.5, edge_color='red')
    
    # Highlight visited nodes if provided
    if visited:
        visited_nodes = list(visited)
        nx.draw_networkx_nodes(G, pos, nodelist=visited_nodes, node_color='yellow', node_size=500)
    
    # Highlight path nodes
    if path:
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='green', node_size=500)
        
        # Highlight start and end nodes
        if len(path) > 0:
            nx.draw_networkx_nodes(G, pos, nodelist=[path[0]], node_color='blue', node_size=500)
            nx.draw_networkx_nodes(G, pos, nodelist=[path[-1]], node_color='red', node_size=500)
    
    # Add labels
    nx.draw_networkx_labels(G, pos, font_size=16, font_weight='bold')
    
    plt.axis('off')
    return plt

# Streamlit App
st.title("Graph Search Algorithm Visualization")

st.sidebar.header("Settings")
search_method = st.sidebar.selectbox(
    "Choose a search algorithm",
    ["Closed List Search", "Open List Search", "Random Search", "Uniform Cost Search"]
)

all_nodes = list(graph.keys())
initial_node = st.sidebar.selectbox("Initial Node", all_nodes, index=0)
target_node = st.sidebar.selectbox("Target Node", all_nodes, index=len(all_nodes)-1)

if st.sidebar.button("Run Search"):
    st.subheader(f"Running {search_method} from {initial_node} to {target_node}")
    
    # Run selected algorithm
    if search_method == "Closed List Search":
        success, path, visited, message = search_with_closed_list(initial_node, target_node)
        plt = create_graph_visualization(path, visited)
    elif search_method == "Open List Search":
        success, path, visited, message = search_with_open_list(initial_node, target_node)
        plt = create_graph_visualization(path, visited)
    elif search_method == "Random Search":
        success, path, visited, message = random_search(initial_node, target_node)
        plt = create_graph_visualization(path, visited)
    elif search_method == "Uniform Cost Search":
        success, path, visited, message = uniform_cost_search(initial_node, target_node)
        plt = create_weighted_graph_visualization(path, visited)
    
    # Display results
    st.pyplot(plt)
    
    # Show path and result message
    st.subheader("Search Results")
    st.write(message)
    
    if path:
        st.write("Path taken:")
        st.write(" → ".join(path))
    
    # Display legend
    st.sidebar.subheader("Legend")
    st.sidebar.markdown("- 🔵 **Blue**: Starting node")
    st.sidebar.markdown("- 🔴 **Red**: Target node")
    st.sidebar.markdown("- 🟢 **Green**: Nodes in path")
    st.sidebar.markdown("- 🟡 **Yellow**: Visited nodes")
    st.sidebar.markdown("- 🔴 **Red lines**: Path edges")

# Display graph info
with st.expander("Show Graph Structure"):
    st.subheader("Graph Structure")
    st.json(graph)
    
    st.subheader("Weighted Graph Structure")
    st.json(graph_weighted)

# Display algorithm explanation
with st.expander("Algorithm Explanations"):
    st.subheader("Closed List Search")
    st.write("""
    Explores nodes one at a time, keeping track of visited nodes in a closed list.
    At each step, it selects a child node that hasn't been visited yet.
    """)
    
    st.subheader("Open List Search")
    st.write("""
    Uses a stack (LIFO) to track nodes to visit.
    Pops the top node from the stack, checks if it's the target, and adds unvisited children to the stack.
    """)
    
    st.subheader("Random Search")
    st.write("""
    At each step, randomly selects one of the child nodes to explore next.
    Simple but unpredictable - may or may not find the target efficiently.
    """)
    
    st.subheader("Uniform Cost Search")
    st.write("""
    A weighted search algorithm that uses a priority queue to explore nodes with the lowest cumulative cost first.
    Optimal for finding the shortest path in terms of edge weights.
    """)