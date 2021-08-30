"""
ID: angela.14
LANG: PYTHON3
TASK: wormhole
"""

with open('wormhole.in', 'r') as fin:
    N = int(fin.readline().strip())
    nodes = []
    for i in range(N):
        info = fin.readline().strip().split(" ")
        nodes.append((int(info[0]), int(info[1])))

boundary = 1000000000


# pair all wormholes
def make_all_pairs(lst):
    if len(lst) < 2:
        yield []
        return
    else:
        a = lst[0]
        for i in range(1, len(lst)):
            pair = (a, lst[i])
            for rest in make_all_pairs(lst[1:i] + lst[i + 1:]):
                yield [pair] + rest


# given a point, get its pair
def get_pair(point, node):
    for j in range(int(N/2)):
        for i in range(2):
            if node[j][i] == point:
                return node[j][(i + 1) % 2]


next_points = {}


# find if it's the end of a loop. Return next point if not
def find_next(curr, system):
    if curr in next_points:
        return next_points[curr]
    next_p = (boundary, -1)
    for k in range(N):
        j = int(k % 2)
        portal = int((k - j)/2)
        if system[portal][j][1] == curr[1] and system[portal][j][0] > curr[0]:
            if system[portal][j][0] < next_p[0]:
                next_p = system[portal][j]
    if next_p == (boundary, -1):
        next_points[curr] = None
        return None
    next_points[curr] = next_p
    return next_p


# check if there is a loop given a starting point
def check_loop(portal, j, system):
    visited = set()
    current = system[portal][j]
    visited.add(current)
    current = find_next(get_pair(current, system), system)
    while current not in visited:
        if current is None:
            return False
        else:
            visited.add(current)
            current = find_next(get_pair(current, system), system)
    return True


nodes = list(make_all_pairs(nodes))
loops = 0
for i in range(len(nodes)):
    # check each node
    node = nodes[i]
    for k in range(N):
        j = int(k % 2)
        pair = int((k - j) / 2)
        # give point and system to check for loops
        if check_loop(pair, j, node):
            loops += 1
            break

with open('wormhole.out', 'w') as fout:
    fout.write(f"{loops}\n")