# -*- coding: utf-8 -*-
import pydot


class Render:

    def __init__(self):
        self.counter = 0
        self.graph = pydot.Dot(graph_type='digraph')

    def draw(self, parent_name, child_name):
        self.counter += 1
        graph = self.graph
        graph.add_node(
            pydot.Node(
                parent_name,
                label=parent_name.split('_')[0]
            ))
        graph.add_node(
            pydot.Node(
                child_name,
                label=child_name.split('_')[0]
            ))
        edge = pydot.Edge(parent_name, child_name)
        graph.add_edge(edge)

    def start(self, node, parent=None):
        for key, value in node.items():
            if isinstance(value, dict):
                key = key + '_' + str(self.counter)
                if parent:
                    self.draw(parent, key)
                self.start(value, key)
            else:
                # drawing the label using a distinct name
                value = value + '_' + str(self.counter)
                self.draw(parent, value)

    def finish(self, name):
        self.graph.write_png(name)
