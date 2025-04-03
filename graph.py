from node import *
from segment import *

import matplotlib.pyplot as plt
import math

class Graph:
    def __init__(self):
        self.node = []
        self.segment = []

def AddNode(g, n):
    if n in g.node:
        return False
    g.node.append(n)
    return True

def AddSegment(g, nameOriginNode, nameDestinationNode):
    origin = None
    destination = None
    i = 0
    while i < len(g.node) and (origin is None or destination is None):
        if g.node[i].name == nameOriginNode:
            origin = g.node[i]
        elif g.node[i].name == nameDestinationNode:
            destination = g.node[i]
        i = i + 1
    if origin and destination:
        origin.AddNeighbor(destination)
        return True
    return False

def GetClosest(g, x, y):
    if not g.node:
        return None
    closest = g.node[0]
    minimo = Distance(g.node[0], closest)
    i = 1
    while i < len(g.node):
        node = g.node[i]
        d = Distance(node, closest)
        if d < minimo:
            minimo = d
            closest = node
        i = i + 1
    return closest

def Plot(g):
    for node in g.node:
        plt.scatter(node.coordinate_x, node.coordinate_y, label = node.name)
        plt.text(node.coordinate_x, node.coordinate_y, node.name)

    for segment in g.segment:
        x_values = [segment.origin.coordinate_x, segment.destination.coordinate_x]
        y_values = [segment.origin.coordinate_y, segment.destination.coordinate_y]
        plt.plot(x_values, y_values)

        mid_x = (segment.origin.coordinate_x + segment.destination.coordinate_x) / 2
        mid_y = (segment.origin.coordinate_y + segment.destination.coordinate_y) / 2
        plt.text(mid_x, mid_y, f"{segment.cost:.2f}")

    plt.title("Gráfico con nodos y segmentos")
    plt.grid(True)

def PlotNode(g, nameOrigin):
    origin_node = None
    for node in g.node:
        if node.name == nameOrigin:
            origin_node = node
    if origin_node is None:
        return False
    for node in g.node:
        if node == origin_node:
            plt.scatter(node.coordinate_x, node.coordinate_y, color='blue')
            plt.text(node.coordinate_x, node.coordinate_y, node.name)
        elif node == origin_node.neighbor:
            plt.scatter(node.coordinate_x, node.coordinate_y, color='green')
            plt.text(node.coordinate_x, node.coordinate_y, node.name)
        else:
            plt.scatter(node.coordinate_x, node.coordinate_y, color='gray')
            plt.text(node.coordinate_x, node.coordinate_y, node.name)
    for neighbor in origin_node.neighbors:
        x_values = [origin_node.coordinate_x, neighbor.coordinate_x]
        y_values = [origin_node.coordinate_y, neighbor.coordinate_y]
        plt.plot(x_values, y_values, color='red')
        mid_x = (origin_node.coordinate_x + neighbor.coordinate_x) / 2
        mid_y = (origin_node.coordinate_y + neighbor.coordinate_y) / 2
        plt.text(mid_x, mid_y, f'{cost:.2f}')
    return True

    plt.title("Gráfico con nodos y segmentos")
    plt.grid(True)