class Vertex:
    def __init__ (self, name):
        self.name = name
        self.adjacent = {}
    def get_name(self):
        return self.name
    def get_weight(self, neighbour):
        return self.adjacent[neighbour]
    def add_neighbor(self, neighbor, c):
        self.adjacent[neighbor] = c
    def get_connections(self):
        return self.adjacent.keys()
    
class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
    def add_vertex(self, name):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(name)
        self.vert_dict[name] = new_vertex
        return new_vertex

    def __iter__(self):
        return iter(self.vert_dict.values())

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None
        
    def add_edge(self, frm, to, c):
         if frm not in self.vert_dict:
            self.add_vertex(frm)
         if to not in self.vert_dict:
            self.add_vertex(to)
         self.vert_dict[frm].add_neighbor(self.vert_dict[to], c)
         self.vert_dict[to].add_neighbor(self.vert_dict[frm], c)
    
    def printGraph(self):
          for v in self:
            for w in v.get_connections():
                vid = v.get_name()
                wid = w.get_name()
                print(vid, wid, v.get_weight(w))


if __name__ == '__main__':

    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)  
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

  