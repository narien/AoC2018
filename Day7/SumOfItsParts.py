import string

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

def timeTick(pendingChars, requiredBy, startList, resString, workers):
    resString[0] += 1
    charsToDel = []
    for char in pendingChars:
        if pendingChars[char] == resString[0]:
            charsToDel.append(char)
            resString[1] = resString[1] + char
            if char in requiredBy:
                startList.extend(requiredBy[char])
                startList.sort()
    for char in charsToDel:
        del pendingChars[char]
    for worker in workers:
        if workers[worker] == resString[0]:
            workers[worker] = 0
    return resString

def findJob(requires, requiredBy, startList, resString, worker, workers):
    char = startList.pop(0)
    if char not in requires and char not in resString[1]:
        executionDone = resString[0] + 61 + string.ascii_uppercase.find(char)
        pendingChars[char] = executionDone
        workers[worker] =  executionDone
    elif char in requires and char not in resString[1]:
        isReady = True
        for reqChar in requires[char]:
            if reqChar not in resString[1]:
                isReady = False
                break
        if isReady:
            executionDone = resString[0] + 61 + string.ascii_uppercase.find(char)
            pendingChars[char] = executionDone
            workers[worker] =  executionDone

if __name__ == '__main__':
    requires = {}
    requiredBy = {}
    pendingChars = {}
    workers = {1:0, 2:0, 3:0, 4:0, 5:0} # 
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
    resString = [-1, ""]

    while len(startList) or len(pendingChars):
        print('startlist ' + str(startList))
        print('pendingchars ' + str(pendingChars))
        print('time ' + str(resString[0]) + ' resstring ' + resString[1])
        for worker in workers:
            if workers[worker] == 0 and len(startList):
                findJob(requires, requiredBy, startList, resString, worker, workers)
        resString = timeTick(pendingChars, requiredBy, startList, resString, workers)

    print('Result string: ' + str(resString))