def valid_permut(route, v):
    t = 0
    pos = (0,0)
    for r in v[0]:
        if t + distance(pos, r[0]) + r[4] > r[3]:
            break
        t += distance(pos, r[0]) + r[4]
        pos = r[1]


def distance(d, e):
    return abs(d[0] - e[0]) + abs(d[1] - d[1])