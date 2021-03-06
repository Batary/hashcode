import random_rides as r
import parsing as p
from datetime import datetime

# rows, cols, nbVehicles, maxRides, bonus, maxSteps, rides = p.read_file("../instances/a_example.in")

# rides = [[(0,0), (1,3), 2, 9, 4], [(1, 2), (1, 0), 0, 9, 2], [(2, 0), (2, 2), 0, 9, 2]]
# sol = r.generate_random_rides(nbVehicles, rides, maxSteps, bonus)
#
# score = 0
# for s in sol:
# 	score += s[2]
# 	print(s)
# print(score)
#
#p.write_output([], str())


def boucle(file):
    maxScore = 0
    resMax = []
    rows, cols, nbVehicles, maxRides, bonus, maxSteps, ri = p.read_file(file)
    i = 0
    while True:
        rides = ri.copy()
        res = r.generate_random_rides(nbVehicles, rides, maxSteps, bonus)
        s = score(res)
        if s > maxScore:
            maxScore = s
            resMax = res
            print(maxScore)
            i+=1
            p.write_output(resMax, "../out/" + str(i) + " - " + str(s))


def score(sol):
    score = 0
    for s in sol:
        score += s[2]
    return score


boucle("../instances/e_high_bonus.in")
