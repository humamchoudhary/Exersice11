TeamsRec = {"Alpha": [12, 5], "Beta": [15, 6],
            "Charlie": [10, 6], "Delta": [0, 12]}


# For adding data of teams
# for i in range(5):
#     Team_Name = input("Enter the name of the team: ")
#     Team_Wins = eval(input("Enter the number of Wins: "))
#     Team_losses = eval(input("Enter the number of losses: "))
#     TeamsRec[Team_Name] = list((Team_Wins, Team_losses))
#     print(TeamsRec)


# # PART A
print("===========- Part A -===========")
Team_Name = input("Enter the name of the team: ")
Team_Value = TeamsRec[Team_Name]

WinAvg = Team_Value[0] / sum(Team_Value)
print(WinAvg)

# PART B
print("===========- Part B -===========")
L = []
for i in TeamsRec:
    Vall = TeamsRec[i][0]
    L.append(Vall)
print(L)

# PART C
print("===========- Part C -===========")
L2 = []
for i in TeamsRec:
    if TeamsRec[i][0] != 0:
        L2.append(i)
print(L2)
