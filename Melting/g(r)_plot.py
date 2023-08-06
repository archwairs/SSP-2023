import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt('gofr_den_0.1.dat')
data2 = np.loadtxt('gofr_temp_1.dat')
data3 = np.loadtxt('gofr_den_1.dat')
data4 = np.loadtxt('gofr_den_2.dat')
data5 = np.loadtxt('gofr_den_3.dat')


r1 = []
r2 = []
r3 = []
r4 = []
r5 = []
gr1 = []
gr2 = []
gr3 = []
gr4 = []
gr5 = []

for i in range(len(data1)):
    r1.append(data1[i,0])
    gr1.append(data1[i,1])
    r2.append(data2[i,0])
    gr2.append(data2[i,1])
    r3.append(data3[i,0])
    gr3.append(data3[i,1])
    r4.append(data4[i,0])
    gr4.append(data4[i,1])
    r5.append(data5[i,0])
    gr5.append(data5[i,1])

plt.text(3, 2.5, 'N = 10,000: a = 10', fontsize = 10)
plt.plot(r1,gr1, label = 'Density = 0.1: $T_{o}$ = 1: $T_{f}$ = 1.3686')
plt.plot(r2,gr2, label = 'Density = 0.5: $T_{o}$ = 1: $T_{f}$ = 0.8506')
plt.plot(r3,gr3, label = 'Density = 1: $T_{o}$ = 1: $T_{f}$ = 1.6875')
plt.plot(r4,gr4, label = 'Density = 2: $T_{o}$ = 1: $T_{f}$ = 25.9429')
plt.plot(r5,gr5, label = 'Density = 3: $T_{o}$ = 1: $T_{f}$ = 133.7768', c = 'g')
plt.xlabel("r")
plt.ylabel("g(r)")
plt.axhline(y = 1, color = 'r', linestyle = '--')
plt.title('g(r) v/s r at different densities')
plt.legend()
plt.show()