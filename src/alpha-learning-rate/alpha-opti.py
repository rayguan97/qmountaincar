import numpy as np
import matplotlib.pyplot as plt

DATAPATH = "data/"
files = ['data-run-0.3.csv', 'data-run-0.4.csv', 'data-run-0.5.csv', 'data-run-0.6.csv', 'data-run-0.7.csv', 'data-run-0.8.csv', 'data-run-0.9.csv']

# load data from text file
data = [0] * len(files)
for i, file in enumerate(files):
    data[i] = np.mean(np.genfromtxt("%s%s" % (DATAPATH, file), delimiter=','))

print(data)
# data[i] is the average epsiode required by certain epsilon
alpha = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

# plot data
plt.plot(alpha,data)

plt.xlabel('alpha')
plt.ylabel('mean Episode')
plt.title('find best alpha')
plt.legend()
plt.show()