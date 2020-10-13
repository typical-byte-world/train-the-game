import numpy as np
import matplotlib.pyplot as pp

filename = "training_data.txt"

data = []
with open(filename) as f:
	for line in f.readlines():
		line = list(map(float, line.strip().split(" ")))
		data.append(line)

data = np.matrix(data)

pp.plot(data[:, 0], label="road#1")
pp.plot(data[:, 1], label="road#2")
pp.plot(data[:, 2], label="car_x")
pp.plot(data[:, 2] - data[:, 1], label="diff")
pp.plot(data[:, 3]*5, label="car_angle")
pp.legend()
pp.grid(True)
pp.show()