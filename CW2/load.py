import numpy as np
import matplotlib.pyplot as plt

def load_data(filename,T):

    data_array = [T(line.strip()) for line in open(filename, 'r')]

    return data_array

def CoV(rho):
    intervals = []
    time = 0
    for x in rho:
        if x == 1:
            intervals.append(time)
            time = 0
        time += 0.002
    mean = np.mean(intervals)
    stdev = np.std(intervals)
    return(stdev/mean)

def FanoFactor(rho, width):
    counts = []
    for x in range(0, len(rho), width/2):
        count = 0
        for y in range(0, width/2):
            if rho[x+y] == 1:
                count += 1
        counts.append(count)
    mean = np.mean(counts)
    var = np.std(counts) * np.std(counts) 
    return(var/mean)

def SpikeAvg(spikes, stim):
    count = 0
    total = [0] * 50
    curr = [0] * 50
    for x in range(50, len(spikes)):
        if spikes[x] == 1:
            count += 1
            curr = stim[x-50: x - 1]
            for i in range(0, len(curr)):
                total[i] += curr[i]
    for y in range(0, len(total)):
        total[y] = total[y]/count
    return total


#spikes=[int(x) for x in load_data("rho.dat")]
spikes=load_data("rho.dat",int)

print(len(spikes))
print(spikes[0:5])

#stimulus=[float(x) for x in load_data("stim.dat")]
stimulus=load_data("stim.dat",float)

print(len(stimulus))
print(stimulus[0:5])

print("Coefficient of Variation: ")
print(CoV(spikes))
print("Fano Factor 10ms: ")
print(FanoFactor(spikes, 10))
print("Fano Factor 50ms: ")
print(FanoFactor(spikes, 50))
print("Fano Factor 100ms: ")
print(FanoFactor(spikes, 100))

xaxis = []
for x in range(0, 50):
    xaxis.append(x * 2)

plt.plot(xaxis, SpikeAvg(spikes, stimulus))
plt.title('Spike Triggered Average')
plt.xlabel('time/ms')
plt.show()
