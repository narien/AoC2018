def calcChecksum(lines):
    doubles = 0
    triples = 0

    for line in lines:
        AlphaCounter = {}
        for char in line:
            if char in AlphaCounter:
                AlphaCounter[char] += 1
            else:
                AlphaCounter[char] = 1
        if 2 in AlphaCounter.values():
            doubles += 1
        if 3 in AlphaCounter.values():
            tripples += 1
    print('Checksum is: ' + str(doubles*triples))

# Returns error count
def compareStrings(stringA, stringB):
    errorCount = 0
    for i in range(len(stringA)):
        if stringA[i] != stringB[i]:
            errorCount += 1
    return errorCount

def findBoxPair(lines):
    startIndex = 1
    for currId in lines:
        for index in range(startIndex, len(lines)):
            if compareStrings(currId, lines[index]) == 1:
                string = ''
                for charIndex in range(len(currId)):
                    string += currId[charIndex] if currId[charIndex] == lines[index][charIndex] else ''
                print ('Matching chars are: ' + string)
                return
        startIndex += 1

# Run program with input.txt in same folder.
if __name__ == '__main__':
    inputList = []
    with open('input.txt', 'r') as f:
      for line in f.readlines():
            inputList.append((line.strip()))

    calcChecksum(inputList)
    findBoxPair(inputList)
