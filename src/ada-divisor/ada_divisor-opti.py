import numpy as np
import matplotlib.pyplot as plt

DATAPATH = "data/"
files = ['data-run-25.csv', 'data-run-40.csv', 'data-run-55.csv', 'data-run-70.csv', 'data-run-85.csv', 'data-run-100.csv']

# load data from text file
data = [0] * len(files)
for i, file in enumerate(files):
    data[i] = np.mean(np.genfromtxt("%s%s" % (DATAPATH, file), delimiter=','))

print(data)
# data[i] is the average epsiode required by certain epsilon
ada_divisor = [25, 40, 55, 70, 85, 100]

# plot data
plt.plot(ada_divisor,data)

plt.xlabel('ada_divisor')
plt.ylabel('mean Episode')
plt.title('find ada_divisor')
plt.legend()
plt.show()