from collections import defaultdict
import numpy as np
import re

def fillDatastructure(lines, guards):
    lines.sort()
    currentGuard = 0
    fellAsleep = 0
    inputPattern = re.compile(':([0-9]{2})] ([A-Z,a-z]*)( #[0-9]*)?')
    for line in lines:
        m = inputPattern.search(line)
        if m.group(2) == 'Guard':
            currentGuard = int(m.group(3)[2:])
        elif m.group(2) == 'falls':
            fellAsleep = int(m.group(1))
        else:
            guards[currentGuard][fellAsleep:int(m.group(1))] += 1

def stratType(guards, func):
    worstGuard = 0
    sleepHighscore = 0
    for guard in guards:
        maxSleep = func(guards[guard])
        if maxSleep > sleepHighscore:
            worstGuard = guard
            sleepHighscore = maxSleep

    mostOftenAsleep = np.argmax(guards[worstGuard])
    print('Worst guard and best time checksum: ' + str(worstGuard*mostOftenAsleep))


# Run program with input.txt in same folder.
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    guards = defaultdict(lambda: np.zeros(60, dtype=int))
    fillDatastructure(lines, guards)
    stratType(guards, sum)
    stratType(guards, max)
