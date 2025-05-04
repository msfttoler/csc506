import heapq

def dijkstra(graph, start, end):
    # Priority queue to store (cost, current_node, path_taken)
    queue = [(0, start, [])]
    seen = set()
    min_dist = {start: 0}
    
    while queue:
        (cost, v1, path) = heapq.heappop(queue)
        if v1 in seen:
            continue
        seen.add(v1)
        path = path + [v1]
        if v1 == end:
            return (cost, path)
        for v2, c in graph.get(v1, {}).items():
            if v2 in seen:
                continue
            prev = min_dist.get(v2, None)
            next_cost = cost + c
            if prev is None or next_cost < prev:
                min_dist[v2] = next_cost
                heapq.heappush(queue, (next_cost, v2, path))
    
    return float("inf"), []

# Example graph simulating roads with traffic delay (lower values = faster routes)
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'Z': 6},
    'E': {'C': 10, 'D': 2, 'Z': 3},
    'Z': {'D': 6, 'E': 3}
}

# Run the algorithm
start_node = 'A'
end_node = 'Z'
cost, path = dijkstra(graph, start_node, end_node)

# Output result
print(f"Shortest path from {start_node} to {end_node}: {' -> '.join(path)}")
print(f"Total cost (time/weight): {cost}")