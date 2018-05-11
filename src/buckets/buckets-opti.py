import numpy as np
import matplotlib.pyplot as plt

DATAPATH = "data/"
files = ['data-run-2.csv', 'data-run-3.csv', 'data-run-4.csv', 'data-run-5.csv', 'data-run-6.csv', 'data-run-7.csv', 
			'data-run-8.csv', 'data-run-9.csv', 'data-run-10.csv']

# load data from text file
data = [0] * len(files)
for i, file in enumerate(files):
    data[i] = np.mean(np.genfromtxt("%s%s" % (DATAPATH, file), delimiter=','))

print(data)
# data[i] is the average epsiode required by certain epsilon
buckets = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# plot data
plt.plot(buckets,data)

plt.xlabel('buckets')
plt.ylabel('mean Episode')
plt.title('find best buckets')
plt.legend()
plt.show()