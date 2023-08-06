import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('sc_temp_1_energy.dat')
print(data[1,2])
time = []
KE = []
PE = []
TE = []
for i in range(len(data)):
    time.append(data[i,0])
    KE.append(data[i,1])
    PE.append(data[i,2])
    TE.append(data[i,3])

plt.plot(time,PE, label = 'Potential Energy')
plt.plot(time,KE, label = 'Kinetic Energy')
plt.plot(time,TE, label = 'Total Energy')
plt.xlabel('Time-steps')
plt.ylabel('Energy (in LJ Units)')
plt.title('Density = 0.5')
plt.legend()
plt.show()
