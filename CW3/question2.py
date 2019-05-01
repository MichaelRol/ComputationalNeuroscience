import random as rnd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math

v_reset = -0.08
v_thresh = -0.054
leak_pot = -0.07
d_t = 0.001
tau_m = 0.02
tau_s = 0.01
rmie = 0.018
rmgs = 0.15
p = 0.5 
v1_old = rnd.uniform(v_reset, v_thresh)
v2_old = rnd.uniform(v_reset, v_thresh)
e_s = -0.08
v1_vector = []
v2_vector = []
s1 = 0
s2 = 0

for _ in range(0, 1000):
    v1 = ((1 - (d_t/tau_m)) * v1_old) + (((leak_pot + rmie) * d_t) / tau_m) + (((rmgs * d_t) / tau_m) * s1 * (e_s - v1_old))
    v2 = ((1 - (d_t/tau_m)) * v2_old) + (((leak_pot + rmie) * d_t) / tau_m) + (((rmgs * d_t) / tau_m) * s2 * (e_s - v2_old))
    s1 *= 0.9
    s2 *= 0.9

    if(v1 > v_thresh):
        v1 = v_reset
        s2 += p
    if(v2 > v_thresh):
        v2 = v_reset
        s1 += p
    v1_old = v1
    v2_old = v2
    v1_vector.append(v1)
    v2_vector.append(v2)

xaxis = []
for x in range(0, 1000):
    xaxis.append(x)

plt.plot(xaxis, v1_vector, 'r', label = 'Neuron 1')
plt.plot(xaxis, v2_vector, 'b', label = 'Neuron 2')
plt.legend(loc='best')
plt.title('Voltage-Time graph for two Neurons with E_s = ' + str(e_s) + 'V', fontsize=22)
plt.xlabel('Time (ms)', fontsize=20)
plt.ylabel('Voltage (V)', fontsize=20)
plt.savefig('TwoNeurons.png')
plt.show()