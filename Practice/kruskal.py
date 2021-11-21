nn = input("Enter node name : ").split()
e = int(input("How many edges : "))

edges = []
parent = {}
rank = {}

print("Enter edges (u,v,w)")

for i in range(e):
    u, v, w = input("Edges %d : " % (i + 1)).split()
    edges.append([u, v, int(w)])


def make_set(x):
    parent[x] = x
    rank[x] = 0


def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])


def union_set(x, y):  # X AND Y BOTH ARE PARENTS
    if rank[x] > rank[y]:
        parent[y] = x

    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


def kruskal():
    selected_edge = list()  # CREATING EMPTY LIST
    mst_weight = 0
    for node in nn:
        make_set(node)
    s_e = sorted(edges, key=lambda x: x[2])

    for edge in s_e:
        u, v, w = edge[0], edge[1], edge[2]
        parent_u = find_set(u)
        parent_v = find_set(v)
        if parent_u != parent_v:
            selected_edge.append(edge)
            mst_weight += w
            union_set(parent_u, parent_v)

    print(" selected edges ")
    for edge in s_e:
        print(edge)
    print(mst_weight)

kruskal()