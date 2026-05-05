nodes = int(input("Enter number of nodes: "))

cost = []

for i in range(nodes):
    row = list(map(int, input(f"Enter cost from node {i} to others: ").split()))
    cost.append(row)

source = int(input("Enter source node: "))

dist = [999] * nodes
visited = [False] * nodes

dist[source] = 0

for _ in range(nodes):

    min_dist = 999
    u = -1

    for i in range(nodes):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            u = i

    visited[u] = True

    for v in range(nodes):
        if cost[u][v] != 999 and not visited[v]:
            if dist[v] > dist[u] + cost[u][v]:
                dist[v] = dist[u] + cost[u][v]

print("\nShortest distances from source node:")

for i in range(nodes):
    print(f"Node {i}: {dist[i]}")