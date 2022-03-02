from random import *
Cards = {'one': 1, 'two': 2, 'three': 3, 'four': 4,
         'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
         'nine': 9, 'ten': 10, 'joker': 11, 'queen': 12,
         'king': 13, 'A': 14}
cards_number = 3
player1 = []
player2 = []
for i in range(cards_number):
    p1 = choice(list(Cards.values()))
    p2 = choice(list(Cards.values()))
    player1.append(p1)
    player2.append(p2)
print(player1, " ", player2)

while True:
    ind1 = player1.index(max(player1))
    ind2 = player2.index(max(player2))
    player1.pop(ind1)
    player2.pop(ind2)

    if max(player1) < max(player2):
        print("Player 2 wins")
        break
    elif max(player2) < max(player1):
        print("Player 1 wins")
        break
    elif max(player1) == max(player2):
        pass
