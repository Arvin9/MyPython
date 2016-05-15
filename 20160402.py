# -*- coding: utf-8 -*- #
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#起始位置
X = [1]
Y = [1]
Z = [1]

#初始速度
V = 1
#速度方向
Dx = 1
Dy = 1
Dz = 1

#重力加速度
G = -1

dt = 0.1

i = 1
while i < 10:
#速度分量
    Vx = (Dx*V)/math.sqrt(Dx*Dx + Dy*Dy + Dz*Dz)
    Vy = (Dx*V)/math.sqrt(Dx*Dx + Dy*Dy + Dz*Dz)
    Vz = (Dx*V)/math.sqrt(Dx*Dx + Dy*Dy + Dz*Dz) + G*dt

    X.append(X[-1] + Vx*dt)
    Y.append(Y[-1] + Vy*dt)
    Z.append(Z[-1] + Vz*dt)

    i = i + 1

print X
print Y
print Z


ax.scatter(X, Y, Z)
plt.show()
