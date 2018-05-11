import numpy as np
import os
import matplotlib.mlab as mlab



ada_divisor_lo, ada_divisor_hi = 25, 100
step_size = 15
for i in mlab.frange(ada_divisor_lo, ada_divisor_hi, step_size):
	ada_divisor = i
	os.system("python3 mountaincar.py --ada_divisor {}".format(ada_divisor))

print("Done")
	

