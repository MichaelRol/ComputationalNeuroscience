import random as rnd
import numpy as np

def get_spike_train(rate,big_t,tau_ref):

    if 1<=rate*tau_ref:
        print("firing rate not possible given refractory period f/p")
        return []


    exp_rate=rate/(1-tau_ref*rate)

    spike_train=[]

    t=rnd.expovariate(exp_rate)

    while t< big_t:
        spike_train.append(t)
        t+=tau_ref+rnd.expovariate(exp_rate)

    return spike_train

def CoV(spike_train):
    intervals = [spike_train[0]]
    for i in range(0, len(spike_train) - 1):
        intervals.append(spike_train[i+1] - spike_train[i])
    mean = np.mean(intervals)
    stdev = np.std(intervals)
    return(stdev/mean)
    
def FanoFactor(spike_train, big_t, width):
    counts = [0] * int(round(big_t/width))
    window_num = 0 
    for spike in spike_train:
        while True:
            if spike < (window_num + 1) * width:
                counts[window_num] += 1
                break
            else:
                window_num += 1
    mean = np.mean(counts)
    var = np.std(counts) * np.std(counts) 
    return(var/mean)


Hz=1.0
sec=1.0
ms=0.001

rate=35.0 *Hz
tau_ref=5*ms

big_t=1000*sec

spike_train=get_spike_train(rate,big_t,tau_ref)

print("CoV: ")
print(CoV(spike_train))
print("Fano 10ms Width:")
print(FanoFactor(spike_train, big_t, 10*ms))
print("Fano 50ms Width:")
print(FanoFactor(spike_train, big_t, 50*ms))
print("Fano 100ms Width:")
print(FanoFactor(spike_train, big_t, 100*ms))

# print(len(spike_train)/big_t)
# print(spike_train)