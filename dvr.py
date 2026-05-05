nodes = int(input("Enter number of nodes: "))

cost = []
for i in range(nodes):
	row = list(map(int, input(f"Enter cost from node {i} to others: ").split()))
	cost.append(row)

dist = cost.copy()

for k in range(nodes):
	for i in range(nodes):
		for j in range(nodes):
			if dist[i][j] > dist[i][k] + dist[k][j]:
				dist[i][j] = dist[i][k] + dist[k][j]

print("\nShortest Distance matrix:")
for i in range(nodes):
	for j in range(nodes):
		print(dist[i][j], end="\t")
	print()