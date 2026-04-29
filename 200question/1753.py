import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
k = int(input())
graph = [[] for _ in range(V+1)]
weight = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append(v)
    weight[u].append(w)

distances = [float('INF')]*(V+1)
def dijkstra(graph, start):
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for i in range(len(graph[current_vertex])):
            neighbor = graph[current_vertex][i]
            weights = weight[current_vertex][i]
            distance = current_distance + weights

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

dijkstra(graph, k)

for i in range(1, len(distances)):
    if distances[i] == float('inf'):
        print('INF')
    else:
        print(distances[i])


