import csv
import matplotlib
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

csv_read = csv.reader(open('log.txt'), delimiter=',')

m = {1000:[], 2000:[], 3000:[], 4000:[], 5000:[]}
avgd = {1000:[], 2000:[], 3000:[], 4000:[], 5000:[]} 
sp = {1000:[], 2000:[], 3000:[], 4000:[], 5000:[]}
for row in csv_read:
    #import ipdb ; ipdb.set_trace()
    for i, col in enumerate(row):

        # 1 - M
        # 2 - N
        # 3 - size
        # 4 - degree min
        # 5 - degree max
        # 6 - shortestpath
        # 7 - 2/3
        sz = int(row[3])
        m_rw = int(row[1])
        avgd_rw = np.mean([int(row[4]), int(row[5])])
        sp_rw = float(row[6])

        m[sz].append(m_rw)
        avgd[sz].append(avgd_rw)
        sp[sz].append(sp_rw)







fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(m[1000], avgd[1000], sp[1000], c='r', marker='x', label='1000')
ax.scatter(m[2000], avgd[2000], sp[2000], c='g', marker='+', label='2000')
ax.scatter(m[3000], avgd[3000], sp[3000], c='b', marker='1', label='3000')
ax.scatter(m[4000], avgd[4000], sp[4000], c='purple', marker='2', label='4000')
ax.scatter(m[5000], avgd[5000], sp[5000], c='c', marker='3', label='5000')


ax.set_xlabel('M')
ax.set_ylabel('Average degree')
ax.set_zlabel('Shortest path time')

ax.legend()

plt.show()
