from queue import Queue
import networkx as nx


def map_nodes(grid):
    nodes = [(1, 0), (len(grid[0]) - 2, len(grid) - 1)]
    for x in range(1, len(grid[0]) - 1):
        for y in range(1, len(grid) - 1):
            if grid[y][x] != "#":
                n = [(x + dx, y + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)] if grid[y + dy][x + dx] != "#"]
                if len(n) > 2:
                    nodes.append((x, y))
    nodemap = {}
    for n in nodes:
        paths = {}
        q = Queue()
        q.put((n, {n}))
        while not q.empty():
            p, path = q.get()
            if p != n and p in nodes and len(path):
                paths[p] = len(path) - 1
                continue
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = p
                xn = x + dx
                yn = y + dy
                pn = (xn, yn)
                if xn >= len(grid[0]) or xn < 0 or yn >= len(grid) or yn < 0 or grid[yn][xn] == "#" or pn in path:
                    continue
                path_new = set(path)
                path_new.add(pn)
                q.put((pn, path_new))
        nodemap[n] = paths

    return nodemap


def readInput23(infile):
    with open(infile) as f:
        return f.read().strip().splitlines()


def part2(infile):
    grid = readInput23(infile)
    S = (1, 0)
    E = (len(grid[0]) - 2, len(grid) - 1)
    nodemap = map_nodes(grid)
    G = nx.Graph()
    for n, c in nodemap.items():
        for m, d in c.items():
            G.add_edge(n, m)
    paths = []
    for p in nx.all_simple_paths(G, S, E):
        l = sum([nodemap[p[i]][p[i - 1]] for i in range(1, len(p))])
        paths.append(l)
    return max(paths)


print("Test 2:", part2("test.txt"))
# print("Input 2:", part2("input.txt"))
