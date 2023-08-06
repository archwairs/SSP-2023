import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('temp_den_3.dat')

print(data[5,1])

time_step = [i for i in range(8000,10001)]
temp = []

for i in range(8000,10001):
    temp.append(data[i,1])

t_total = 0
for i in range(len(temp)):
    t_total +=  temp[i]

t_f = t_total/(len(temp))
print(t_f)