import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def power_law(x, k, n):
    return k * np.power(x, n)

initial_guess = [1, 0.6]  

N = []                #List with different monomer numbers
R_g_good = []         #List with radius of gyration at different monomer numbers 

fit_params, _ = curve_fit(power_law, N, R_g_good, p0=initial_guess)
k_fit, n_fit = fit_params

print("Best-fit parameters:")
print("k =", k_fit)
print("n =", n_fit)

Ni = [0.01*(i+1) for i in range(25600)]
f_N = [0 for i in range(len(Ni))]
for i in range(len(Ni)):
    f_N[i] = k_fit*((Ni[i])**n_fit)

y_err_values = []

for i in range(len(N)):
    y_err_values.append(np.abs(R_g_good[i]-f_N[1600*2**i - 1]))

plt.scatter(N, R_g_good)
plt.errorbar(N, R_g_good, yerr=y_err_values, fmt='o', capsize=3)
plt.plot(Ni, f_N, '--')
plt.xlabel('$N$')
plt.ylabel('$R_g$')
plt.legend()
plt.show()
