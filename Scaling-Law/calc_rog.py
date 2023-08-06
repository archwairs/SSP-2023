import numpy as np
import matplotlib.pyplot as plt

filename = 'pos_n_good.dump'     #dump file generated via LAMMPS
#f = open ("rg_16(zigzag).txt","a")
data = []
N = n               #n needs to be replaced with the number of monomers in a chain
with open(filename, 'r') as file:
    for line in file:
        line = line.strip()  # Remove leading/trailing whitespace
        if line and not line.startswith("ITEM:"):  # Skip non-empty lines starting with "ITEM:"
            values = line.split()  # Split the line into individual values
            try:
                numeric_values = [float(value) for value in values]  # Convert values to float
                data.append(numeric_values)
            except ValueError:
                pass  # Skip lines with non-numeric values

timestep = [data[(N+5)*i][0] for i in range(int(len(data)/(N+5)))]

r = []

for i in range(int(len(data)/(N+5))):
    for j in range(N):
        r.append(data[(N+5)*i + 5 + j][2:5])
r_com = []

for i in range(len(timestep)):
    x_sum = 0
    y_sum = 0
    z_sum = 0
    for j in range(N):
        r_temp = r[N*i:N*(i+1)][j]
        x_sum += r_temp[0]
        y_sum += r_temp[1]
        z_sum += r_temp[2]
    r_c = [x_sum/N, y_sum/N, z_sum/N]
    r_com.append(r_c)

print(len(r_com))

rg = []

for i in range(len(timestep)):
    r_diff_sq_sum = 0
    for k in range(N):
        for j in range(3):
            r_diff_sq = (r[N*i:N*(i+1)][k][j] - r_com[i][j])**2
            r_diff_sq_sum += r_diff_sq
    rg.append(np.sqrt(r_diff_sq_sum/N))

print(rg)

rg_eqm_sum = 0
for i in range(int(0.9*len(timestep)), len(timestep)):
    rg_eqm_sum += rg[i]

rg_eqm_av = rg_eqm_sum/(0.1*len(timestep))
print(rg_eqm_av)
#for i in range(len(rg)):
#    f.write('\n' + str(rg[i]))
