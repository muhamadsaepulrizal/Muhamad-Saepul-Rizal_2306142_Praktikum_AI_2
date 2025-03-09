#BFS algorithm in python

import collections

#BFS algorithm
def bfs(graph, root):

  visited, queue = set(), collections.deque([root])
  visited.add(root)

  while queue:

    #dequeue a vertex from queue
    vertex = queue.popleft()
    print(str(vertex) + " ", end="")

    #if not visited, mark it is visited, and enqueue it
    for neighbour in graph[vertex]:
      if neighbour not in visited:
        visited.add(neighbour)
        queue.append(neighbour)

if __name__ == '__main__':
  graph = {0: [1,2], 1: [2], 2: [3], 3: [1,2]}
  print("following is Breadth first traversal")
  bfs(graph, 0)