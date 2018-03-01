import random_rides as r
import parsing as p

rows, cols, nbVehicles, maxRides, bonus, maxSteps, rides  = p.read_file("../instances/a_example.in")
print(rides)

# rides = [[(0,0), (1,3), 2, 9, 4], [(1, 2), (1, 0), 0, 9, 2], [(2, 0), (2, 2), 0, 9, 2]]
sol = r.generate_random_rides(nbVehicles, rides, maxSteps, bonus)

score = 0
for s in sol:
	score += s[2]
	print(s)
print(score)