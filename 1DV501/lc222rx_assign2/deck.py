# A program that generates a five card hand
# out of a randomly generated deck of cards that is also shuffled
from random import choice
cards = []

amount = 0
x = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
y = {0, 1, 2, 3}
exclude_set = set()
while amount != 52:
    nr = choice(list(x - exclude_set))
    if nr == 11:
        nr = "Jack"
    elif nr == 12:
        nr = "Queen"
    elif nr == 13:
        nr = "King"
    elif nr == 14:
        nr = "Ace"

    suit = choice(list(y - exclude_set))
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
    if card not in cards:
        amount += 1
        cards.append(card)
    # else:
        # exclude_set.add(nr)

new_deck = [0] * 52

A = set()
exclude_set = set()
for i in range(52):
    A.add(i)
amount = 0
while amount != 52:
    rng = choice(list(A - exclude_set))
    if new_deck[rng] == 0:
        new_deck.insert(rng, cards[amount])
        if rng < 52 and len(new_deck) == 53:
            new_deck.pop(rng + 1)
        amount += 1
    else:
        exclude_set.add(rng)

print("My hand:")
for i in range(52):
    print(cards[i])
