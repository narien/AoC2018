foundDuplicate = False
total = 0
mem = set([0])


def loopOverInput(lines):
    global foundDuplicate, total, mem
    for line in lines:
        total += int(line)
        if not foundDuplicate and total in mem:
            foundDuplicate = True
            print ('First Repeating frequency is: ', str(total))
        else:
            mem.add(total)
    return total

# Run program with input.txt in same folder.
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    print ('Resulting frequency is: ' + str(loopOverInput(lines)))
    while not foundDuplicate:
        loopOverInput(lines)






