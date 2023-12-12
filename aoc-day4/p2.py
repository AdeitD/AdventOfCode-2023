import sys

totalCards = 0
maxCardID = 0
cardsCountDict = {}
cardsWinCountDict = {}

def addNewCards(id): 
    if cardsWinCountDict[id] != 0:
        for i in range(1,cardsWinCountDict[id]+1):
            cardsCountDict[id+i] += 1

with open(sys.argv[1], "r") as file:
    for row in file:
        totalMatchingNumbers = 0
        cardID = int(row.split(':')[0].strip().split()[1]) # ie, first split contains "Card 1", final value: 1
        justPoints = row.split(":")[1].strip() # ie, contains "41 48 83 86 17 | 83 86  6 31 17  9 48 53"

        winningCards = set([int(i) for i in justPoints.split("|")[0].strip().split()]) # List of all winning card numbers
        ownedCards = [int(i) for i in justPoints.split("|")[1].strip().split()] # List of all owned card numbers

        cardsCountDict[cardID] = 1

        totalCards += 1
        maxCardID = max(cardID, maxCardID)

        for card in ownedCards:
            if card in winningCards:
                totalMatchingNumbers += 1 

        cardsWinCountDict[cardID] = totalMatchingNumbers

for id in range(1, maxCardID+1):
    for i in range(1,cardsCountDict[id]+1):
        addNewCards(id)


print(sum(cardsCountDict.values()))
