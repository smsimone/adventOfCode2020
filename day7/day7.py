import json

to_find = "shiny_gold"
rules = {}


class Graph(object):
    def __init__(self):
        self.arches = []
        self.vertexes = {}

    def add_node(self, node):
        '''
        se il colore del nodo non è ancora stato inserito fra i vertici, lo aggiungo
        altrimenti recupero il nodo che era stato salvato tra i vertici
        '''
        oldnode = node
        if node.color not in self.vertexes:
            self.vertexes[node.color] = node
        else:
            '''
            se sto recuperando un nodo vecchio aggiungo tutti i nuovi nodi padri/figli
            '''
            oldnode = self.vertexes[node.color]
            oldnode.append_children(node.children)
            oldnode.append_parents(node.parents)

    def print_graph(self):
        values = map(lambda key: self.vertexes[key], self.vertexes.keys())
        for vertex in values:
            children = [child[1]
                        for child in self.arches if child[0] is vertex]
            print([x.color for x in vertex.parents], "=>", vertex.color,
                  "=>", [x.color for x in children])

    def print_arches(self):
        for arch in self.arches:
            print(arch[0], "=>", arch[1])

    def print_vertexes(self):
        for key in self.vertexes:
            vertex = self.vertexes[key]
            print(vertex.parents, "=>", vertex.color, "=>", vertex.children)


class Node(object):
    def __init__(self, color, children):
        self.color = color
        self.children = children
        self.parents = []

    def add_parent(self, parent):
        self.parents.append(parent)

    def append_children(self, children):
        for child in children:
            self.children.append(child)
        self.children = list(set(self.children))

    def append_parents(self, parents):
        for parent in parents:
            self.parents.append(parent)
        self.parents = list(set(self.parents))

    def to_string(self):
        return "{} => {} => {}".format(self.parents, self.color, self.children)


if __name__ == '__main__':
    graph = Graph()
    # mi carico la mappa contenente tutte le regole
    with open('/Users/smaso/Desktop/adventOfCode2020/day7/test_input.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            components = line.split(":")
            color = components[0].strip().replace(" ", "_")
            underbags = [x.strip() for x in components[1].strip().split(",")]
            under_bags = []
            if "other" not in line:
                for underbag in underbags:
                    under_components = underbag.split(" ")[1:]
                    under_bags.append("{}_{}".format(
                        under_components[0], under_components[1]))
            rules[color] = under_bags
            node = Node(color, under_bags)
            graph.add_node(node)

    graph.print_vertexes()
