import numpy as np
import os
import matplotlib.mlab as mlab



buckets_lo, buckets_hi = 2, 4
step_size = 1
for i in mlab.frange(buckets_lo, buckets_hi, step_size):
	buckets = i
	os.system("python3 mountaincar.py --buckets {}".format(buckets))

print("Done")
	

