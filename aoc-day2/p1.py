import sys

maxRed = 12
maxGreen = 13
maxBlue = 14

validIDSum = 0

with open(sys.argv[1], "r") as file:
    for row in file:
        splitIDSubset = row.split(": ")

        gameID = int(splitIDSubset[0].split()[1])
        cubeSubsets = splitIDSubset[1].split("; ")

        for idx, subset in enumerate(cubeSubsets):
            validGame = True
            separatedByColour = subset.split(", ")

            for colour in separatedByColour:
                if "red" in colour:
                    if int(colour.split()[0]) > maxRed:
                        validGame = False
                        break
                elif "green" in colour:
                    if int(colour.split()[0]) > maxGreen:
                        validGame = False
                        break
                else: # Must be blue cubes
                    if int(colour.split()[0]) > maxBlue:
                        validGame = False
                        break
        
            if not validGame:
                break
            elif idx == len(cubeSubsets) - 1:
                validIDSum += gameID
             
print(validIDSum)