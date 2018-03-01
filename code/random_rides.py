import random as rand


def generate_random_rides(nb_vehicles, rides, t_max, bonus):
    assign_rides = list()
    nb = 0
    j = 0
    while nb < nb_vehicles:
        nb = 0
        for i in range(0, nb_vehicles):
            if j == 0:
                pos = (0, 0)
                score = 0
                t = 0
            else:
                pos = assign_rides[i][1]
                score = assign_rides[i][2]
                t = assign_rides[i][3]
            sol = find_possible_rides(pos, t, rides)
            if not sol:
                nb += 1
                continue
            ride = rand.choice(sol)
            new_pos = ride[1]
            new_score = score + ride[4]
            if t + distance(pos, ride[0]) <= ride[2]:
                new_score += bonus
            new_t = ride_final(pos, t, ride)
            if new_t > t_max:
                nb += 1
                continue
            if j == 0:
                assign_rides.append(([ride], new_pos, new_score, new_t))
            else:
                l = assign_rides[i][0]
                l.append(ride)
                new_tuple = (l, new_pos, new_score, new_t)
                assign_rides[i] = new_tuple
            rides.remove(ride)
        j += 1
    return assign_rides


def find_possible_rides(pos, t, rides):
    rides_res = list()
    for r in rides:
        time = distance(pos, r[0]) + r[4]
        if time >= 50:
            continue
        if t + time + 1 < r[3]:
            rides_res.append(r)
    return rides_res


def distance(d, e):
    return abs(d[0] - e[0]) + abs(d[1] - d[1])


def ride_final(pos, t, ride):
    t_in_start = t + distance(pos, ride[0])
    if t_in_start < ride[2]:
        return ride[2] + ride[4]
    return t_in_start + ride[4]