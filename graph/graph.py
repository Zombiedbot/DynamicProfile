import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure()
ax1 = fig.add_subplot(1, 3, 1, projection = '3d')
n = np.linspace(1, 7, 7)
m = np.linspace(1, 10000, 100)
N, M = np.meshgrid(n, m)
file = open("output.txt", "r")
Z = []
for j in file:
    Z.append(np.array([float(k) for k in j.split()]))
Z = np.transpose(np.array(Z))
ax1.set_title("Dynamic profile")
ax1.set_xlabel("n")
ax1.set_ylabel("m")
ax1.set_zlabel("time")
ax1.plot_wireframe(N, M, Z)

ax2 = fig.add_subplot(1, 3, 2, projection = '3d')
n = np.linspace(1, 6, 6)
m = np.linspace(1, 6, 6)
N, M = np.meshgrid(n, m)
file = open("output1.txt", "r")
Z = []
for j in file:
    Z.append(np.array([float(k) for k in j.split()]))
Z = np.transpose(np.array(Z))
ax2.set_title("Native algorithm")
ax2.set_xlabel("n")
ax2.set_ylabel("m")
ax2.set_zlabel("time")
ax2.plot_wireframe(N, M, Z)

ax3 = fig.add_subplot(1, 3, 3, projection = '3d')
n = np.linspace(1, 8, 8)
m = np.linspace(1, 10000, 101)
N, M = np.meshgrid(n, m)
file = open("output2.txt", "r")
Z = []
for j in file:
    Z.append(np.array([float(k) for k in j.split()]))
Z = np.array(Z)
Z = np.transpose(Z)
ax3.set_title("Linear algebra")
ax3.set_xlabel("n")
ax3.set_ylabel("m")
ax3.set_zlabel("time")
ax3.plot_wireframe(N, M, Z)

plt.show()
