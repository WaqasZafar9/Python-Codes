def astar(graph, heuristic, start, goal):
    front = [(0, start)]
    visited_node = {}
    total_cost = {start: 0}
    while front:
        current_cost, current_node = front.pop(0)
        if current_node == goal:
            break
        for next_node, cost in graph[current_node].items():
            new_cost = current_cost + cost
            if next_node not in total_cost or new_cost < total_cost[next_node]:
                total_cost[next_node] = new_cost
                priority = new_cost + heuristic[next_node]
                front.append((priority, next_node))
                visited_node[next_node] = current_node
    path = []
    current_node = goal
    while current_node != start:
        path.append(current_node)
        current_node = visited_node[current_node]
    path.append(start)
    path.reverse()
    return path

# Example usage:
graph = {
    'a': {'b': 6, 'e': 7},
    'b': {'c': 99, 'g': 0},
    'c': {},
    'd': {'g': 0},
    'e': {'d': 1},
    'g': {}
}
heuristic_values = {
    'a': 6,
    'b': 0,
    'c': 99,
    'd': 0,
    'e': 7,
    'g': 0
}
start_node = 'a'
goal_node = 'g'
shortest_path = astar(graph, heuristic_values, start_node, goal_node)
print("Shortest path from {} to {}: {}".format(start_node, goal_node, shortest_path))
