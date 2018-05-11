import numpy as np
import os
import matplotlib.mlab as mlab



min_epsilon_lo, min_epsilon_hi = 0.0, 0.3
step_size = 0.03
for i in mlab.frange(min_epsilon_lo, min_epsilon_hi, step_size):
	min_epsilon = i
	os.system("python3 mountaincar.py --min_epsilon {}".format(min_epsilon))

print("Done")
	

