from xml.dom import NoModificationAllowedErr


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + 'adjacent: ' + str([x.id for x in self.adjacent])
    
    def add_neighbor(self, neighbor, weight = 0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id
    
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.value())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex
    
    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None
    
    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)
        
        self.vert_dict[frm].addneighbor(self.vert_dict[to])

    def get_vertices(self):
        return self.vert_dict.keys()
    
    def minDistance(self, dist, sptSet):
        min = 1e7
        
        for v in range(self.V):
            if dist[v]<min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        
        return min_index
    
    def dijkstra(self, src):
        dist = [1e7]*self.num_vertices
        dist[src] = 0
        sptSet = [False]*self.num_vertices

        for cout in range(self.num_vertices):
            u = self.minDistance(dist, sptSet)

            sptSet[u] = True
            for v in range(self.num_vertices):
    