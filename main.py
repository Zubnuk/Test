def get_shortest_path_dijkstra(dist_matrix: list[list[int]], source_idx: int,
                               target_idx: int) -> dict[str: int, list[int]]:
    """Calculates using Dijkstra's algorithm the shortest path between two
    vertices in an ordered graph.

    :param dist_matrix: an integer matrix with distances values.
    :param source_idx: index of the source vertex.
    :param target_idx: index of the target vertex.
    :raise Exception: when dist_matrix is not a square integer matrix, when
    the source_idx is equal to the target_idx, when the source_idx or the
    target_idx is great or equal to the number of vertices.
    :return: a dictionary with keys: distance - the shortest distance value,
    path - an ordered list of vertices indexes.
    """
    pass


def get_shortest_path_floyd_warshall(dist_matrix: list[list[int]],
                                     source_idx: int, target_idx: int) -> \
        dict[str: int, list[int]]:
    """Calculates using Floyd–Warshall's algorithm the shortest path between two
    vertices in an ordered graph.

    :param dist_matrix: an integer matrix with distances values.
    :param source_idx: index of the source vertex.
    :param target_idx: index of the target vertex.
    :raise Exception: when dist_matrix is not a square integer matrix, when
    the source_idx is equal to the target_idx, when the source_idx or the
    target_idx is great or equal to the number of vertices.
    :return: a dictionary with keys: distance - the shortest distance value,
    path - an ordered list of vertices indexes.
    """
    pass


def get_min_cost_path(price_table: list[list[int]]) ->\
        dict[str: int, str: list[tuple[int, int]]]:
    """Searches for the minimum cost path in the table. Each cell in the table
    has some price per visit.
    :param price_table: an integer matrix with cell price values.
    :raise Exception: when price_table is not an integer matrix.
    :return: a dictionary with keys: cost - the minimum value of the cost of the
    path, path - an ordered list of tuples with cell indices.
    """
    pass


def main():
    matrix = [[0, None, None],
              [1, 0, None],
              [None, 1, 0]]
    print(get_shortest_path_dijkstra(matrix, 2, 0))

    matrix = [[0, 2, 1],
              [None, 0, -2],
              [None, None, 0]]
    print(get_shortest_path_floyd_warshall(matrix, 0, 2))

    table = [[1, 2, 2],
             [3, 4, 2],
             [1, 1, 2]]
    print(get_min_cost_path(table))


if __name__ == '__main__':
    main()
