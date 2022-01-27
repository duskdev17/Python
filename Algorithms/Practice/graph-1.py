"""Graph Adjacency Matrix"""

n = int(input("How many nodes? "))
e = int(input("How many edges? "))

adj = [[0 for i in range(n)] for j in range(n)]

print(adj)

print("Enter edges' information in separate lines.")

for i in range(e):
    u, v = map(int, input("Edges %d: " %(i+1).split()))
    adj[u][v] = 1
    adj[v][u] = 1

for line in adj:
    for element in line:
        print(element, end = '  ')
    print()