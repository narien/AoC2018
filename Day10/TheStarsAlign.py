import re
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = []
        for line in f.readlines():
            l = [int(d) for d in re.findall(r'-?\d+', line)]
            input.append(l)
    data = np.array(input, dtype=int)
    positions = data[:,:2]
    velocities = data[:,2:]

    for _ in range(10867): #10867 iterations required
        positions += velocities

    plt.plot(positions[:,0], positions[:,1], '*')
    plt.show()

