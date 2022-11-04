from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math
import pyzdde.zdde as pyz

ln = pyz.createLink()
ln.apr = True
# define aim function
def aimFunction(x):
    #y = x ** 3 - 60 * x ** 2 - 4 * x + 6
    ln.zSetSurfaceData(surfNum=2, code=ln.SDAT_THICK, value=x)
    value = abs(ln.zGetOperand(1, 10))
    return value

#初始化x 0~100
# x = [i / 10 for i in range(1000)]
#初始化y
# y = [0 for i in range(1000)]
# for i in range(1000):
#     y[i] = aimFunction(x[i])

# plt.plot(x, y)
T = 1000  # initiate temperature
Tmin = 10  # minimum value of temperature
x = np.random.uniform(low=0, high=1000)  # initiate x
k = 50  # times of internal circulation
y = 0  # initiate result
t = 0  # time
print(f'初始溫度:{T}, 停止溫度:{Tmin}, 初始厚度:{x}')
ybest=10000
xbest=10000
while T >= Tmin:
    for i in range(k):
        # calculate y
        y = aimFunction(x)
        # generate a new x in the neighboorhood of x by transform function
        xNew = x + np.random.uniform(low=-0.05, high=0.05)*T
        if (0 <= xNew and xNew <= 1000):
            yNew = aimFunction(xNew)
            if yNew<ybest:
                ybest=yNew
                xbest=xNew
            if yNew - y < 0:
                x = xNew
            else:
                # metropolis principle
                p = math.exp(-(yNew - y) / T)
                r = np.random.uniform(low=0, high=1)
                if r < p:
                    x = xNew

    t += 1
    print(f'溫度:{T}, Error:{ybest}, Thickness:{xbest}')
    if ybest<0.001:
        break
    #T = 1000 / (1 + t)  #降溫函數
    T = T*0.95  #降溫函數

print(x, aimFunction(x))
ln.close()
exit(0)