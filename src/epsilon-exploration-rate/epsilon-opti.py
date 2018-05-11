import numpy as np
import matplotlib.pyplot as plt

DATAPATH = "data/"
files = ['data-run-0.0.csv', 'data-run-0.03.csv', 'data-run-0.06.csv', 'data-run-0.09.csv', 'data-run-0.12.csv' ,'data-run-0.15.csv','data-run-0.18.csv','data-run-0.21.csv',
'data-run-0.24.csv','data-run-0.27.csv','data-run-0.3.csv']

# load data from text file
data = [0] * len(files)
for i, file in enumerate(files):
    data[i] = np.mean(np.genfromtxt("%s%s" % (DATAPATH, file), delimiter=','))

print(data)
# data[i] is the average epsiode required by certain epsilon
epsilon = [0.0,0.03,0.06,0.09,0.12,0.15,0.18,0.21,0.24,0.27,0.3]

# plot data
plt.plot(epsilon,data)

plt.xlabel('epsilon')
plt.ylabel('mean Episode')
plt.title('find best epsilon')
plt.legend()
plt.show()