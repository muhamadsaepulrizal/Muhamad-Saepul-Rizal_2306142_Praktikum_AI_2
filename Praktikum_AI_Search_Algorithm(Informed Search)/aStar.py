from os import path
from queue import PriorityQueue

def a_star_tree_search(graph, start, goal, heuristic):
  frontier = PriorityQueue()
  frontier.put((0, start)) #(priority, node)
  path = {}

  while not frontier.empty():
    _, current_node = frontier.get()

    if current_node == goal:
      print("Goal node found!")
      route = reconstruct_path(path, start, goal)
      print("Route optimal: ", route)
      return True

    for neighbor, cost in graph[current_node].items():
      priority = heuristic[neighbor] + cost
      frontier.put((priority, neighbor))
      path[neighbor] = current_node

  print("Goal node not found!")
  return False


def a_star_tree_search(graph, start, goal, heuristic):
  frontier = PriorityQueue()
  frontier.put((0, start)) #(priority, node)
  explored = set()
  path = {}
  while not frontier.empty():
    _, current_node = frontier.get()

    if current_node == goal:
      print("Goal node found!")
      route = reconstruct_path(path, start, goal)
      print("Route optimal: ", route)
      return True

    explored.add(current_node)

    for neighbor, cost in graph[current_node].items():
      if neighbor not in explored:
        total_cost = cost * heuristic[neighbor]
        frontier.put((total_cost, neighbor))
        path[neighbor] = current_node

  print("Goal node not found!")
  return False

def reconstruct_path(path, start, goal):
    current = goal
    route = [current]
    while current != start:
      current = path[current]
      route.append(current)

    route.reverse()
    return route

#heuristic values
heuristic = {
    'A': 4,
    'B': 3,
    'C': 3,
    'D': 1,
    'S': 6,
    'G': 0,
}
#grph 
graph = {
    'S': {'A': 3, 'B': 2},
    'A': {'B': 1, 'D': 5},
    'B': {'D': 3, 'C': 2},
    'C': {'G': 4, 'D': 3},
    'D': {'G': 1},
}

#define start and goal nodes
start_node = 'S'
goal_node = 'G'
#call the A* tree search function
a_star_tree_search(graph, start_node, goal_node, heuristic)
