def sumMetaDataSimple(inputData):
    metadataSum = 0
    children = inputData.pop()
    metaHeader = inputData.pop()

    for _ in range(children):
        metadataSum += sumMetaDataSimple(inputData)
    for _ in range(metaHeader):
        metadataSum += inputData.pop()
    return metadataSum

def sumMetaData(inputData):
    metadataSum = 0
    children = inputData.pop()
    metaHeader = inputData.pop()
    childMetaList = []

    for _ in range(children):
        childMetaList.append(sumMetaData(inputData))
    for _ in range(metaHeader):
        metaData = inputData.pop()
        if children and metaData > 0 and metaData - 1 < len(childMetaList):
            metadataSum += childMetaList[metaData - 1]
        elif not children:
            metadataSum += metaData
    return metadataSum

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        inputData = list(map(int, f.read().split()))[::-1]
    inputData2 = inputData.copy()
    print('Part 1 metadata sum is: ' + str(sumMetaDataSimple(inputData)))
    print('Part 2 metadata sum is: ' + str(sumMetaData(inputData2)))
