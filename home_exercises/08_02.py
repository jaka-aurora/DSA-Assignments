
#Helsinki - Espoo: 20  
#Helsinki - Vantaa: 25  
#Helsinki - Turku: 165  
#Espoo - Vantaa: 15  
#Vantaa - Lahti: 105  
#Lahti - Jyväskylä: 170  
#Jyväskylä - Kuopio: 145  
#Tampere - Turku: 160  
#Tampere - Jyväskylä: 150  
#Tampere - Oulu: 430  
#Oulu - Rovaniemi: 220  
#Kuopio - Oulu: 280  

# Set this info of distances to `roads` variable correctly.

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