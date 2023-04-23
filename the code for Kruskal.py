import disjointset_example as dst

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = []

    def add_edge(self, k, g, p):
        self.graph.append([k, g, p])

    def addNode(self, value):
        self.nodes.append(value)

    def printSolution(self, k, g, p):
        for k, g, p in self.MST:
            print("%k - %k: %k")

    def Kruskal_Algo(self):
        i, e = 0, 0
        ds = dst.DisjointSet(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.V - 1:
            k, g, p = self.graph[i]
            i =+ 1
            x = ds.find(k)
            y = ds.find(g)
            if x != y:
                e += 1
                self.MST.append([k, g, p])
                ds.union(x, y)
        self.printSolution(k, g, p) 

    def find(self, ds, k):
        return ds.find(k)  

g = Graph(5)
g.addNode = ("A")
g.addNode = ("B")
g.addNode = ("C")
g.addNode = ("D")
g.addNode = ("E")
g.add_edge("A", "B", 6)
g.add_edge("A", "C", 4)
g.add_edge("A", "D", 5)
g.add_edge("C", "B", 9)
g.add_edge("B", "E", 8)
g.add_edge("E", "C", 2)
g.add_edge("D", "E", 3)

g.Kruskal_Algo()