from collections import defaultdict
stack = []
def dfs(adj, visited, u):
    if u not in visited:
        visited.add(u)
        for element in adj[u]:
            if element not in visited:
                dfs(adj, visited, element)
    stack.append(u)
n = int(input("How many nodes? "))
e = int(input("How many edge? "))
adj = defaultdict(list)
print("Enter Edge Info ")
for i in range(e):
    u, v = input("Edge  %d " % (i + 1)).split()
    adj[u].append(v)

print(adj)
visited = set()
print("Topological Sort : ")
for vertex in list(adj):
    if vertex not in visited:
        dfs(adj, visited, vertex)


while stack:
    print(stack.pop())