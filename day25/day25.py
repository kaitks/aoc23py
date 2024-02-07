import networkx as nx


def day25(file: str) -> int:
    with open(file, "r") as file:
        contents = file.read()

    g = nx.Graph()

    for line in contents.splitlines():
        node, adjacent = line.split(":")
        for r in adjacent.strip().split(" "):
            g.add_edge(node, r)
            g.add_edge(r, node)

    edges = nx.minimum_edge_cut(g)
    g.remove_edges_from(edges)
    cc1, cc2 = nx.connected_components(g)
    total = len(cc1) * len(cc2)
    print(total)
    return total


day25("test.txt")
day25("input.txt")
