import numpy as np
import os
import matplotlib.mlab as mlab



min_alpha_lo, min_alpha_hi = 0.3, 0.9
step_size = 0.1
for i in mlab.frange(min_alpha_lo, min_alpha_hi, step_size):
	min_alpha = i
	os.system("python3 mountaincar.py --min_alpha {}".format(min_alpha))


print("Done")
	

