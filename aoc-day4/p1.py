import sys

pointSum = 0

with open(sys.argv[1], "r") as file:
    for row in file:
        worthPoints = 0
        justPoints = row.split(":")[1].strip()

        winningCards = set([int(i) for i in justPoints.split("|")[0].strip().split()]) # List of all winning card numbers
        ownedCards = [int(i) for i in justPoints.split("|")[1].strip().split()] # List of all owned card numbers

        for card in ownedCards:
            if card in winningCards:
                if worthPoints == 0:
                    worthPoints = 1
                else: 
                    worthPoints *= 2 

        pointSum += worthPoints

print(pointSum)

        