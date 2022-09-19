# A program that generates a five card hand
# out of a randomly generated deck of cards that is also shuffled
from random import randrange, shuffle
cards = []

for i in range(0, 52):
    nr = randrange(2, 14)
    if nr == 11:
        nr = "Jack"
    elif nr == 12:
        nr = "Queen"
    elif nr == 13:
        nr = "King"
    elif nr == 14:
        nr = "Ace"

    suit = randrange(4)
    if suit == 0:
        suit = " of Clubs"
    elif suit == 1:
        suit = " of Hearts"
    elif suit == 2:
        suit = " of Spades"
    elif suit == 3:
        suit = " of Diamonds"

    if type(nr) == int:
        card = str(nr) + suit
    else:
        card = nr + suit
    cards.append(card)
shuffle(cards)

print("My hand:")
for i in range(5):
    print(cards[i])
