"""Graph Adjacency List"""

n = int(input("How many nodes? "))
e = int(input("How many edges? "))

adj = {}

print("Enter edges information. ")

for i in range(e):
    u, v = input("Edges %d: " %(i+1)).split()
    if u not in adj:
        adj[u] = [v]
    else:
        adj[u].append(v)
    if v not in adj:
        adj[v] = [u]
    else:
        adj[v].append(u)

print(adj)