# Question:
# Given a graph represented as an adjacency list and a start node, implement BFS traversal. Then write a function to check if a target node is reachable from the start node.
# Input:
# graph = {
#     "A": ["B", "C"],
#     "B": ["D"],
#     "C": ["D"],
#     "D": []
# }
# start = "A"
#
# Output of BFS traversal: ["A", "B", "C", "D"]
# is_connected("A", "D") → True
# is_connected("A", "X") → False

from collections import deque

# Part A: BFS traversal of a graph
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

    return order

# Part B: Check if a graph is connected (valid/reachable)
def is_connected(graph, start, target):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node == target:
            return True
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            queue.append(neighbor)

    return False

# Part C: Detect cycle in directed graph (DFS)
def has_cycle(graph):
    visited = set()
    rec_stack = set()  # nodes in current DFS path

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False



# Test
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}
print(bfs(graph, "A"))             # ['A', 'B', 'C', 'D']
print(is_connected(graph, "A", "D"))  # True
print(has_cycle(graph))            # False