from collections import defaultdict

def addr(register, a, b, c):
    register[c] = register[a] + register[b]

def addi(register, a, b, c):
    register[c] = register[a] + b

def mulr(register, a, b, c):
    register[c] = register[a] * register[b]

def muli(register, a, b, c):
    register[c] = register[a] * b

def banr(register, a, b, c):
    register[c] = register[a] & register[b]

def bani(register, a, b, c):
    register[c] = register[a] & b

def borr(register, a, b, c):
    register[c] = register[a] | register[b]

def bori(register, a, b, c):
    register[c] = register[a] | b

def setr(register, a, b, c):
    register[c] = register[a]

def seti(register, a, b, c):
    register[c] = a

def gtir(register, a, b, c):
    if a > register[b]:
        register[c] = 1
    else:
        register[c] = 0

def gtri(register, a, b, c):
    if register[a] > b :
        register[c] = 1
    else:
        register[c] = 0

def gtrr(register, a, b, c):
    if register[a] > register[b] :
        register[c] = 1
    else:
        register[c] = 0

def eqir(register, a, b, c):
    if a == register[b]:
        register[c] = 1
    else:
        register[c] = 0

def eqri(register, a, b, c):
    if register[a] == b:
        register[c] = 1
    else:
        register[c] = 0

def eqrr(register, a, b, c):
    if register[a] == register[b]:
        register[c] = 1
    else:
        register[c] = 0

def checkOperations(operations, instrInput, beforeRegister, afterRegister, operationIdMap):
    count = 0
    for instr in operations:
        currReg = beforeRegister.copy()
        instr(currReg, instrInput[1], instrInput[2], instrInput[3])
        if currReg == afterRegister:
            count += 1
        else:
            if instr in operationIdMap[instrInput[0]]:
                del operationIdMap[instrInput[0]][operationIdMap[instrInput[0]].index(instr)]
    return 1 if count >= 3 else 0

def cleanIdMap(operationIdMap):
    newIdMap = {}
    done = False
    while not done:
        done = True
        for key, value in operationIdMap.items():
            if len(value) == 1:
                newIdMap[key] = value[0]
                for l in operationIdMap.values():
                    if newIdMap[key] in l:
                        l.remove(newIdMap[key])
                done = False
                break
    return newIdMap


if __name__ == '__main__':
    operations = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
    part1 = 0
    operationIdMap = defaultdict(lambda: operations.copy())
    with open('input.txt', 'r') as f:
        while True:
            line = f.readline()
            if not 'Before' in line:
                f.readline()
                operationIdMap = cleanIdMap(operationIdMap)
                register = [0, 0, 0, 0]
                for line in f.readlines():
                    l = list(map(int, line.strip().split()))
                    operationIdMap[l[0]](register, l[1], l[2], l[3])
                print('Register 0 is: ' + str(register[0]))
                break
            beforeRegister = eval(line.strip()[8:])
            instrInput = list(map(int, f.readline().strip().split()))
            operationIdMap[instrInput[0]]
            line = f.readline()
            afterRegister = eval(line.strip()[8:])
            f.readline()
            part1 += checkOperations(operations, instrInput, beforeRegister, afterRegister, operationIdMap)
    print('Nbr of samples that have 3 or more opcodes: ' + str(part1))


