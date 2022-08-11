# Disjoint Set

# find
def find(a):
    if parent[a] == a:
        return a

    p = find(parent[a])
    parent[a] = p
    return parent[a]


# union
def union(i, j):
    a = find(i)
    b = find(j)

    if a == b:
        return
    if rank[a] > rank[b]:
        parent[b] = a
    elif rank[a] < rank[b]:
        parent[a] = b
    else:
        rank[b] += 1
        parent[a] = b


# main
rank = [0 for _ in range(10)]
parent = [0, 4, 2, 2, 4, 2, 0, 0, 0, 4]

for i in range(len(parent) - 1):
    union(i, i + 1)
print(parent)
