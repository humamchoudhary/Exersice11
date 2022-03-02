from random import *
DECK = [{'value': i, 'suit': c}
        for c in ['spades', 'clubs', 'hearts', 'diamonds']
        for i in range(2, 15)]

player1 = sample(DECK, 3)
Player_Suit = []
Player_Value = []
# Part A

# THERE ARE VERY LOW CHANCES OF GETTING A FLUSH
for i in player1:
    Player_Suit.append(i['suit'])

print(Player_Suit)
if Player_Suit.count(i) == 3:
    print("Flush!!!")
    print(Player_Suit)


# Part B

# THERE IS A VERY LOW CHANCES OF GETTING THREE OF A KIND
for i in player1:
    Player_Value.append(i['value'])
print(Player_Value)
if Player_Value.count(i) == 3:
    print("THREE OF A KIND")
    print(Player_Value)


# PART C

if Player_Value.count(i) != 3 and Player_Value.count(i) == 2:
    print("THREE OF A KIND")
    print(Player_Value)
count = 0
for i in range(3):
    try:
        if Player_Value[i+1]-Player_Value[i] == 1:
            count += 1
    except:
        pass

if count == 3:
    print("Its a Straight!!!")
