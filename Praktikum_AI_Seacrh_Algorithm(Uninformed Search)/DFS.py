#python3 program toprint DFS traversal
#from a given graph

from collections import defaultdict

#kelas ini merepresentasikan sebuah graf yang diarahkan
#menggunakan representasi daftar kejadian

class Graph:

  #konstruktor
  def __init__(self):

    #kamus default untuk menyimpan graf
    self.graph = defaultdict(list)

  #fungsi untuk menambahkan tepi ke graf
  def addEdge(self, u, v):
    self.graph[u].append(v)

  #fungsi yang digunakan oleh DFS
  def DFSUtil(self, v, visited):

    #tanda node saat ini sebagai sudah dikunjungi
    #dan cetak
    visited.add(v)
    print(v, end=' ')

    #panggil rekursif untuk semua titik ujung
    #yang berdekatan dengan titik ini
    for neighbour in self.graph[v]:
      if neighbour not in visited:
        self.DFSUtil(neighbour, visited)

  #fungsi untuk melakukan peelusuran DFS. ini menggunakan
  #DFSUtil() rekursif
  def DFS(self, v):

    #buat himpunan untuk menyimpan node yang sudah dikunjungi
    visited = set()

    #panggil fungsi bantu rekursif
    #untuk mencetak penelusuran DFS
    self.DFSUtil(v, visited)

#kode pengguna
if __name__ == "__main__":
  g = Graph()
  g.addEdge(0, 1)
  g.addEdge(0, 2)
  g.addEdge(1, 2)
  g.addEdge(2, 0)
  g.addEdge(2, 3)
  g.addEdge(3, 3)

  print("berikut adalah penelusuran Depth First (dimulai dari node 2)")

  #panggil fungsi
  g.DFS(2)

#code ini disumbangkan oleh neelam yadav