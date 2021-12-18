def make_set(x):
    parent[x] = x
    rank[x] = 0


def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])

    return parent[x]


def union_set(x, y):
    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] = rank[y] + 1


def kruskal():
    selected_edges = []
    mst_weight = 0
    for node in nodes:
        make_set(node)

    sorted_edges = sorted(edges, key=lambda x: x[2])
    for edge in sorted_edges:
        u, v, w = edge[0], edge[1], edge[2]
        parent_u = find_set(u)
        parent_v = find_set(v)
        if parent_u != parent_v:
            selected_edges.append(edge)
            mst_weight += w
            union_set(parent_u, parent_v)

    print("Selected edges are")
    for edge in selected_edges:
        print(edge)
    print("MST weight: %d." % mst_weight)


nodes = input("Enter nodes' name: ").split()
e = int(input("How many edges: "))

edges = []
parent = {}
rank = {}

print("Enter edges' information (u v w)")
for i in range(e):
    u, v, w = input("Edge %d: " % (i + 1)).split()
    edges.append([u, v, int(w)])

kruskal()
print(parent)
print(rank)

"""
Enter nodes' name: 9
How many edges: 14
Enter edges' information (u v w)
Edge 1: a b 4
Edge 2: a h 8
Edge 3: b h 11
Edge 4: b c 8
Edge 5: h i 7
Edge 6: c i 2
Edge 7: i g 6
Edge 8: c d 7
Edge 9: c f 4
Edge 10: h g 1
Edge 11: d e 9
Edge 12: d f 14
Edge 13: e f 10
Edge 14: g f 2
"""