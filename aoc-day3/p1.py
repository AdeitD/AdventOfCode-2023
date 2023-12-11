import sys

schematicList = []
partNumberSum = 0

with open(sys.argv[1], "r") as file:
    for row in file:
        schematicList.append(list(row.strip()))

def isAdjacentToSymbol(r, c) -> bool:
    for i in range(-1, 2):
        for j in range(-1, 2):
            adjC = c+i
            adjR = r+j

            if adjR < 0 or adjR >= len(schematicList[r]) or adjC < 0 or adjC >= len(schematicList) or (adjR == 0 and adjC == 0):
                continue
            else:
                adjacentChar = schematicList[adjR][adjC]
                if not (adjacentChar.isdigit() or adjacentChar == '.'):
                    return True
                    
    return False

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
    for c, char in enumerate(row): # c here stands for column index
        if char.isdigit() and isAdjacentToSymbol(r, c):
            partNumberSum += int(getFullNumber(r, c))

print(partNumberSum)