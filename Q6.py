Teams = {}
Teams_Num = eval(input("Enter the number teams: "))
for i in range(Teams_Num):
    Name = input(f"Enter the name of {i+1} team: ")
    wins = eval(input(f"Enter the winnings of {Name} team: "))
    lose = eval(input(f"Enter the Loses of {Name} team: "))
    List = []
    List.extend((wins, lose))
    Teams.update({Name: List})
print(Teams)
