from collections import defaultdict
from queue import Queue


n = int(input("Please enter the number of nodes: "))

e = int(input("Please enter the number of edges: "))

# creating adjacency list using dictionary
adj = defaultdict(list)

for i in range(e):
    u, v = input("Edge %d: " % (i + 1)).split()
    adj[u].append(v)
    adj[v].append(u)

# Performing BFS
q = Queue(maxsize=len(adj))

visited = set()

s = input("Enter the source node: ")

q.put(s)

visited.add(s)

print(n-1)