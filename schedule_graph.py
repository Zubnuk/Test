import random
from typing import Optional
import networkx as nx
import matplotlib.pyplot as plt

from custom_exception import ArgumentException


DEFAULT_TREE_COUNT = 3
DEFAULT_VERTEX_COUNT = 15


class ScheduleGraph:

    """
    Generates graph vertex list
    """
    @staticmethod
    def __generate_random_vertex_list(vertex_count: int) -> list[str]:
        vertex_list = list()
        letter_code = 65
        num = 0
        for i in range(vertex_count):
            if letter_code > 90:
                letter_code = 65
            vertex_list.append(chr(letter_code) + str(num))
            num += 1
            letter_code += 1
        return vertex_list

    @staticmethod
    def generate_random_forest(tree_count: Optional[int] = None,
                               vertex_count: Optional[int] = None) -> nx.Graph:
        if tree_count <= 0 or vertex_count <= 0 or type(tree_count) != int or type(vertex_count) != int:
            raise ArgumentException('Tree count and vertex count must be an integer more than zero')
        if tree_count > vertex_count:
            raise ArgumentException('Tree count must be not more than vertex count')
        colors = ['blue', 'blueviolet', 'darkorange', 'darkseagreen', 'fuchsia', 'green', 'lawngreen',
              'lightpink', 'mintcream', 'red', 'salmon', 'turquoise', 'darkslateblue', 'yellow',
              'plum', 'orangered', 'mistyrose', 'gray', 'sandybrown']
        graph = nx.DiGraph()
        vertex_list = ScheduleGraph.__generate_random_vertex_list(vertex_count)
        stock_list = [vertex_list[i] for i in range(tree_count)]
        vertex_list = vertex_list[tree_count:]
        vertex_count -= tree_count
        stock_index = 0
        for i in range(tree_count):
            this_color = colors[random.randint(0, len(colors) - 1)]
            colors.remove(this_color)
            graph.add_node(stock_list[stock_index], color=this_color)
            added_vertex_list = [stock_list[stock_index]]
            this_vertex_count = random.randint(0, vertex_count) if i != tree_count - 1 else vertex_count
            vertex_count -= this_vertex_count
            if this_vertex_count == 0:
                stock_index += 1
                continue
            this_vertex_list = vertex_list[:this_vertex_count]
            while len(this_vertex_list) != 0:
                start_vertex = added_vertex_list[random.randint(0, len(added_vertex_list) - 1)]
                finish_vertex = this_vertex_list[random.randint(0, len(this_vertex_list) - 1)]
                graph.add_node(finish_vertex, color=this_color)
                graph.add_edge(finish_vertex, start_vertex)
                added_vertex_list.append(finish_vertex)
                this_vertex_list.remove(finish_vertex)
                vertex_list.remove(finish_vertex)
            stock_index += 1
        return graph

    @staticmethod
    def show_plot(graph: nx.Graph) -> None:
        color_map = [graph.nodes[name]['color'] for name in graph.nodes]
        nx.draw_planar(graph, with_labels=True, node_color=color_map)
        plt.show()

def __usage_example():
    ScheduleGraph.show_plot(ScheduleGraph.generate_random_forest(DEFAULT_TREE_COUNT, DEFAULT_VERTEX_COUNT))

if __name__ == '__main__':
    __usage_example()
