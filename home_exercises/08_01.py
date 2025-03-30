# presents Finnish cities and their road connections using a dictionary-based adjacency list

from collections import deque

# To find the route from place A to place B, we can use Breadth-First Search (BFS) to find the shortest or a possible path.

#  1  procedure BFS(G, root) is
#  2      let Q be a queue
#  3      label root as explored
#  4      Q.enqueue(root)
#  5      while Q is not empty do
#  6          v := Q.dequeue()
#  7          if v is the goal then
#  8              return v
#  9          for all edges from v to w in G.adjacentEdges(v) do
# 10              if w is not labeled as explored then
# 11                  label w as explored
# 12                  w.parent := v
# 13                  Q.enqueue(w)

def find_route(graph, start, end):
    queue = deque([(start, [start])])  # Queue stores (current_city, path_so_far)
    visited_cities = set()

    while queue:
        city, path = queue.popleft()

        if city == end:
            return path  # Return the path once we reach the destination

        if city not in visited_cities:
            visited_cities.add(city)
            for neighbor in graph.get(city, []):
                if neighbor not in visited_cities:
                    queue.append((neighbor, path + [neighbor]))

    return None

# Define the Finnish cities graph (Adjacency List)
city_graph = {
    "Helsinki": ["Espoo", "Vantaa", "Turku"],
    "Espoo": ["Helsinki", "Vantaa"],
    "Vantaa": ["Helsinki", "Espoo", "Lahti"],
    "Lahti": ["Vantaa", "Jyväskylä"],
    "Jyväskylä": ["Lahti", "Kuopio", "Tampere"],
    "Kuopio": ["Jyväskylä", "Oulu"],
    "Tampere": ["Turku", "Jyväskylä"],
    "Turku": ["Helsinki", "Tampere"],
    "Oulu": ["Kuopio", "Rovaniemi"],
    "Rovaniemi": ["Oulu"]
}

# TODO: Set routes to find routes between two cities
routes = [["Kuopio", "Helsinki"], ["Helsinki", "Kuopio"], ["Vantaa", "Oulu"], ["Oulu", "Vantaa"]]

# Find the routes between cities
for cities in routes:
    route = find_route(city_graph, cities[0], cities[1])
    if route:
        print(" -> ".join(route))
    else:
        print(f"No route found between the {route[0]} and {route[1]}.")