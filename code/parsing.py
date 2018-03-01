
# parser


def read_file(file):
	f = open(file, "r")
	lines = f.read().split("\n")
	t = lines.pop(0).split(" ")
	tt = [int(x) for x in t]
	
	if(len(lines[-1]) < 2) : lines.pop()
	
	lines = [x.split(" ") for x in lines]
	
	for a in range(len(lines)):
		l = lines[a]
		for i in range(len(l)):
			l[i] = int(l[i])
		lines[a] = [(l[0], l[1]), (l[2], l[3]), l[4], l[5], abs(l[0] - l[2]) + abs(l[1] - l[3]), a ]
	
	# print(lines)
	
	return tt[0], tt[1], tt[2], tt[3], tt[4], tt[5], lines
	
# 3 4 2 3 2 10
# rides[0] = [(0, 0), (1, 3), 2, 9, 4, 0]
# rows, cols, nbVehicles, maxRides, bonus, maxSteps, rides  = read_file("../instances/a_example.in")
# print(rides)



def write_output(vehicles, output_file):
	out = open(output_file, "w")
	for v in range(len(vehicles)):
		out.write(str(v))
		for r in vehicles[v][0]:
			out.write(" " + str(r[5]))
		out.write("\n")