import sys

schematicList = []
gearRatioSum = 0
gearDict = {}

with open(sys.argv[1], "r") as file:
    for row in file:
        schematicList.append(list(row.strip()))

def isAdjacentToGear(r, c) -> bool:
    for i in range(-1, 2):
        for j in range(-1, 2):
            adjC = c+i
            adjR = r+j

            if adjR < 0 or adjR >= len(schematicList[r]) or adjC < 0 or adjC >= len(schematicList) or (adjR == 0 and adjC == 0):
                continue
            else:
                if schematicList[adjR][adjC] == '*':
                    return (adjR, adjC)
                    
    return ()

def getFullNumber(r, c) -> str: 
    startIdx = c - 1
    endIdx = c + 1
    result = schematicList[r][c]
    schematicList[r][c] = '.'

    while startIdx >= 0 and schematicList[r][startIdx].isdigit():
        result = schematicList[r][startIdx] + result
        schematicList[r][startIdx] = '.'
        
        startIdx -= 1
    
    while endIdx < len(schematicList[r]) and schematicList[r][endIdx].isdigit():
        result += schematicList[r][endIdx]
        schematicList[r][endIdx] = '.'

        endIdx += 1

    return result 

for r, row in enumerate(schematicList):
    for c, char in enumerate(row): # c here stands for column
        if char.isdigit():
            gearCoords = isAdjacentToGear(r, c)

            if gearCoords:
                if gearCoords in gearDict:
                    gearDict[gearCoords].append(int(getFullNumber(r, c)))
                else:
                    gearDict[gearCoords] = [int(getFullNumber(r, c))]

for coord, partNum in gearDict.items():
    if len(partNum) == 2:
        gearRatioSum += partNum[0] * partNum[1]
        

print(gearRatioSum)