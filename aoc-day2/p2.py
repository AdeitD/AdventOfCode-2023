import sys

powerSum = 0

with open(sys.argv[1], "r") as file:
    for row in file:
        maxRed = 0
        maxGreen = 0
        maxBlue = 0

        splitIDSubset = row.split(": ")

        cubeSubsets = splitIDSubset[1].split("; ")

        for idx, subset in enumerate(cubeSubsets):
            separatedByColour = subset.split(", ")

            for colour in separatedByColour:
                if "red" in colour:
                    maxRed = max(maxRed, int(colour.split()[0]))
                elif "green" in colour:
                    maxGreen = max(maxGreen, int(colour.split()[0]))
                else: # Must be blue cubes
                    maxBlue = max(maxBlue, int(colour.split()[0]))

            if idx == len(cubeSubsets) - 1:
                powerSum += maxRed * maxBlue * maxGreen
             
print(powerSum)