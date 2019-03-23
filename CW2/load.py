import numpy as np

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
    print(rho[0:100])
    print(intervals[0:100])
    return(stdev/mean)

#spikes=[int(x) for x in load_data("rho.dat")]
spikes=load_data("rho.dat",int)

print(len(spikes))
print(spikes[0:5])

#stimulus=[float(x) for x in load_data("stim.dat")]
stimulus=load_data("stim.dat",float)

print(len(stimulus))
print(stimulus[0:5])


