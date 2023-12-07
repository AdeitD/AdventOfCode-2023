import sys

numReplace = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}

counter = 0

with open(sys.argv[1], "r") as file:
    for row in file:
        rowLen = len(row)
        finalNumber = ""
        for idx, x in enumerate(row):
            try:
                int(x)
            except:
                for alphaNum, num in numReplace.items():
                    if row[idx:rowLen].startswith(alphaNum):
                        finalNumber += num
            else:
                finalNumber += x

        deciphered = finalNumber[0] + finalNumber[-1]

        counter += int(deciphered)

print(counter)
