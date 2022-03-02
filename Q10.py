Letter = " abcdefghijklmnopqrstuvwxyz "
Letter_Fwds = []
Letter_Bwds = []
for i in Letter:
    Letter_Fwds.append(i)
for i in Letter[::-1]:
    Letter_Bwds.append(i)
Dict = dict(zip(Letter_Fwds, Letter_Bwds))
print(Dict)

Word_In = input("Enter the words to be cyphered: ")
Cyp = []
for i in Word_In.lower():
    Cyp.append(Dict[i])
print(''.join(Cyp))
