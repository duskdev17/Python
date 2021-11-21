"""DFS --- Greedy Algorithm"""
from collections import defaultdict


def dfs(adj, visited, u):
    if u not in visited:
        visited.add(u)

    for element in adj[u]:
        if element not in visited:
            dfs(adj, visited, element)

        print(u, end = ' ')

n = int(input("n="))
e = int(input("e="))

adj = defaultdict(list)

for i in range(e):
    u, v = input("Edge %d: " %(i+1)).split()
    adj[u].append(v)
    adj[v].append(u)

print(adj)

visited = set()
print("DFS: ")

for vertex in adj:
    if vertex not in visited:
        dfs(adj, visited, vertex)