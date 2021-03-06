import csv
import matplotlib
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

csv_read = csv.reader(open('log.txt'), delimiter=',')

n = {1000:[], 2000:[], 3000:[], 4000:[], 5000:[]}
avgd = {1000:[], 2000:[], 3000:[], 4000:[], 5000:[]} 
for row in csv_read:
    #import ipdb ; ipdb.set_trace()
    for i, col in enumerate(row):
        
        # 0 - <>
        # 1 - M
        # 2 - N
        # 3 - size
        # 4 - degree min
        # 5 - degree max
        # 6 - shortestpath
        # 7 - 2/3
        sz = int(row[3])
        n_rw = int(row[2])
        avgd_rw = np.mean([int(row[4]), int(row[5])])

        n[sz].append(n_rw)
        avgd[sz].append(avgd_rw)



fig = plt.figure()
ax = fig.add_subplot(111)

ax.scatter(n[1000], avgd[1000], c='r', marker='o', label='1000')
ax.scatter(n[2000], avgd[2000], c='g', marker='o', label='2000')
ax.scatter(n[3000], avgd[3000], c='b', marker='o', label='3000')
ax.scatter(n[4000], avgd[4000], c='y', marker='o', label='4000')
ax.scatter(n[5000], avgd[5000], c='c', marker='o', label='5000')

ax.set_xscale('log')
ax.set_xticklabels([1,2,3,10,100])
ax.set_xticks([1,2,3,10,100])

ax.set_xlabel('N')
ax.set_ylabel('Average degree')

ax.legend()

plt.show()
