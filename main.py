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


def main():
    matrix = [[0, None, None],
              [1, 0, None],
              [None, 1, 0]]
    print(get_shortest_path_dijkstra(matrix, 2, 0))


if __name__ == '__main__':
    main()
