from collections import deque

graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}



def dfs(graph, root):
    visited = list()
    stack = list()

    stack.append(root)

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])

    return visited

print(dfs(graph, 'A'))

def bfs(graph, root):
    visited = list()
    queue = deque()

    queue.append(root)

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return visited

print(bfs(graph, 'A'))