import sys

def partOne(iterations):
    scores = [3, 7]
    elfOne = 0
    elfTwo = 1
    while len(scores) < iterations + 10:
        newBlend = scores[elfOne] + scores[elfTwo]
        scores += [int(i) for i in str(newBlend)]
        elfOne = (1 + scores[elfOne] + elfOne) % len(scores)
        elfTwo = (1 + scores[elfTwo] + elfTwo) % len(scores)
    print(scores[iterations:iterations+10])

def partTwo(sequence):
    scores = [3, 7]
    elfOne = 0
    elfTwo = 1
    sequenceIx = 0
    sequenceLength = len(sequence)
    while True:
        newBlend = scores[elfOne] + scores[elfTwo]
        scores += [int(i) for i in str(newBlend)]
        elfOne = (1 + scores[elfOne] + elfOne) % len(scores)
        elfTwo = (1 + scores[elfTwo] + elfTwo) % len(scores)
        if len(scores) >= len(sequence):
            if scores[sequenceIx:sequenceIx+sequenceLength] == sequence:
                break
            else:
                sequenceIx += 1
    print('Recipes before: ' + str(sequenceIx))


if __name__ == '__main__':
    iterations = int(sys.argv[1])
    sequence = [int(i) for i in str(iterations)]
    partOne(iterations)
    partTwo(sequence)


