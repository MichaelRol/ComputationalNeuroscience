import matplotlib.pyplot as plt

v_reset = -0.07
v_thresh = -0.04
leak_pot = -0.07
mem_res = 10000000
d_t = 0.001
i_e = 0.0000000031
tau = 0.01
v_vector = []
v_old = i_e
for _ in range(0, 1000):
    v=v_old + (leak_pot-v_old+ mem_res *i_e )* d_t / tau
    if v > v_thresh:
        v = v_reset
    v_old = v
    v_vector.append(v)

xaxis = []
for x in range(0, 1000):
    xaxis.append(x)

plt.plot(xaxis, v_vector)
plt.title('Integrate and Fire Model')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.savefig('IandF.png')
plt.show()