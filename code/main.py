import random_rides as r
import parsing as p

rows, cols, nbVehicles, maxRides, bonus, maxSteps, rides  = p.read_file("../instances/e_high_bonus.in")
print(rides)

# rides = [[(0,0), (1,3), 2, 9, 4], [(1, 2), (1, 0), 0, 9, 2], [(2, 0), (2, 2), 0, 9, 2]]
sol = r.generate_random_rides(nbVehicles, rides, maxSteps, bonus)

score = 0
for s in sol:
    score += s[2]
    print(s)
print(score)


def boucle(file):
    maxScore = 0
    resMax = []
    rows, cols, nbVehicles, maxRides, bonus, maxSteps, rides = p.read_file(file)
    while True:
        res = r.generate_random_rides(nbVehicles, rides, maxSteps, bonus)
        s = score(res)
        if s > maxScore:
            maxScore = s
            resMax = res
            print(maxScore)

def score(sol):
    score = 0
    for s in sol:
        score += s[2]
    return score