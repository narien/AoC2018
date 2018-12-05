import string

def reduce(string):
    ix = 0
    while ix < len(string):
        if ix <= -1:
            ix = 0
        asciiVal = ord(string[ix])
        if ix + 1 < len(string):
            if string[ix].upper() == string[ix+1].upper() and string[ix] != string[ix+1]:
                string = string[:ix] + string[ix+2:]
                ix -= 2
        ix += 1
    return string

def removeUnitAndReduce(string, char):
    string = string.replace(char, "")
    string = string.replace(char.upper(), "")
    return reduce(string)

# Run program with input.txt in same folder.
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read().strip()
    print('Part1 reduced string: ' +str(len(reduce(input))))

    res = set()
    for char in string.ascii_lowercase:
        res.add(len(removeUnitAndReduce(input, char)))
    print('Part2 Shortest polymer is: ' + str(min(res)))