"""Graph Adjacency List"""

from collections import defaultdict

n = int(input("How many nodes? "))
e = int(input("How many edges? "))

adj = defaultdict(list)

print("Enter edges information. ")

for i in range(e):
    u, v = input("Edge %d: " %(i+1)).split()
    adj[u].append(v)
    adj[v].append(u)

print(adj)