from queue import PriorityQueue

#fungsi untuk merekonstruksi jalur
def reconstruct_path(came_from, start, goal):
  current = goal
  path = []

  while current != start:
    path.append(current)
    current = came_from[current]

  path.append(start)
  path.reverse()
  return path

#fungsi algoritma Greedy Best-First Search
def greedy_search(graph, start, goal):
  frontier = PriorityQueue() #Antrian prioritas
  frontier.put((heuristic[start], start)) #tambahkan simpul awal
  came_from = {} #menyimpan jalur
  explored = set() #menyimpan simpul yang sudah dikunjungi

  while not frontier.empty():
    _, current_node = frontier.get() #ambil simpul dengan nilai heuristik terkecil

    if current_node == goal:
      print("simpul tujuan ditemukan")
      path = reconstruct_path(came_from, start, goal)
      print("jalur terpendek: ", path)
      return path #kembalikan jalur yang ditemukan

    explored.add(current_node)

    for neighbor in graph[current_node]:
      if neighbor not in explored:
        frontier.put((heuristic[neighbor], neighbor))
        came_from[neighbor] = current_node #simpan jalur

  print("simpul tujuan tidak ditemukan!")
  return None

#heuristik
heuristic = {
      'A': 4,
      'B': 3,
      'C': 3,
      'D': 1,
      'S': 6,
      'G': 0,
  }

graph = {
      'S': ['A', 'B'],
       'A': ['B', 'D'],
       'B': ['D', 'C'],
       'C': ['D', 'G'],
       'D': ['G'],
}



#titik awal dan tujuan
start_node = 'S'
goal_node = 'G'
#panggil fungsi greedy search
greedy_search(graph, start_node, goal_node)

