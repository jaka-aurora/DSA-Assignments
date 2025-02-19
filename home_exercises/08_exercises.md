# Lesson Exercises

## 08-01: Shortest Route with BFS

There is implemented Breadth-First Search algorithm to find the shortest route between two connected points.

In this assignment, you should test the program that it works correctly.
Try to test algorithm with different routes between given cities.

* TODO: Set `routes` array to find routes between two cities 

```
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
# routes = ??? 

# Find the routes between cities
for cities in routes:
    route = find_route(city_graph, cities[0], cities[1])
    if route:
        print(" -> ".join(route))
    else:
        print(f"No route found between the {route[0]} and {route[1]}.")

```

## 08-02: Find shortest route (Dijkstra/networkx)

In this assignment, you should calculate the shortest route between two distances using networkx.

* finding the shortest route is done with Dijkstra’s algorithm.

In this task, you only have to set the `roads` list yourself. All the other code is ready.

Use the following information to set routes with kilometers:

```
Helsinki - Espoo: 20  
Helsinki - Vantaa: 25  
Helsinki - Turku: 165  
Espoo - Vantaa: 15  
Vantaa - Lahti: 105  
Lahti - Jyväskylä: 170  
Jyväskylä - Kuopio: 145  
Tampere - Turku: 160  
Tampere - Jyväskylä: 150  
Tampere - Oulu: 430  
Oulu - Rovaniemi: 220  
Kuopio - Oulu: 280  
```

Set this info of distances to `roads` variable correctly.


```
import networkx as nx

city_graph = nx.Graph()

# Add nodes between cities
cities = ["Helsinki", "Espoo", "Vantaa", "Tampere", "Turku", "Oulu", "Jyväskylä", "Kuopio", "Lahti", "Rovaniemi"]
city_graph.add_nodes_from(cities)

# TODO: Add edges (roads and distances between cities)
roads = [ 
   # TODO: Set roads + distances correctly in the array
]

for city1, city2, distance in roads:
    city_graph.add_edge(city1, city2, weight=distance)

# Init output adjacency list (connections between cities)
for city, neighbors in city_graph.adjacency():
    print(f"{city}: {list(neighbors)}")


# Find the shortest route using Dijkstra’s algorithm
routes = [["Jyväskylä", "Helsinki"],["Helsinki", "Oulu"],["Rovaniemi", "Espoo"],["Turku","Kuopio"]]

for route in routes:
    try:
        # method can be 'dijkstra', 'bellman-ford' etc.
        shortest_path = nx.shortest_path(city_graph, source=route[0], target=route[1], weight="weight", method='dijkstra')
        total_distance = nx.shortest_path_length(city_graph, source=route[0], target=route[1], weight="weight", method='dijkstra')
        print(" -> ".join(shortest_path), f". Distance: {total_distance} km")
    except nx.NetworkXNoPath:
        print(f"No route found between the {route[0]} and {route[1]}.")

``` 
