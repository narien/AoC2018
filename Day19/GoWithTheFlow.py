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

if __name__ == '__main__':
    register = [0, 0, 0, 0, 0, 0]
    with open('input.txt', 'r') as f:
        instructionPointer = int(f.readline().strip().split()[1])
        program = []
        for line in f.readlines():
            instr = line.strip().split()
            instr[1] = int(instr[1])
            instr[2] = int(instr[2])
            instr[3] = int(instr[3])
            program.append(instr)

    instructionPointerVal = 0
    while True:
        register[instructionPointer] = instructionPointerVal
        instr = program[instructionPointerVal]
        if instr[0] == "addr":
            addr(register, instr[1], instr[2], instr[3])
        elif instr[0] == "addi":
            addi(register, instr[1], instr[2], instr[3])
        elif instr[0] == "mulr":
            mulr(register, instr[1], instr[2], instr[3])
        elif instr[0] == "muli":
            muli(register, instr[1], instr[2], instr[3])
        elif instr[0] == "banr":
            banr(register, instr[1], instr[2], instr[3])
        elif instr[0] == "bani":
            bani(register, instr[1], instr[2], instr[3])
        elif instr[0] == "borr":
            borr(register, instr[1], instr[2], instr[3])
        elif instr[0] == "bori":
            bori(register, instr[1], instr[2], instr[3])
        elif instr[0] == "setr":
            setr(register, instr[1], instr[2], instr[3])
        elif instr[0] == "seti":
            seti(register, instr[1], instr[2], instr[3])
        elif instr[0] == "gtir":
            gtir(register, instr[1], instr[2], instr[3])
        elif instr[0] == "gtri":
            gtri(register, instr[1], instr[2], instr[3])
        elif instr[0] == "gtrr":
            gtrr(register, instr[1], instr[2], instr[3])
        elif instr[0] == "eqir":
            eqir(register, instr[1], instr[2], instr[3])
        elif instr[0] == "eqri":
            eqri(register, instr[1], instr[2], instr[3])
        elif instr[0] == "eqrr":
            eqrr(register, instr[1], instr[2], instr[3])
        instructionPointerVal = register[instructionPointer]
        instructionPointerVal += 1
        if instructionPointerVal >= len(program):
            break
    print('Register 0 is: ' + str(register[0]))


