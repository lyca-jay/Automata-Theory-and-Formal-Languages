import heapq

# Graph representation
graph = {
    'A': {'B': 1, 'D': 3},
    'B': {'C': 1},
    'C': {'F': 5},
    'D': {'E': 1},
    'E': {'F': 1},
    'F': {}
}

# Heuristic values (estimated distance to goal)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 4,
    'E': 1,
    'F': 0
}

def astar(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor, cost in graph[current].items():
            new_cost = g_cost[current] + cost

            if new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(open_list, (priority, neighbor))
                came_from[neighbor] = current

    return None

# start = 'A'
# goal = 'F'

# path = astar(start, goal)

# print("A* Pathfinding Result")
# print("Start:", start)
# print("Goal:", goal)
# print("Shortest Path:", path)

print("A* Pathfinding Result\n")
print("Example 1: A to F")
print("Shortest Path:", astar('A', 'F'))
print()
print("Example 2: B to F")
print("Shortest Path:", astar('B', 'F'))