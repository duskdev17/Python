import sys


def dfs(node):
    color[node] = 'gray'

    for elements in adj[node]:
        if color[elements] == 'gray':
            print('Cycle')
            sys.exit()
        elif color[elements] == 'white':
            dfs(elements)
            print(' Not c')

    color[node] = 'black'


n = input("Enter Nodes: ").split()
e = int(input("Enter Number of Edges: "))

adj = {}
color = {}
rac = []
for node in n:
    color[node] = 'white'
    adj[node] = []

for i in range(e):
    v, u = input("Edge %d: " % (i + 1)).split()
    adj[v].append(u)

for node in n:
    if color[node] == 'white':
        dfs(node)
