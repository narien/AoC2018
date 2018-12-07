def findFirstList(requires, requiredBy):
    result = []
    for char in requiredBy:
        if char not in requires:
            result.append(char)
    result.sort()
    return result

def addChar(char, requiredBy, startList, resString):
    resString = resString + char
    if char in requiredBy:
        startList.extend(requiredBy[char])
    startList.sort()
    return resString

def buildString(requires, requiredBy, startList, resString):
    char = startList.pop(0)
    if char not in requires and char not in resString:
        resString = addChar(char, requiredBy, startList, resString)
    elif char in requires and char not in resString:
        isReady = True
        for reqChar in requires[char]:
            if reqChar not in resString:
                isReady = False
                break
        if isReady:
            resString = addChar(char, requiredBy, startList, resString)
    return resString

if __name__ == '__main__':
    requires = {}
    requiredBy = {}
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            chars = line.split()
            if chars[7] not in requires:
                requires[chars[7]] = [chars[1]]
            else:
                requires[chars[7]].append(chars[1])
            if chars[1] not in requiredBy:
                requiredBy[chars[1]] = [chars[7]]
            else:
                requiredBy[chars[1]].append(chars[7])
    for l in requiredBy.values():
        l.sort()
    for l in requires.values():
        l.sort()
#    print('RequiredBy: ' + str(requiredBy))
#    print('Requires: ' + str(requires))

    startList = findFirstList(requires, requiredBy)
    resString = ""

    while len(startList):
        resString = buildString(requires, requiredBy, startList, resString)
    print('Result string: ' + resString)